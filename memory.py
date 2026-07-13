import json
import os

MEMORY_FILE = "memory.json"


class Memory:

    def __init__(self):
        self.memories = []
        self.load()

    def load(self):
        if os.path.exists(MEMORY_FILE):
            try:
                with open(MEMORY_FILE, "r", encoding="utf-8") as file:
                    self.memories = json.load(file)
            except:
                self.memories = []
        else:
            self.memories = []

    def save(self):
        with open(MEMORY_FILE, "w", encoding="utf-8") as file:
            json.dump(self.memories, file, indent=4)

    def remember(self, text):
        self.memories.append(text)
        self.save()

    def list(self):
        return self.memories

    def forget(self, text):
        self.memories = [
            item for item in self.memories
            if item.lower() != text.lower()
        ]
        self.save()

    def clear(self):
        self.memories = []
        self.save()