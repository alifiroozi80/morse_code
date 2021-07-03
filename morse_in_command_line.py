from letters_and_symbols import morse_char
from sounds import PlaySound


class MorseCode:
    """
    With this module you can encode and decode your text inside the terminal...
    """
    def __init__(self):
        self.morse = []
        self.key_list = list(morse_char.keys())
        self.val_list = list(morse_char.values())

    def encode(self):
        text = input("Enter Your Text: ").upper().split(" ")
        for word in text:
            for char in word:
                try:
                    index = self.key_list.index(char)
                except ValueError:
                    print(f"Error in input. Cannot translate the {char} character!")
                else:
                    self.morse.append(self.val_list[index])
            self.morse.append("/")
        print(" ".join(self.morse))
        sounds = input("Play Audio? [y/n]: ").lower()
        if sounds == "y":
            PlaySound(text)

    def decode(self):
        inp = input("Enter Your Morse Code: ")
        text = inp.split("/")
        for word in text:
            x = word.split(" ")
            while "" in x:
                x.remove("")
            for char in x:
                try:
                    index = self.val_list.index(char)
                except ValueError:
                    print("This is not valid Morse code!")
                else:
                    self.morse.append(self.key_list[index])
            self.morse.append(" ")
        print("".join(self.morse))
