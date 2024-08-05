import os
import spacy

# Load the spaCy model
nlp = spacy.load('en_core_web_sm')

# Corrected directory paths
questions_dir = r'C:\Users\naman\OneDrive\Desktop\webscraper\processed_questions'
processed_dir = r'C:\Users\naman\OneDrive\Desktop\webscraper\refined_questions'
os.makedirs(processed_dir, exist_ok=True)

def extract_questions(text):
    doc = nlp(text)
    questions = [sent.text for sent in doc.sents if '?' in sent.text]
    return questions

def refine_question(question):
    refined_question = question.strip()
    topic = "Unknown Topic"  # You can later improve this with a topic classification function
    test_cases = [
        {"input": "example_input", "expected_output": "example_output"},
        # Add more test cases based on the question type
    ]
    edge_cases = ["edge_case_1", "edge_case_2"]  # Define relevant edge cases
    return {
        "question": refined_question,
        "topic": topic,
        "test_cases": test_cases,
        "edge_cases": edge_cases
    }

for file in os.listdir(questions_dir):
    if os.path.isfile(os.path.join(questions_dir, file)):
        with open(os.path.join(questions_dir, file), 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        questions = extract_questions(content)
        refined_questions = [refine_question(q) for q in questions]

        with open(os.path.join(processed_dir, file), 'w', encoding='utf-8') as f:
            for refined_question in refined_questions:
                f.write(f"Question: {refined_question['question']}\n")
                f.write(f"Topic: {refined_question['topic']}\n")
                f.write("Test Cases:\n")
                for test_case in refined_question['test_cases']:
                    f.write(f"  Input: {test_case['input']} => Expected Output: {test_case['expected_output']}\n")
                f.write("Edge Cases:\n")
                for edge_case in refined_question['edge_cases']:
                    f.write(f"  {edge_case}\n")
                f.write("\n")
