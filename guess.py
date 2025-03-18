from breezypythongui import EasyFrame
import random

class GuessingGame(EasyFrame):
    def __init__(self):
        super().__init__(title="Guessing Game")
        self.setSize(350, 200)
        self.setResizable(False)
        
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        
        self.addLabel("Guess a number between 1 and 100:", row=0, column=0, columnspan=2, sticky="NSEW")
        self.inputField = self.addIntegerField(value=0, row=1, column=0, sticky="EW")
        self.addButton("Guess", row=1, column=1, command=self.check_guess)
        self.resultLabel = self.addLabel("", row=2, column=0, columnspan=2, sticky="NSEW")
    
    def check_guess(self):
        self.attempts += 1
        guess = self.inputField.getNumber()
        
        if guess < self.target_number:
            message = "Try Higher!"
        elif guess > self.target_number:
            message = "Try Lower!"
        else:
            message = f"Congratulations! You guessed it in {self.attempts} tries!"
            self.target_number = random.randint(1, 100)
            self.attempts = 0
        
        self.resultLabel['text'] = message

if __name__ == "__main__":
    GuessingGame().mainloop()
