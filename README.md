# 🤖 Git Tutor CLI — Powered by Gemini

An AI-powered command-line assistant that helps you learn Git and GitHub interactively.

This project simulates a real-world development workflow using Git branches (`dev → staging → main`) while building an intelligent assistant using Google's Gemini API.

---

## 🚀 Features

- 💬 Ask any Git or GitHub question in natural language
- ⚡ Fast responses using Gemini 2.5 Flash
- 🎯 Beginner-friendly explanations with exact commands
- 🔒 Secure API key handling using `.env`
- 🧠 Context-aware conversation (chat session memory)

---

## 🛠️ Tech Stack

- Python
- Google Gemini API (`google-genai`)
- dotenv (for environment management)
- Git & GitHub (branching + PR workflow)

---

## 📦 Setup Instructions

### 1. Clone the repository

git clone https://github.com/tulika105/Git-Learning.git
cd Git-Learning

---

### 2. Install dependencies

pip install -r requirements.txt  

---

### 3. Add your API key

Create a `.env` file:

GEMINI_API_KEY=your_api_key_here  

---

### 4. Run the app

python git_tutor.py  

---

## 💡 Example

You: what is git commit?  

Git Tutor: `git commit` saves your staged changes and creates a snapshot of your project.

---

## 🔁 Git Workflow Used

dev → staging → main  

- `dev` → feature development  
- `staging` → testing  
- `main` → production-ready code  

---

## 🎯 Learning Goals

- Understand Git commands through AI interaction  
- Practice real-world Git workflows (branches + PRs)  
- Learn API integration and environment management  
- Build production-ready CLI tools  

---

