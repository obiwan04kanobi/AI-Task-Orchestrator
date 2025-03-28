from flask import Flask, request, render_template, jsonify
import requests
import subprocess
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)


LLM_API_URL = "https://api.groq.com/openai/v1/chat/completions"
LLM_API_KEY = os.getenv('GROQ_API_KEY') 

def get_llm_response(prompt):
    """Query the LLM to decide which container to run."""
    headers = {
        "Authorization": f"Bearer {LLM_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama-3.3-70b-versatile",  
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        response = requests.post(LLM_API_URL, json=payload, headers=headers)
        response.raise_for_status()  
        return response.json()["choices"][0]["message"]["content"].strip()
    except requests.RequestException as e:
        print(f"Error while calling LLM API: {e}")
        return "LLM API error"
    except KeyError:
        print(f"Unexpected LLM response: {response.json()}")
        return "Invalid LLM response"

def run_container(image_name, input_data):
    """Run a Docker container and return the output."""
    try:
        
        if isinstance(input_data, bytes):
            input_data = input_data.decode()  
        
        print(f"Running: docker run --rm -i {image_name} with input: {input_data}")

        result = subprocess.run(
            ["docker", "run", "--rm", "-i", image_name],  
            input=input_data, 
            capture_output=True,
            text=True
        )
        
        
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            print(f"Docker Error: {result.stderr.strip()}")
            return f"Docker Error: {result.stderr.strip()}"
    
    except Exception as e:
        print(f"Error running Docker container: {e}")
        return "Docker execution error"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']

        
        decision = get_llm_response(f"Determine the task: {user_input}")

        if "clean" in decision.lower():
            output = run_container("data_cleaner", user_input)
        elif "sentiment" in decision.lower():
            output = run_container("sentiment_analyzer", user_input)
        else:
            output = "Task not recognized."

        return jsonify({"decision": decision, "output": output})

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
