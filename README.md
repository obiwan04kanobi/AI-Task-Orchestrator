# AI Task Orchestrator

AI Orchestrator is a Flask-based application that dynamically selects and runs Docker containers for different AI tasks (e.g., data cleaning, sentiment analysis) based on user input. It uses an LLM API to decide which container to execute.

## 📋 Features

- Dynamic Task Orchestration via LLM API
- Supports Multiple AI Tasks (e.g., Sentiment Analysis, Data Cleaning)
- Dockerized Environment
- Flask Web Interface for User Input

## 🗂️ Project Structure

```
AI-Task-Orchestrator/
├── Dockerfile
├── app.py (Flask Orchestrator)
├── services/
│   ├── sentiment_analyzer/
│   │     ├── Dockerfile
│   │     └── analyzer.py
│   └── data_cleaner/
│         ├── Dockerfile
│         └── cleaner.py
└── templates/
      └── index.html
```

## 🛠️ Setup Instructions

1. **Clone the Repository:**

```bash
git clone https://github.com/obiwan04kanobi/AI-Task-Orchestrator
cd AI-Task-Orchestrator
```

2. **Set Up Environment:**

Ensure you have Docker and Python installed.

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

3. **Environment Variables:**

Create a `.env` file with your LLM API key:

```
GROQ_API_KEY=your_api_key_here
```

4. **Build Docker Images:**

```bash
docker build -t data_cleaner ./services/data_cleaner
docker build -t sentiment_analyzer ./services/sentiment_analyzer
```

5. **Run the Flask Application:**

```bash
python app.py
```

6. **Access the Web UI:**

Navigate to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 📊 System Architecture

![Architecture Diagram](/system_design_architecture.png)

1. User input is received via Flask Web UI.
2. The LLM API determines which AI task to run.
3. Relevant Docker container is executed with user input.
4. Output is returned to the user.

## 📽️ Demo Video

[Demo Video Link 🔗](https://drive.google.com/file/d/1AcRoim5ldMaWE1enErS4Q9ZEb2NKB_y6/view?usp=sharing)

## 📦 Docker Containers

1. **Data Cleaner** - Cleans noisy text.
2. **Sentiment Analyzer** - Analyzes sentiment (positive/negative).

## 🧪 Example Usage

1. Input: `Clean this text @2025`

   Output: `Clean this text 2025`

2. Input: `Analyze the sentiment of: I love this product!`

   Output: `Positive`

---
