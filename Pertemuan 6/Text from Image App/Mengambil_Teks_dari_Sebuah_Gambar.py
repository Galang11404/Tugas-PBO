import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import pytesseract

class TextFromImageApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Text from Image App")

        self.image_path = None

        self.create_widgets()

    def create_widgets(self):
        open_button = tk.Button(self.root, text="Open Image", command=self.open_image_dialog)
        open_button.pack(pady=10)

        extract_button = tk.Button(self.root, text="Extract Text", command=self.extract_text)
        extract_button.pack(pady=5)

        self.text_display = tk.Text(self.root, height=10, width=50)
        self.text_display.pack(pady=10)

    def open_image_dialog(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
        if file_path:
            self.image_path = file_path
            self.display_image(file_path)

    def extract_text(self):
        if self.image_path:
            image = Image.open(self.image_path)
            text = pytesseract.image_to_string(image)
            self.text_display.delete(1.0, tk.END)  # Clear previous text
            self.text_display.insert(tk.END, text)

    def display_image(self, image_path):
        img = Image.open(image_path)
        img.thumbnail((300, 300))
        photo = ImageTk.PhotoImage(img)
        label = tk.Label(self.root, image=photo)
        label.image = photo
        label.pack()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = TextFromImageApp()
    app.run()
