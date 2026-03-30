# MORSE sözlüğünün tersini oluştur
from morse.mapping import MORSE


MORSE_REVERSE = {v: k for k, v in MORSE.items()}

def decode_word(word):
    letters = word.split()
    decoded_letters = [MORSE_REVERSE[letter] for letter in letters if letter in MORSE_REVERSE]
    return "".join(decoded_letters)

def decode(text):
    words = text.split("|")
    decoded_words = [decode_word(w) for w in words]
    return " ".join(decoded_words)


if __name__ == "__main__":
    # Example usage for one word
    EXAMPLE_TEXT= ".- -... -.-."
    decoded = decode_word(EXAMPLE_TEXT)
    print(decoded)


    # Example usage for one sentence
    EXAMPLE_TEXT = ".- -... -.-. | .- -... -.-."
    decoded = decode(EXAMPLE_TEXT)
    print(decoded)
