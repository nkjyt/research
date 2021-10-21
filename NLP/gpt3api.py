"""
GPT-3のAPIを用いて単語を並べ替えさせるスクリプト
"""

import os
import openai

class Gpt3API():
    def __init__(self, i_text) -> None:
        self.i_text = i_text
        pass

    def word2sentence(self):
        openai.api_key = "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"
        response = openai.Completion.create(
        engine="davinci",
        prompt="Rearrange the words to make a sentence.\n\nInput: upon a time once.\nOutput: Once upon a time.\n\nInput: influx an aliens the peace disrupted of.\nOutput: An influx of aliens disrupted the peace.\n\nInput: you if maintain to your dominance want.\nOutput: If you to maintain to your dominance.\n\nInput: I do what should?\nOutput: What should I do ?\n\nInput: " + self.i_text + "\nOutput:",
        temperature=0.7,
        max_tokens=64,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=[".", "?"]
        )
        return response["choices"][0]["text"]
    
    def fillInTheBlank(self, text):
        openai.api_key = "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"
        response = openai.Completion.create(
        engine="davinci",
        prompt="Fill in the blanks. input: I am going to the [blank]. output: I am going to the church. input: I ate a [blank]. output: I ate a taco. input: I live in [blank]. output: I live in California. input: " + text + " output:",
        temperature=0.7,
        max_tokens=64,
        top_p=1,
        frequency_penalty=0.2,
        presence_penalty=0,
        stop=["input:"]
        )
        return response["choices"][0]["text"]
