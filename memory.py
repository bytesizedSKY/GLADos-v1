MEMORY_FILE = "memory.txt"


def load_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            memory = f.read().splitlines()
            return memory
    except:
        return []


def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        for line in memory:
            f.write(line + "\n")


def add_to_memory(memory, text):
    memory.append(text)
    save_memory(memory)