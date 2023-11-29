import tkinter as tk
from tkinter import filedialog
import pygame

class AudioPlayerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Audio Player MP3")

        self.file_path = None

        pygame.mixer.init()

        self.create_widgets()

    def create_widgets(self):
        open_button = tk.Button(self.root, text="Pilih File", command=self.open_file_dialog, bg="pink", fg="white", font=("Arial", 12, "bold"))
        open_button.pack(pady=20)

        play_button = tk.Button(self.root, text="Play", command=self.play_sound, bg="pink", fg="white", font=("Arial", 12, "bold"))
        play_button.pack(pady=10)

        stop_button = tk.Button(self.root, text="Pause", command=self.stop_sound, bg="pink", fg="white", font=("Arial", 12, "bold"))
        stop_button.pack(pady=10)

    def open_file_dialog(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.mp3;*.wav")])
        if file_path:
            self.file_path = file_path

    def play_sound(self):
        if self.file_path:
            pygame.mixer.music.load(self.file_path)
            pygame.mixer.music.play()

    def stop_sound(self):
        pygame.mixer.music.stop()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = AudioPlayerApp()
    app.run()
