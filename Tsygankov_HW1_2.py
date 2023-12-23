import re
from collections import deque

def is_palindrome(input_string):
 
    s = re.sub(r'[^a-zA-Z]', '', input_string).lower()
    
    char_queue = deque(s)
    
    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False
    
    return True

if __name__ == "__main__":
    input_text = input("Введіть текст для перевірки на паліндром: ")

    if is_palindrome(input_text) or (len(input_text) % 2 == 1 and is_palindrome(input_text[:-1])):
        print("Це паліндром.")
    else:
        print("Це не паліндром.")