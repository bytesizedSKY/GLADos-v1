# brain.py

def detect_intent(text):
    text = text.lower()

    remember_words = [
        "remember", "my name is", "i am", "i'm",
        "i like", "i love", "my favourite", "my favorite",
        "i live", "i study", "i work", "call me"
    ]

    recall_words = [
        "who am i", "what do you know about me",
        "what is my name", "tell me about me"
    ]

    question_words = [
        "what", "why", "how", "when", "where", "explain"
    ]

    # detect memory creation
    for word in remember_words:
        if word in text:
            return "remember"

    # detect memory recall
    for word in recall_words:
        if word in text:
            return "recall"

    # detect question
    for word in question_words:
        if text.startswith(word):
            return "question"

    # default small talk
    return "chat"

def build_intent_instruction(intent):
    if intent == "remember":
        return """
INTENT: MEMORY CREATION

The user is telling you something about themselves.
Acknowledge naturally.
Do NOT say you are storing memory.
Respond normally and warmly.
"""

    elif intent == "recall":
        return """
INTENT: MEMORY RECALL

User is asking about themselves.
Answer using ONLY the USER PROFILE.
 prioritize USER PROFILE over conversation.
If info missing, say you don't know yet.
"""

    elif intent == "question":
        return """
INTENT: QUESTION ANSWERING

User is asking for knowledge or explanation.
Give clear, helpful, informative answers.
"""

    else:
        return """
INTENT: CASUAL CHAT

Normal friendly conversation.
"""