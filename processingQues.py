import os
import spacy

# Load the spaCy model
nlp = spacy.load('en_core_web_sm')

# Corrected directory paths
questions_dir = r'C:\Users\naman\OneDrive\Desktop\webscraper\questions'
processed_dir = r'C:\Users\naman\OneDrive\Desktop\webscraper\processed_questions'
os.makedirs(processed_dir, exist_ok=True)

def extract_questions(text):
    doc = nlp(text)
    questions = []
    
    for sent in doc.sents:
        text = sent.text.strip()
        if '?' in text or text.startswith(('Q', 'What', 'Explain', 'How', 'Describe', 'Implement', 'Why', 'Algorithm','algo','data structure','array','integer','given','find','output','input','time complexity','space complexity','complexity','code','program','write','function','method','class','object','inheritance','polymorphism','encapsulation','abstraction','interface','abstract class','concrete class','list','ds','dsa','oops','os','dbms')):
            questions.append(text)
            questions.append('\n')

    return questions

for file in os.listdir(questions_dir):
    file_path = os.path.join(questions_dir, file)
    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        questions = extract_questions(content)
        
        processed_file_path = os.path.join(processed_dir, file)
        with open(processed_file_path, 'w', encoding='utf-8') as f:
            for question in questions:
                f.write(question + '\n')

print(f"Processed files saved to {processed_dir}")
