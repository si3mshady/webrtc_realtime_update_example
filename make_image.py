import requests
import os

OPENAI_API_KEY = 'sk-'; 

def generate_image_url(prompt):
    url = "https://api.openai.com/v1/images/generations"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }
    data = {
        "model": "dall-e-3",
        "prompt": prompt,
        "n": 1,
        "size": "1024x1024"
    }
    response = requests.post(url, headers=headers, json=data)
    response_data = response.json()
    return response_data["data"]

# Example usage
prompt = "A talking head avatar that is a woman that could exist in the move The Matrix, she must have a close mouth,  beautiful eyes"
image_url = generate_image_url(prompt)
print(image_url)