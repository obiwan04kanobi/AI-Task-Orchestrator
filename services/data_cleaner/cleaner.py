import sys
import re

def clean_text(text):
    return re.sub(r'[^a-zA-Z0-9 ]', '', text)

if __name__ == "__main__":
    input_text = sys.stdin.read()
    print(clean_text(input_text))
