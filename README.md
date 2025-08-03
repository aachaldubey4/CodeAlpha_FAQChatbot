# CodeAlpha_FAQChatbot
This chatbot was proudly created by Aachal Dubey 
💻 MCA Student | Intern at CodeAlpha 
✨ Passionate about AI, Web, and Real-World Projects!

# 🤖 FAQ Chatbot using Python & Flask

This is an intelligent FAQ Chatbot created by **Aachal Dubey** as part of an internship at **Code Alpha**.  
It answers user questions using Natural Language Processing and gives the best-matched answers from a predefined FAQ dataset.

---

## 📌 Features

✅ Match user input to most relevant FAQ using cosine similarity  
✅ Display top 3 suggested similar questions  
✅ Show "Learn More" links with each answer  
✅ Users can rate responses using 👍 / 👎 feedback  
✅ Dark Mode toggle with sleek modern UI  
✅ Personalized response if asked “Who created you?”

---

## 🧠 Tech Stack

- **Python 3**
- **Flask** (Backend API)
- **HTML, CSS, JS** (Frontend)
- **Scikit-learn** (TF-IDF, cosine similarity)
- **NLTK** (Text preprocessing)

---

## 🚀 Project Structure

CodeAlpha_FAQChatbot/
│
├── app.py # Flask backend API
├── index.html # Frontend UI with chatbox and dark mode
├── faq.json # Question-answer dataset with optional links
├── package.json # NLTK dependency




---

## 📦 Setup Instructions

### ✅ 1. Clone the Repository

```bash
git clone https://github.com/aachaldubey4/CodeAlpha_FAQChatbot.git
cd CodeAlpha_FAQChatbot

✅ 2. Install Requirements

pip install flask scikit-learn nltk


✅ 3. Run the Server

python app.py

