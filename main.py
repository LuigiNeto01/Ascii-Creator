import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger()

ascii_alphabet = {
    '-': [
        "        ",
        "        ",
        "███████╗",
        "╚══════╝",
        "        ",
        "        "
    ],
    'A': [
        " █████╗ ",
        "██╔══██╗",
        "███████║",
        "██╔══██║",
        "██║  ██║",
        "╚═╝  ╚═╝"
    ],
    'B': [
        "██████╗ ",
        "██╔══██╗",
        "██████╔╝",
        "██╔══██╗",
        "██████╔╝",
        "╚═════╝ "
    ],
    'C': [
        " ██████╗ ",
        "██╔════╝ ",
        "██║      ",
        "██║      ",
        "╚██████╗ ",
        " ╚═════╝ "
    ],
    'D': [
        "██████╗  ",
        "██╔══██╗ ",
        "██║  ██║ ",
        "██║  ██║ ",
        "██████╔╝ ",
        "╚═════╝  "
    ],
    'E': [
        "███████╗",
        "██╔════╝",
        "█████╗  ",
        "██╔══╝  ",
        "███████╗",
        "╚══════╝"
    ],
    'F': [
        "███████╗",
        "██╔════╝",
        "█████╗  ",
        "██╔══╝  ",
        "██║     ",
        "╚═╝     "
    ],
    'G': [
        " ██████╗ ",
        "██╔════╝ ",
        "██║  ███╗",
        "██║   ██║",
        "╚██████╔╝",
        " ╚═════╝ "
    ],
    'H': [
        "██╗  ██╗",
        "██║  ██║",
        "███████║",
        "██╔══██║",
        "██║  ██║",
        "╚═╝  ╚═╝"
    ],
    'I': [
        "██╗",
        "██║",
        "██║",
        "██║",
        "██║",
        "╚═╝"
    ],
    'J': [
        "     ██╗",
        "     ██║",
        "     ██║",
        "██   ██║",
        "╚█████╔╝",
        " ╚════╝ "
    ],
    'K': [
        "██╗  ██╗",
        "██║ ██╔╝",
        "█████╔╝ ",
        "██╔═██╗ ",
        "██║  ██╗",
        "╚═╝  ╚═╝"
    ],
    'L': [
        "██╗     ",
        "██║     ",
        "██║     ",
        "██║     ",
        "███████╗",
        "╚══════╝"
    ],
    'M': [
        "███╗   ███╗",
        "████╗ ████║",
        "██╔████╔██║",
        "██║╚██╔╝██║",
        "██║ ╚═╝ ██║",
        "╚═╝     ╚═╝"
    ],
    'N': [
        "███╗   ██╗",
        "████╗  ██║",
        "██╔██╗ ██║",
        "██║╚██╗██║",
        "██║ ╚████║",
        "╚═╝  ╚═══╝"
    ],
    'O': [
        " ██████╗ ",
        "██╔═══██╗",
        "██║   ██║",
        "██║   ██║",
        "╚██████╔╝",
        " ╚═════╝ "
    ],
    'P': [
        "██████╗ ",
        "██╔══██╗",
        "██████╔╝",
        "██╔═══╝ ",
        "██║     ",
        "╚═╝     "
    ],
    'Q': [
        " ██████╗ ",
        "██╔═══██╗",
        "██║   ██║",
        "██║▄▄ ██║",
        "╚██████╔╝",
        " ╚══▀▀═╝ "
    ],
    'R': [
        "██████╗ ",
        "██╔══██╗",
        "██████╔╝",
        "██╔══██╗",
        "██║  ██║",
        "╚═╝  ╚═╝"
    ],
    'S': [
        "███████╗",
        "██╔════╝",
        "█████╗  ",
        "╚════██╗",
        "███████║",
        "╚══════╝"
    ],
    'T': [
        "████████╗",
        "╚══██╔══╝",
        "   ██║   ",
        "   ██║   ",
        "   ██║   ",
        "   ╚═╝   "
    ],
    'U': [
        "██╗   ██╗",
        "██║   ██║",
        "██║   ██║",
        "██║   ██║",
        "╚██████╔╝",
        " ╚═════╝ "
    ],
    'V': [
        "██╗   ██╗",
        "██║   ██║",
        "██║   ██║",
        "╚██╗ ██╔╝",
        " ╚████╔╝ ",
        "  ╚═══╝  "
    ],
    'W': [
        "██╗    ██╗",
        "██║    ██║",
        "██║ █╗ ██║",
        "██║███╗██║",
        "╚███╔███╔╝",
        " ╚══╝╚══╝ "
    ],
    'X': [
        "██╗  ██╗",
        "╚██╗██╔╝",
        " ╚███╔╝ ",
        " ██╔██╗ ",
        "██╔╝ ██╗",
        "╚═╝  ╚═╝"
    ],
    'Y': [
        "██╗   ██╗",
        "╚██╗ ██╔╝",
        " ╚████╔╝ ",
        "  ╚██╔╝  ",
        "   ██║   ",
        "   ╚═╝   "
    ],
    'Z': [
        "███████╗",
        "╚══███╔╝",
        "  ███╔╝ ",
        " ███╔╝  ",
        "███████╗",
        "╚══════╝"
    ]
}

def convert_word_to_ascii(word, letters):
    """
    Converts a word to its ASCII Art representation, combining each line of the letters.
    :param word: Word to be converted.
    :param letters: Dictionary of ASCII Art letters to use for conversion.
    :return: ASCII Art representation of the word.
    """
    word_lines = ["" for _ in range(6)]  
    for letter in word.upper():
        if letter in letters:
            letter_ascii = letters[letter]
            for i in range(6):
                word_lines[i] += letter_ascii[i] + ""
        else:
            for i in range(6):
                word_lines[i] += " " * 4  # Size for unknown character / space
    return "\n".join(word_lines)

if __name__ == "__main__":
    user_word = input("Enter a word to convert to ASCII Art: ").strip()
    word_ascii_art = convert_word_to_ascii(user_word, ascii_alphabet)

    logger.info(f'\n{word_ascii_art}')
