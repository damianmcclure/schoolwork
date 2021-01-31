class hangman:
    def __init__(self, word):
        self.wordlength = len(word)
        self.fullword = []
        self.display = []
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        # Creates the dashes based on the word
        for i in range(self.wordlength):
            self.display.append("_")
            self.fullword.append(word[i])
    
    def play(self, letter):
        # Checks if the letter has been used before (or if the input isn't a letter)
        if letter in self.alphabet:
            self.alphabet.remove(letter)
            # Checks how many times the letter occurs
            if letter in self.fullword:
                count = self.fullword.count(letter)
                nt = 0
                # Replaces dashes with letters
                for ltr in self.fullword:
                    if letter == ltr:
                        self.display[nt] = letter
                    
                    nt = nt+1
                
                return self.display
            else:
                # Error message if it wasn't in the word
                return '"'+letter+'" was not in the word.'
        else:
            # Error message if you already used the letter or it wasnt a letter
            return 'you already used "'+letter+'" or your input wasn\'t a letter.'
            

# Just for testing the program.
test = hangman("research")

for i in range(100):
    guess = input("Guess a letter: ")
    print(test.play(guess))
