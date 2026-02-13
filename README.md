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
gonna have to implement this outside of my code editor :(

### Why I made this
IDK, mainly because I wanted to learn some of the **cool** features that are in a README file.