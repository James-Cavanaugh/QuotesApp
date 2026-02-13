# Basic Quotes App

This project is something I decided to make during my a boring Physics Class.

## Features
- Display Quotes from a .txt file
- Change the displayed quote every 30 seconds
- Also Change the quote upon a button press
- Timer that shows when the quote will update with accurate time

## Interesting Code
```python
def recursive_timer(self, ms=30000):  # why must i do this to myself
    self.timer = self.scr.after(25, lambda:self.recursive_timer(ms-25))
    self.seconds_label.config(text=f"Second Until Next Quote: {ms//1000}")
    if ms <= 0:
        self.reset_timer()
        self.display_quote()
```

### App GUI
<img width="498" height="245" alt="Screenshot 2026-02-13 at 1 11 21 PM" src="https://github.com/user-attachments/assets/bb2c0e07-da11-461f-91a7-0bc7a3c12de6" />

### Why I made this
IDK, mainly because I wanted to learn some of the **cool** features that are in a README file.

### Side Note
I spent 20 minutes trying to push this repo just to find out that my SSH key randomly got disabled on my mac, idk how or why it happened but it did.
