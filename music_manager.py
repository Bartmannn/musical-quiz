from pydub import AudioSegment
from os import scandir

MUSIC_PATH:str = r"./music"
DURATION:int = 5000 #in milisecionds


class Music:

    def __init__(self) -> None:
        self.index = 0
        self.titles:list = [path.name for path in scandir(MUSIC_PATH) if path.is_file()]
        self.randomize_titles()
        self.next_song()

    def randomize_titles(self) -> None:
        from random import shuffle
        shuffle(self.titles)

    def play(self) -> None:
        from pydub.playback import play
        play(self.extract_song_piece(DURATION))

    def extract_song_piece(self, miliseconds:int) -> AudioSegment:
        end_time = self.start_time + miliseconds
        extract = self.song[self.start_time: end_time]
        self.start_time = end_time
        return extract

    def next_index(self) -> None:
        self.index += 1

    def next_song(self) -> None:
        from random import randint
        self.song = AudioSegment.from_mp3(f"{MUSIC_PATH}/{self.titles[self.index]}")
        self.song_length = round(self.song.duration_seconds)
        self.start_time = randint(0, self.song_length - 30) * 1000

    def next(self):
        self.next_index()
        self.next_song()

    def get_title(self) -> str:
        return f"{self.titles[self.index]}"

    def index_in_range(self) -> bool:
        if self.index + 1 >= len(self.titles):
            return False
        return True

    def reset(self):
        self.randomize_titles()
        self.index = 0
        self.next_song()

    def __len__(self):
        return len(self.titles)
    
