# app.py
from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
import nltk

nltk.download('punkt')  # for tokenizing sentences if needed

app = Flask(__name__)

# Load your FAQs
with open('faq.json') as f:
    faq_data = json.load(f)

# Grab all the questions
questions = [item['question'] for item in faq_data]

# Turn words into numbers (like teaching robot to read)
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)

from flask import send_from_directory

# Route for root URL to serve index.html
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/chat', methods=['POST'])
@app.route('/chat', methods=['POST'])
def chat():
    user_question = request.json.get('question')

    # Convert user question into vector
    user_vector = vectorizer.transform([user_question])

    # Find similarity with known questions
    similarity = cosine_similarity(user_vector, question_vectors)
    best_match_index = similarity.argmax()

    # Get answer and link
    answer = faq_data[best_match_index]['answer']
    link = faq_data[best_match_index].get('link', '')

    # Suggestions (top 3 similar, excluding the best match)
    similarities = similarity.flatten()
    top_indices = similarities.argsort()[-3:][::-1]
    suggestions = [faq_data[i]['question'] for i in top_indices if i != best_match_index]

    return jsonify({
        'question': faq_data[best_match_index]['question'],
        'answer': answer,
        'link': link,
        'suggestions': suggestions
    })


if __name__ == '__main__':
    app.run(debug=True)
