
# FAQ Search Application with FastAPI and Sentence-BERT

This repository contains a simple FAQ search functionality using [FastAPI](https://fastapi.tiangolo.com/) and [Sentence-BERT](https://www.sbert.net/). The application consists of a FastAPI backend that processes search queries and a frontend built with HTML, CSS, and JavaScript to interact with the backend.

## Table of Contents

- [Installation](#installation)
- [Project Structure](#project-structure)
- [Running the Application](#running-the-application)
- [Explanation](#explanation)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/faq-search-app.git
cd faq-search-app
```

### 2. Set Up the Backend

Make sure you have Python 3.7+ installed.

Install the required Python packages:

```bash
pip install fastapi uvicorn sentence-transformers torch
```

### 3. Frontend Setup

The frontend is a simple HTML file. No additional dependencies are needed. 

## Project Structure

```bash
.
├── main.py              # FastAPI backend handling search functionality
├── index.html           # Frontend for the FAQ search
├── README.md            # Project documentation
└── requirements.txt     # Python dependencies (optional)
```

## Running the Application

### 1. Start the FastAPI Backend

Run the following command to start the backend server:

```bash
uvicorn main:app --reload
```

The backend will be available at `http://127.0.0.1:8000`.

### 2. Open the Frontend

Open the `index.html` file in your browser. Make sure the FastAPI server is running, as the frontend fetches results from `http://127.0.0.1:8000/search`.
![Screenshot from 2024-10-22 23-00-29](https://github.com/user-attachments/assets/36108b6b-55d0-4aa9-902f-eac036b0f6fe)

## Explanation

This application consists of two components:

### Backend (FastAPI)
- The FastAPI backend uses the **Sentence-BERT** model to process and find the most relevant FAQs for a given search query.
- **Cosine similarity** is used to match user queries to pre-embedded FAQs.
- The backend includes a single API route `/search` where the frontend sends search queries and receives results.

### Frontend (HTML, CSS, JS)
- The frontend provides a simple user interface where users can enter a search query and receive FAQ results.
- JavaScript is used to dynamically fetch search results from the backend and display them without refreshing the page.

### How It Works
1. The **backend** loads a predefined set of FAQ questions and their answers, embedding them using **Sentence-BERT**.
2. When a user submits a search query, the backend compares the query to the FAQ embeddings and returns the most relevant results using **cosine similarity**.
3. The **frontend** displays the results dynamically, with each FAQ's section, question, answer, and similarity score.
![Screenshot from 2024-10-22 23-38-16](https://github.com/user-attachments/assets/003871af-147e-4890-aebb-dd62ac465653)
![Screenshot from 2024-10-22 23-37-42](https://github.com/user-attachments/assets/cbd25a56-dbf1-4d17-a5c2-2ccb31dcb664)
