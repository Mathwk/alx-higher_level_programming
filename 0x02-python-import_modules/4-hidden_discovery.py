#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    s = dir(hidden_4)
    for a in s:
        if a[:2] != "__":
            print(a)
