import os
from groq import Groq


class AI:

    def __init__(self):
        self.client = Groq(
            api_key=os.environ.get("GROQ_API_KEY")
        )

        self.system_prompt = """
You are MyAI.
You are helpful, friendly, and explain things clearly.
"""


    def ask(self, prompt, memories=None):

        messages = [
            {
                "role": "system",
                "content": self.system_prompt
            }
        ]

        if memories:
            messages.append(
                {
                    "role": "system",
                    "content": "User memories:\n" + "\n".join(memories)
                }
            )

        messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        try:

            response = self.client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=messages
            )

            return response.choices[0].message.content

        except Exception as e:
            return f"AI Error: {e}"