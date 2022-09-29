from music_manager import Music
from tkinter import *
from tkinter import messagebox



class Game():

    def __init__(self) -> None:
        self.music_manager = Music()
        self.window = Tk()
        self.window.title("Musical Quiz Game")
        self.window.config(padx=50, pady=50)
        self.current_song_range = Label(text=f"{self.music_manager.index + 1}/{len(self.music_manager)}")
        self.title_label = Label(text=". . . . .", width=50)
        self.show_title_button = Button(text="Show title", command=self.show_title)
        self.play_button = Button(text="Play song", command=self.music_manager.play)
        self.next_button = Button(text="Next song", command=self.next_song)
        self.restart_button = Button(text="Restart game", command=self.reset)
        self.exit_button = Button(text="Exit", command=exit)

        self.set_UI()

        self.window.mainloop()

    def set_UI(self):
        self.current_song_range.grid(row=0, column=4)
        self.title_label.grid(row=1, column=0, columnspan=3)
        self.show_title_button.grid(row=1, column=3)
        self.play_button.grid(row=3, column=1)
        self.next_button.grid(row=3, column=3)
        self.restart_button.grid(row=4, column=0)
        self.exit_button.grid(row=4, column=4)

    def show_title(self):
        self.title_label.config(text=self.music_manager.get_title())

    def next_song(self):
        if self.music_manager.index_in_range():
            self.music_manager.next()
            self.title_label.config(text=". . . . .")
            self.current_song_range.config(text=f"{self.music_manager.index + 1}/{len(self.music_manager)}")
        else:
            messagebox.showinfo(title="Congratulations!", message=f"This is the end of Musical Quiz.\nI hope you had a lot of fun!")

    def reset(self):
        self.music_manager.reset()
        self.title_label.config(text=". . . . .")
        self.current_song_range.config(text=f"1/{len(self.music_manager)}")


