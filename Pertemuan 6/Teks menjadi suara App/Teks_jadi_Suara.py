import tkinter as tk
from tkinter import ttk
import pyttsx3

class TextToSpeechApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Teks menjadi suara App")

        self.text_entry = tk.Entry(self.root, width=50)
        self.text_entry.pack(pady=10)

        speak_button = tk.Button(self.root, text="Bicara", command=self.speak_text)
        speak_button.pack(pady=5)

        self.engine = pyttsx3.init()

    def speak_text(self):
        text_to_speak = self.text_entry.get()
        self.engine.say(text_to_speak)
        self.engine.runAndWait()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = TextToSpeechApp()
    app.run()
