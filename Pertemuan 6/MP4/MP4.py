import tkinter as tk
from tkinter import ttk, filedialog
import vlc

class VideoPlayerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mp4 Video Player")

        self.Instance = vlc.Instance()
        self.player = self.Instance.media_player_new()

        self.create_widgets()

    def create_widgets(self):
        open_button = tk.Button(self.root, text="Open Video", command=self.open_video_dialog)
        open_button.pack(pady=10)

        play_button = tk.Button(self.root, text="Play", command=self.play_video)
        play_button.pack(side=tk.LEFT, padx=5)

        pause_button = tk.Button(self.root, text="Pause", command=self.pause_video)
        pause_button.pack(side=tk.LEFT, padx=5)

        stop_button = tk.Button(self.root, text="Close", command=self.stop_video)
        stop_button.pack(side=tk.LEFT, padx=5)

    def open_video_dialog(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4")])
        if file_path:
            media = self.Instance.media_new(file_path)
            self.player.set_media(media)

    def play_video(self):
        if self.player.get_media():
            self.player.play()

    def pause_video(self):
        self.player.pause()

    def stop_video(self):
        self.player.stop()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = VideoPlayerApp()
    app.run()
