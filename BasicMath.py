"""
This benchmark tests the backend's ability to perform basic math.
"""

import json5 as json

# Load settings
settings = json.load(open('settings.json'))

seed = settings['Test-Settings']['Seed']
num_range = settings['Test-Settings']['BasicMath']['Number-Range']
operations = settings['Test-Settings']['BasicMath']['Operations']

N_test = settings['Test-Settings']['Iterations']

# Load the backend and dependecies
import Backend
import numpy as np
import time
import os
import datetime
import re
clear = lambda: os.system('cls')
clear()

np.random.seed(seed)

def GeneratePrompt():
    number1 = np.random.randint(num_range[0], num_range[1])
    number2 = np.random.randint(num_range[0], num_range[1])
    operation = np.random.choice(operations)

    prompt = f"Solve the following equation: {number1} {operation} {number2}. Output just your final answer, do not include the equation.\nAnswer: "
    return prompt, number1, number2, operation

def ResultOne(number1, number2, operation):
    return {'+': (lambda x, y: x + y), '-': (lambda x, y: x - y), '*': (lambda x, y: x * y), '/': (lambda x, y: x / y)}[operation](number1, number2)

def TestOne():
    prompt, number1, number2, operation = GeneratePrompt()
    answer = Backend.Generate(prompt)

    # Remove all non-digit characters, include minus signs and decimal points
    result = re.sub('[^0-9-.]', '', answer)

    if result == "":
        return False

    try:
        return float(result) == ResultOne(number1, number2, operation)
    except:
        return False

correct = 0
time_start = time.time()

for i in range(N_test):
    if TestOne():
        correct += 1
    
    clear()
    print(f"Time elapsed: {str(datetime.timedelta(seconds=int(time.time() - time_start)))}")
    print(f"Test {i + 1}/{N_test}: {correct / (i + 1) * 100:.2f}%")

time_end = time.time()
time_elapsed = time_end - time_start
