import random

# -------------------------------
# Word Knowledge Base (AI Memory)
# -------------------------------
WORDS = {
    "easy": [
        "cat", "dog", "apple", "ball", "book", "pen", "fish", "milk"
    ],
    "medium": [
        "python", "hangman", "computer", "network", "programming", "keyboard"
    ],
    "hard": [
        "artificial", "intelligence", "algorithm", "neural", "optimization"
    ]
}

# Letter frequency (used by AI hint system)
LETTER_FREQUENCY = "etaoinshrdlcumwfgypbvkjxqz"


# -------------------------------
# Hangman Drawing
# -------------------------------
HANGMAN_PICS = [
    """
     ------
     |    |
          |
          |
          |
          |
    --------
    """,
    """
     ------
     |    |
     O    |
          |
          |
          |
    --------
    """,
    """
     ------
     |    |
     O    |
     |    |
          |
          |
    --------
    """,
    """
     ------
     |    |
     O    |
    /|    |
          |
          |
    --------
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
          |
          |
    --------
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
    /     |
          |
    --------
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
    / \\   |
          |
    --------
    """
]


# -------------------------------
# AI Helper Functions
# -------------------------------
def choose_word(difficulty):
    """AI selects a word based on difficulty"""
    return random.choice(WORDS[difficulty])


def ai_hint(word, guessed_letters):
    """
    AI gives a smart hint based on letter frequency
    """
    for letter in LETTER_FREQUENCY:
        if letter in word and letter not in guessed_letters:
            return letter
    return None


# -------------------------------
# Main Game Logic
# -------------------------------
def play_hangman():
    print("🎮 Welcome to AI-Based Hangman Game 🎮\n")

    # Difficulty selection
    while True:
        difficulty = input("Choose difficulty (easy / medium / hard): ").lower()
        if difficulty in WORDS:
            break
        print("❌ Invalid choice. Try again.")

    word = choose_word(difficulty)
    guessed_letters = set()
    wrong_attempts = 0
    max_attempts = len(HANGMAN_PICS) - 1

    print("\nGame Started! Guess the word.\n")

    while wrong_attempts < max_attempts:
        print(HANGMAN_PICS[wrong_attempts])

        # Display word progress
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("Word:", display_word.strip())
        print("Guessed letters:", " ".join(sorted(guessed_letters)))

        # Win condition
        if all(letter in guessed_letters for letter in word):
            print("\n🎉 Congratulations! You guessed the word:", word)
            return

        choice = input("\nEnter a letter or type 'hint': ").lower()

        # AI Hint
        if choice == "hint":
            hint_letter = ai_hint(word, guessed_letters)
            if hint_letter:
                print("🤖 AI Hint: Try the letter ->", hint_letter)
            else:
                print("🤖 AI: No hints available.")
            continue

        # Input validation
        if len(choice) != 1 or not choice.isalpha():
            print("❌ Please enter a single valid letter.")
            continue

        if choice in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.add(choice)

        if choice not in word:
            wrong_attempts += 1
            print("❌ Wrong guess!")

    # Game Over
    print(HANGMAN_PICS[wrong_attempts])
    print("\n💀 Game Over!")
    print("The correct word was:", word)


# -------------------------------
# Run the Game
# -------------------------------
if __name__ == "__main__":
    play_hangman()