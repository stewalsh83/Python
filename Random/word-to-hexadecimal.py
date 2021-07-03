
d_hex = {
   'a': '61', 'A': '41',
   'b': '62', 'B': '42',
   'c': '63', 'C': '43',
   'd': '64', 'D': '44',
   'e': '65', 'E': '45',
   'f': '66', 'F': '46',
   'g': '67', 'G': '47',
   'h': '68', 'H': '48',
   'i': '69', 'I': '49',
   'j': '6A', 'J': '4A',
   'k': '6B', 'K': '4B',
   'l': '6C', 'L': '4C',
   'm': '6D', 'M': '4D',
   'n': '6E', 'N': '4E',
   'o': '6F', 'O': '4F',
   'p': '70', 'P': '50',
   'q': '71', 'Q': '51',
   'r': '72', 'R': '52',
   's': '73', 'S': '53',
   't': '74', 'T': '54',
   'u': '75', 'U': '55',
   'v': '76', 'V': '56',
   'w': '77', 'W': '57',
   'x': '78', 'X': '58',
   'y': '79', 'Y': '59',
   'z': '7A', 'Z': '5A'
}

def main():
    words = input('Enter Word: ')
    a = []
    i = 0
    while i < len(words):
        word = words[i].strip()
        if word in d_hex:
            ls = '{}  '.format(d_hex[word])
            a.append(ls)
            word = '"{}" converted to hexadecimal is:\n{}'.format(words, ''.join(a))
        else:
            word = "Invalid input!"
        i += 1
    print(word)

print('\n')

if __name__ == "__main__":
    main()