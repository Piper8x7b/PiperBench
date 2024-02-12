"""
Backend.py

This module contains the functions for the backend.
The backend is what generates all the text for the game.
"""

import json5 as json

# Load settings
settings = json.load(open('settings.json'))

# Load WebUI API backend
if settings['Backend'] == 'text-generation-webui':
    import requests
    
    # Headers for WebUI
    headers = {
        "Content-Type": "application/json"
    }

    def Generate(prompt):
        """
        The Generate function takes a prompt as input and returns a text generated based on the prompt.
        
        Args:
        - prompt (str): The prompt for text generation.

        Returns:
        - str: The generated text based on the prompt.
        """
        # Prepare data for the request
        data = {
            "prompt": prompt,
            "max_tokens": settings['Text-Generation']['max_tokens'],
            "temperature": settings['Text-Generation']['temperature'],
            "top_p": settings['Text-Generation']['top_p'],
            "stop": settings['Text-Generation']['stop']
        }

        # Send a request to the WebUI API for text generation
        response = requests.post(url=settings['Backend-Settings']['WebUI-API'], headers=headers, json=data, verify=False).json()

        # Extract and return the generated text
        return response.get("choices")[0].get("text")

# Load Langchain backend    
elif settings['Backend'] == 'langchain':
    from langchain_community.llms import LlamaCpp

    # Load the LlamaCpp model
    llm = LlamaCpp(
        model_path = settings['Backend-Settings']['Langchain-Model'],
        n_ctx = settings['Backend-Settings']['Langchain-Settings']['n_ctx'],
        n_gpu_layers = settings['Backend-Settings']['Langchain-Settings']['n_gpu_layers'],
        n_batch = settings['Backend-Settings']['Langchain-Settings']['n_batch'],
        verbose = settings['Backend-Settings']['Langchain-Settings']['verbose'],

        model_kwargs = {
            "f_16_kb": settings['Backend-Settings']['Langchain-Settings']['f_16_kb']
        },

        temperature = settings['Text-Generation']['temperature'],
        top_p = settings['Text-Generation']['top_p'],
        stop = settings['Text-Generation']['stop']
    )

    def Generate(prompt):
        """
        The Generate function takes a prompt as input and returns a text generated based on the prompt.
        
        Args:
        - prompt (str): The prompt for text generation.

        Returns:
        - str: The generated text based on the prompt.
        """
        return llm.invoke(prompt)
    
# Load OpenAI backend
elif settings['Backend'] == 'openai':
    from openai import OpenAI

    # Open a OpenAI client
    client = OpenAI(
        api_key = settings['Backend-Settings']['OpenAI-key']
    )

    def Generate(prompt):
        """
        The Generate function takes a prompt as input and returns a text generated based on the prompt.
        
        Args:
        - prompt (str): The prompt for text generation.

        Returns:
        - str: The generated text based on the prompt.
        """
        # Create a completion using OpenAI API
        completion = client.chat.completions.create(
            model=settings['Backend-Settings']['OpenAI-Model'],
            max_tokens=settings['Text-Generation']['max_tokens'],
            temperature=settings['Text-Generation']['temperature'],
            top_p=settings['Text-Generation']['top_p'],
            stop=settings['Text-Generation']['stop'],
            messages=[
                {'role': 'system', 'content': 'You are a professional assistant. Your task is to predict the completion to a prompt given by the user. Respond with just your completion.'},
                {'role': 'user', 'content': 'Prompt: ' + prompt}
            ]
        )

        return completion.choices[0].message.content

# Test the backend
if __name__ == '__main__':
    print('The quick brown fox ' + Generate('The quick brown fox '))
