from exceptions import file_exception
import sys


def clean(file: str) -> None:
    """
    :param file: file with some text
    :return: None
    create new file "cleaned_text.txt" in root directory with cleaned text, without punctuation marks
    and in low register; each word on the new line
    If file does not exist, print your own text
    """
    try:
        with open(file) as file:
            text = file.readlines()
    except FileNotFoundError:
        file_exception()
        text = sys.stdin.read()

    with open("cleaned_text.txt", 'w') as cleaned_text:
        for line in text:
            if line.isspace():
                continue
            cleared_line = line.lower()
            table = line.maketrans(',.?:;!"()[]', "           ")
            cleared_line = cleared_line.translate(table)
            cleared_line = cleared_line.split()
            cleared_line = "\n".join(cleared_line)
            cleaned_text.write(cleared_line + "\n")
