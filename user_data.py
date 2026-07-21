# user_data.py

FILE = "user.txt"

def read_data():
    try:
        with open(FILE, "r") as f:
            return f.read()
    except:
        return "No stored user profile yet."

def save_to_data_file(text):
    try:
        with open(FILE, "r") as f:
            old = f.read()
    except:
        old = ""

    # backup old profile
    with open("user_backup.txt", "w") as f:
        f.write(old)

    # save new profile
    with open(FILE, "w") as f:
        f.write(text)