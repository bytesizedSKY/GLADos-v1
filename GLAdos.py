import requests
from memory import *
from personality import *
from user_data import read_data, save_to_data_file
from brain import *

memory = load_memory()
system_perso = personality()
url = "http://localhost:11434/api/generate"

print(system_perso[1], "booting...")
print(system_perso[1], "v0 is online. Type 'exit' to quit.\n")


while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Have a nice day.")
        break

    intent=detect_intent(user_input)
    print("DEBUG Intent:", intent)
    profile = read_data()
    history = "\n".join(memory[-10:])
    intent_instruction = build_intent_instruction(intent)

 
    full_prompt = f"""
{system_perso[0]}

{intent_instruction}

### USER PROFILE (long-term facts)
{profile}

### RECENT CONVERSATION
{history}

User: {user_input}
Assistant:
"""

    data = {
        "model": "llama3",
        "prompt": full_prompt,
        "stream": False
    }

    response = requests.post(url, json=data)
    reply = response.json()["response"]

    print(system_perso[1] + ":", reply)


    add_to_memory(memory, "User: " + user_input)
    add_to_memory(memory, system_perso[1] + ": " + reply)
    save_memory(memory)

    memory_prompt = f"""
You maintain a long-term user profile.

CURRENT PROFILE:
{profile}

NEW CONVERSATION:
User: {user_input}
Assistant: {reply}

Update the profile if needed.

Rules:
- Keep under 20 lines
- Only store long-term facts and preferences
- Remove temporary info
- Merge duplicates
- Return the FULL updated profile
"""

    data2 = {
        "model": "llama3",
        "prompt": memory_prompt,
        "stream": False
    }

    if intent == "remember":
     
     print("Updating long-term memory...")
     response2 = requests.post(url, json=data2)
     new_profile = response2.json()["response"]
     save_to_data_file(new_profile)