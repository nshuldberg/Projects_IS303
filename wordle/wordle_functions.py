def choose_word():
    import random
    words = ["apple", "grape", "peach", "lemon", "mango",
        "berry", "melon", "guava", "plums", "olive",
        "beach", "ocean", "shore", "waves", "coral",
        "storm", "cloud", "rainy", "sunny", "windy",
        "tiger", "zebra", "horse", "sheep", "mouse",
        "eagle", "shark", "whale", "panda", "koala",
        "bread", "toast", "pasta", "steak", "bacon",
        "cream", "honey", "sugar", "spice", "smack"
        "chair", "table", "couch", "shelf", "bench",
        "clock", "phone", "radio", "light", "cable",
        "plant", "grass", "trees", "bloom", "flame",
        "stone", "brick", "metal", "steel", "glass",
        "happy", "smile", "laugh", "enjoy", "proud",
        "brave", "calm", "trust", "peace", "dream",
        "quick", "swift", "brisk", "rapid", "speed",
        "write", "learn", "teach", "study", "think",
        "build", "paint", "craft", "shape", "draws",
        "music", "piano", "flute", "drums", "sound",
        "heart", "brain", "blood", "nerve", "bones",
        "world", "earth", "space", "orbit", "stars"]
    word = random.choice(words)
    return word

def get_guess(guess):
    guess = ""
    while len(guess) != 5:
        guess = input("Guess a five-letter word: ").lower()
        if len(guess) == 5:
            break
        print("Invalid word length. Please try again.")
    return guess

def evaluate_guess(guess, word):
    feedback = []
    for i in range(len(guess)):
        if guess[i] == word[i]:
            feedback.append("G")
        elif guess[i] in word:
            feedback.append("Y")
        elif guess[i] not in word:
            feedback.append("-")
    return "|".join(feedback)

def display_guess(guess, feedback):
    print(f"Your guess: {guess}")
    print(f"\n{feedback}")

def has_won(guess, word):
    if guess == word:
        return True
    elif guess != word:
        return False

