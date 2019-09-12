#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for o in dir(hidden_4):
        if "__" in o:
            continue
        else:
            print("{}".format(o))
