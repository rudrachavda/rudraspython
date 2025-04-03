import time
import os

def animate_text(text):
    for char in text:
        print(char, end='', flush = True)
        time.sleep(0.1)
    print()
    
if __name__ == '__main__':
    os.system('clear' if os.name == 'posix' else 'cls')
    word_to_animate = input("Enter a word:")
    animate_text(word_to_animate)

