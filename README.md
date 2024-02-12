# PiperBench
A tragically simple Large Language Model benchmark.
Model's are simply tested based on how well they can convert written forms of numbers to their digital forms
 # Current results
The benchmark was run on a 3060 12gb, 32 gigabytes of ram at 3200MHz, and a AMD Ryzen 7 5700G.
[text-generation-webui](https://github.com/oobabooga/text-generation-webui) was used for inference.
Parameters used:
- max_tokens: 64
- temperature: 1.33
- top_: 0.33
- seed: 42

[Suggest models](https://docs.google.com/forms/d/e/1FAIpQLSc3DGjwiyVN3zr2A-5AGetLj_815uEONWRE09lIjpEYdpx35w/viewform?usp=sf_link)

 ## Average
| Model | Accuracy | Iterations tested | Time elapsed |
|--|--|--|--|
|mixtral-8x7b-v0.1.Q3_K_M.gguf | 64.85% | 1000 | 0:55:16 |
|mistral-7b-instruct-v0.2.Q5_K_M.gguf | 59.00% | 1000 | 0:17:40 |
|collectivecognition-v1.1-mistral-7b.Q5_K_M.gguf | 56.3% | 1000 | 0:14:53 |
|neuralbeagle14-7b.Q5_K_M.gguf | 46.60% | 1000 | 0:15:32 |
|laserxtral-Q3_K_XS.gguf | 40.75% | 1000 | 0:31:55 |

 ## Correctness

| Model | Accuracy | Iterations tested | Time elapsed |
|--|--|--|--|
|mixtral-8x7b-v0.1.Q3_K_M.gguf | 85.10% | 1000 | 0:56:00 |
|collectivecognition-v1.1-mistral-7b.Q5_K_M.gguf | 79.70% | 1000 | 0:15:32 |
|mistral-7b-instruct-v0.2.Q5_K_M.gguf | 65.80% | 1000 | 0:21:25 |
|neuralbeagle14-7b.Q5_K_M.gguf | 46.50% | 1000 | 0:16:13 |
|laserxtral-Q3_K_XS.gguf | 45.10% | 1000 | 0:36:00 |

 ## BasicMath
| Model | Accuracy | Iterations tested | Time elapsed |
|--|--|--|--|
|mistral-7b-instruct-v0.2.Q5_K_M.gguf | 52.20% | 1000 | 0:13:56 |
|neuralbeagle14-7b.Q5_K_M.gguf | 46.70% | 1000 | 0:14:51 |
|mixtral-8x7b-v0.1.Q3_K_M.gguf | 44.60% | 1000 | 0:54:32 |
|laserxtral-Q3_K_XS.gguf | 36.40% | 1000 | 0:27:50 |
|collectivecognition-v1.1-mistral-7b.Q5_K_M.gguf | 32.90% | 1000 | 0:14:15 |

 # Creddit
**Big thanks** to [llmperf](https://github.com/ray-project/llmperf) for sprouting the idea of the first benchmark "Correctness.py"
I most likely would of not had the idea for this project without llmperf!
