from tkinter import ttk
import tkinter as tk
import random

class Screen:
    def __init__(self):
        self.scr = tk.Tk()
        self.scr.resizable(False, False)
        self.scr.geometry("500x500")
        self.scr.title = "Quotes App"
        self.frame = ttk.Frame(self.scr, padding=10)
        self.frame.grid()
        self.quote_label = tk.Label(self.frame, text=get_quote(), wraplength=400, font="Arial 20")
        self.quote_label.grid(column=0, row=0)
        self.seconds_label = tk.Label(self.frame, text="Seconds Until Next Quote: 30", wraplength=400, font="Arial 20")
        self.seconds_label.grid(column=0, row=1)
        self.button = tk.Button(self.frame, text="Next", command=self.display_quote)
        self.button.grid(column=1, row=0)
        self.timer = ""
        self.recursive_timer()

    def start(self):
        self.scr.mainloop()

    def reset_timer(self):
        self.scr.after_cancel(self.timer)
        self.timer = self.scr.after(1000, self.recursive_timer)


    def recursive_timer(self, ms=30000):  # im retarded
        self.timer = self.scr.after(25, lambda:self.recursive_timer(ms-25))
        self.seconds_label.config(text=f"Second Until Next Quote: {ms//1000}")
        if ms <= 0:
            self.reset_timer()
            self.display_quote()

    def display_quote(self):
        quotes = get_quotes()
        self.seconds_label.config(text="Second Until Next Quote: 30")
        if quotes:
            self.reset_timer()
            index = random.randint(0, len(quotes) - 1)
            quote = quotes[index]
            self.quote_label.config(text=quote)
        else:
            print("No Quotes to Display")

def get_quotes():
    with open("quotes.txt", "r") as file:
        return file.readlines()

def get_quote():
    quotes = get_quotes()
    if quotes:
        index = random.randint(0, len(quotes) - 1)
        quote = quotes[index]
        return quote
    else:
        return "Error: No Quotes to Display"

if __name__ == "__main__":
    screen = Screen()
    screen.start()