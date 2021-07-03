from pydub import AudioSegment
from pydub.playback import play


class PlaySound:
    """
    This class responsible for playing morse code to audio...
    """
    def __init__(self, text):
        self.text = text
        self.play()

    def play(self):
        print("Playing audio file...")
        for word in self.text:
            for char in word:
                try:
                    sound = AudioSegment.from_file(f"./sounds/{char}_morse_code.ogg.mp3")
                except FileNotFoundError:
                    print("Sorry, We can't play symbols code yet!")
                else:
                    play(sound)
