from tkinter import filedialog
from pydub import AudioSegment
from pydub.playback import play
import tkinter as tk


root = tk.Tk()
root.title("Multimedia Application")
# Definisikan fungsi untuk memutar musik
def play_music():
    file_path = filedialog.askopenfilename()
    if file_path:
        audio = AudioSegment.from_file(file_path)
        play(audio)

# Membuat tombol untuk memutar musik
play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack()

root.mainloop()