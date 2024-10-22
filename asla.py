import json

with open('faqs.json', 'r') as file:
    faq_data = json.load(file) 
print(faq_data)