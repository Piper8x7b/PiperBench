seed = 128
num_range = (0, 1_000_000)

N_test = 1000
model_name = "laserxtral-Q3_K_XS.gguf"

import Backend
import num2words
import numpy as np
import time
import os
import datetime
import re
clear = lambda: os.system('cls')
clear()

np.random.seed(seed)

def GeneratePrompt():
    number = np.random.randint(num_range[0], num_range[1])
    number_str = num2words.num2words(number)

    return f"Convert the following sequence of words into a number: {number_str}. Output just your final answer.\nAnswer: ", number

def TestOne():
    prompt, number = GeneratePrompt()
    answer = Backend.Generate(prompt)

    #get just the number
    result = re.sub('[^0-9]', '', answer)

    if result == "":
        return False
    if result[0].isdigit() == False:
        return False

    return int(result) == number

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

# Save the results
with open("Correctness.txt", "a") as f:
    f.write(f"Model {model_name}: {correct / N_test * 100:.2f}% out of {N_test} iterations\n")
    f.write(f"Time elapsed: {str(datetime.timedelta(seconds=int(time_elapsed)))}\n")