def get_guess(guess):
    guess = ""
    while len(guess) != 5:
        guess = input("Guess a five-letter word: ")
        if len(guess) == 5:
            break
        print("Invalid Guess. Please try again.")
    return guess

def choose_word(cmptr):
    import random
    words = ["apple", "grape", "zesty", "brave", "crane", "flint", "spear", "track",
    "blaze", "charm", "dwarf", "eagle", "frost", "glide", "honey", "ivory",
    "jolly", "knack", "lemon", "mango", "naval", "ocean", "piano", "quilt",
    "raven", "solar", "tango", "umbra", "vigor", "whale", "xenon", "youth",
    "zonal", "bloom", "cider", "dodge", "ember", "fable", "giant", "harsh",
    "ideal", "jumpy", "karma", "latch", "mirth", "noble", "olive", "prism",
    "quark", "risky", "siren", "tulip", "unity", "vivid", "waltz", "xylem",
    "yacht", "zesty"]
    cmptr = random.choice(words)
    return cmptr

def evaluate_guess(guess, word):
    feedback = []
    for i in range(len(guess)):
        if guess[i] == word[i]:
            feedback.append("G")
        elif guess[i] in word:
            feedback.append("Y")
        elif guess[i] not in word:
            feedback.append("-")
        return " ".join(feedback)





    