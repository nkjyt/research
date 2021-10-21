import openai
from gpt3api import Gpt3API

"""
input: any sentences contain [blank].
output: complete sentences filled in the [blank].
"""

inp = "Aren't quiet people with glasses usually [blank]?"
gpt3 = Gpt3API(inp)

print(gpt3.fillInTheBlank(inp))
