#!/usr/bin/python3
"""
A function that prints texts, newline after ;.?
    checks text is type str
    Text: Some text
"""


def text_indentation(text):
    """A function that splits text
    Return: None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    new_text = ""
    last = "."

    for i in range(0, len(text)):

        if text[i] in [".", "?", ":"]:
            new_text += text[i]
            new_text += "\n" * 2
            last = text[i]

        elif text[i] == " " and last in [".", "?", ":"]:
            continue
        else:
            new_text += text[i]
            last = text[i]

    print(new_text, end="")
