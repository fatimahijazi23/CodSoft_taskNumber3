import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")  #title of the root window
        self.root.configure(bg='white')  
        
        defaultFont = ('Arial', 30)
        
        self.frame = tk.Frame(root, bg='white')  
        self.frame.pack(pady=110)
        
        self.label = tk.Label(self.frame, text="Enter password length:", font=defaultFont, bg='white') 
        self.label.grid(row=0, column=0)
        
        self.lengthEntry = tk.Entry(self.frame, font=defaultFont)  
        self.lengthEntry.grid(row=0, column=1)
        
        self.generateButton = tk.Button(self.frame, text="Generate!", command=self.generatePassword, bg='pink', font=defaultFont + ('bold',))  
        self.generateButton.grid(row=1, columnspan=2, pady=10)  
        
        self.passwordLabel = tk.Label(root, text="", font=defaultFont, bg='white')  
        self.passwordLabel.pack(pady=20)
        
    def generatePassword(self):
        try:
            length = int(self.lengthEntry.get()) 
            if length < 1:
                raise ValueError("Sorry, the length must be at least 1.")
            password = self.generateRandomPassword(length)  
            self.passwordLabel.config(text=f"Generated Password: {password}")  
        except ValueError as e:
            messagebox.showwarning("Input Error", str(e))
    
    def generateRandomPassword(self, length):  
        characters = string.ascii_letters + string.digits + string.punctuation  
        password = ''.join(random.choice(characters) for _ in range(length))  #Generate a random password of the specified length
        return password

if __name__ == "__main__":
    root = tk.Tk() 
    app = PasswordGenerator(root)  
    root.mainloop()
