# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text, 1):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append((i, next))
            continue

        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0:
                return i

            top = opening_brackets_stack[-1][1]

            if next == ")" and top == "(":
                opening_brackets_stack.pop()
            elif next == "]" and top == "[":
                opening_brackets_stack.pop()
            elif next == "}" and top == "{":
                opening_brackets_stack.pop()
            else:
                return i

    if len(opening_brackets_stack) == 0:
        return "Success"

    else:
        return opening_brackets_stack[-1][0]


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
