"""
The first benchmark in the PiperBench project.

This benchmark tests the backend's ability to convert written numbers in text to digits.
"""

import json5 as json

# Load settings
settings = json.load(open('settings.json'))

num_range = settings['Test-Settings']['TextToDigit']['Number-Range']

# Load the backend and dependecies
import Backend
import num2words
import numpy as np
import re

def GeneratePrompt():
    number = np.random.randint(num_range[0], num_range[1])
    number_str = num2words.num2words(number)

    return f"Convert the following sequence of words into a number: {number_str}. Output just your final answer.\nAnswer: ", number

def TestOne():
    prompt, number = GeneratePrompt()
    answer = Backend.Generate(prompt)

    # Remove all non-digit characters
    result = re.sub('[^0-9]', '', answer)

    if result == "":
        return False
    if result[0].isdigit() == False:
        return False

    return int(result) == number

if __name__ == "__main__":
    import time
    import datetime
    import os
    clear = lambda: os.system('cls')
    clear()

    seed = settings['Test-Settings']['Seed']
    N_test = settings['Test-Settings']['Iterations']

    np.random.seed(seed)

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

    clear()
    print("Results:")
    print(f"Time elapsed: {str(datetime.timedelta(seconds=int(time_elapsed)))}")
    print(f"Accuracy: {correct / N_test * 100:.2f}%")
