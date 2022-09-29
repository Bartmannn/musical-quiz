# Made by Bartosz Bohdziewicz 2022 #
# OS: Linux Ubuntu 22 LTS #

from tkinter import *
from turtle import title
from music_manager import Music
from tkinter import messagebox

def show_title():
    global title_label
    title_label.config(text=music_manager.get_title())

def next_song():
    global current_song_range, title_label
    if music_manager.index_in_range():
        music_manager.next()
        title_label.config(text=". . . . .")
        current_song_range.config(text=f"{music_manager.index + 1}/{len(music_manager)}")
    else:
        messagebox.showinfo(title="Congratulations!", message=f"This is the end of Musical Quiz.\nI hope you had a lot of fun!")

def reset():
    global current_song_range, title_label
    music_manager.reset()
    title_label.config(text=". . . . .")
    current_song_range.config(text=f"1/{len(music_manager)}")

def main():

    global title_label
    global current_song_range

    window = Tk()
    window.title("Musical Quiz Game")
    window.config(padx=50, pady=50)


    #UI
    current_song_range = Label(text=f"{music_manager.index + 1}/{len(music_manager)}")
    current_song_range.grid(row=0, column=4)

    title_label = Label(text=". . . . .", width=50)
    title_label.grid(row=1, column=0, columnspan=3)

    show_title_button = Button(text="Show title", command=show_title)
    show_title_button.grid(row=1, column=3)

    play_button = Button(text="Play song", command=music_manager.play)
    play_button.grid(row=3, column=1)

    next_button = Button(text="Next song", command=next_song)
    next_button.grid(row=3, column=3)

    restart_button = Button(text="Restart game", command=reset)
    restart_button.grid(row=4, column=0)

    exit_button = Button(text="Exit", command=exit)
    exit_button.grid(row=4, column=4)

    window.mainloop()


if __name__ == "__main__":
    music_manager = Music()
    main()

