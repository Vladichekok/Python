def print_string(s):
    if not isinstance(s, str):
        print("Error: I need a row")
        return
    print(s)


def check_case(s):
    if not isinstance(s, str):
        print("Error: I need a row")
        return
    if s.isupper():
        print("All letters CAPS")
    elif s.islower():
        print("All letters small")
    else:
        print("Mixing letters")


def smogtether_upper():
    return [ch.upper() for ch in "smogtether"]
