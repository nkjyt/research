import openai
from gpt3api import Gpt3API


inp = "have a I cat."
gpt3 = Gpt3API(inp)

print(gpt3.word2sentence())

