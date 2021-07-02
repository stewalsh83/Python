
d_morse = {
   'a': '.-', 'A': '.-',
   'b': '-...', 'B': '-...',
   'c': '-.-.', 'C': '-.-.',
   'd': '-..', 'D': '-..',
   'e': '.', 'E': '.',
   'f': '..-.', 'F': '..-.',
   'g': '--.', 'G': '--.',
   'h': '....', 'H': '....',
   'i': '..', 'I': '..',
   'j': '.---', 'J': '.---',
   'k': '-.-', 'K': '-.-',
   'l': '.-..', 'L': '.-..',
   'm': '--', 'M': '--',
   'n': '-.', 'N': '-.',
   'o': '---', 'O': '---',
   'p': '.--.', 'P': '.--.',
   'q': '--.-', 'Q': '--.-',
   'r': '.-.', 'R': '.-.',
   's': '...', 'S': '...',
   't': '-', 'T': '-',
   'u': '..-', 'U': '..-',
   'v': '...-', 'V': '...-',
   'w': '.--', 'W': '.--',
   'x': '-..-', 'X': '-..-',
   'y': '-.--', 'Y': '-.--',
   'z': '--..', 'Z': '--..'
}

words = input('Enter Word: ')

def main():
    a = []
    i = 0
    while i < len(words):
        word = words[i].strip()
        if word in d_morse:
            ls = '{}  '.format(d_morse[word])
            a.append(ls)
            word = '"{}" converted to morse code is:\n{}'.format(words, ''.join(a))
        else:
            word = "Invalid input!"
        i += 1
    print(word)

print('\n')

if __name__ == "__main__":
    main()