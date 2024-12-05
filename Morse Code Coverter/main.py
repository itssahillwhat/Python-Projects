morse_code_dict = {
    # Latin Alphabet
    'a': '.-',    'b': '-...',  'c': '-.-.',  'd': '-..',   'e': '.',
    'f': '..-.',  'g': '--.',   'h': '....',  'i': '..',    'j': '.---',
    'k': '-.-',   'l': '.-..',  'm': '--',    'n': '-.',    'o': '---',
    'p': '.--.',  'q': '--.-',  'r': '.-.',   's': '...',   't': '-',
    'u': '..-',   'v': '...-',  'w': '.--',   'x': '-..-',  'y': '-.--',
    'z': '--..',

    # Digits
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',

    # Common Punctuation
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '@': '.--.-.', ' ': '/',

    # Special Characters
    '¡': '..-.-', '¿': '..-..-', '§': '...-..-', '©': '-.-.-.', '®': '.-.-.',

    # International Morse Code (used in various languages)
    'Æ': '.-.-.', 'Ø': '---.', 'Å': '.--.-', 'Ç': '-.-..', 'Ñ': '--.--',
    'Þ': '-.--.', 'Ğ': '--.-.', 'İ': '..-', 'Š': '----', 'Ž': '--..--'
}


def morse(text):
    text_list = []
    for letter in text:
        text_list.append(morse_code_dict[letter])

    return ' '.join(text_list)



while True:
    try:
        text = input("Type your message:\n").upper()
        result = morse(text)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
    ans = input("Type 'yes' if you want to go again. Otherwise type 'no'. ")
    if ans.lower() != "yes":
        print("Goodbye!")
        break