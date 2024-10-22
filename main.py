import time
from sentence_transformers import SentenceTransformer, util
import torch
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

# Load the Sentence-BERT model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Create an instance of the FastAPI app
app = FastAPI()

# Allow CORS so the frontend can communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sample nested FAQ data
import json

with open('faqs.json', 'r') as file:
    faq_data = json.load(file)  

# Flatten the FAQ data and generate embeddings
faqs = []
faq_embeddings = {}
faq_counter = 0
for section, section_faqs in faq_data.items():
    for faq in section_faqs:
        faqs.append({"section": section, "question": faq["question"], "answer": faq["answer"]})
        faq_embeddings[faq_counter] = model.encode(faq["question"] + " " + faq["answer"], convert_to_tensor=True)
        faq_counter += 1

# Search function
def search_faq(query, threshold=0.7):
    query_embedding = model.encode(query, convert_to_tensor=True)
    scores = {
        i: util.pytorch_cos_sim(query_embedding, emb).item()
        for i, emb in faq_embeddings.items()
    }
    max_score = max(scores.values())
    results = [
        {
            "section": faqs[i]['section'],
            "question": faqs[i]['question'],
            "answer": faqs[i]['answer'],
            "score": score
        }
        for i, score in scores.items()
        if score >= max_score * threshold
    ]
    results = sorted(results, key=lambda x: x["score"], reverse=True)
    return results

# Route for searching FAQs
@app.post("/search")
async def search_faq_api(request: Request):
    body = await request.json()
    query = body.get("query")
    if query:
        results = search_faq(query)
        return JSONResponse(content={"results": results})
    return JSONResponse(content={"error": "Invalid request"}, status_code=400)
