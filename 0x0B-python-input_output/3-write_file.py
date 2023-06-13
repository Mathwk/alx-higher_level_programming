
#!/usr/bin/python3
"""
2-write_file.py
"""


def write_file(filename="", text=""):
    """ writes the text in a file"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
