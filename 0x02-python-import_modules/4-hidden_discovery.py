#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 module"""
    import hidden_4

    label = dir(hidden_4)
    for label in label:
        if label[:2] != "__":
            print(label)
