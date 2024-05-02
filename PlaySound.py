# import required modules
from pydub import AudioSegment
from pydub.playback import play

# for playing wav file
song = AudioSegment.from_wav("/Users/fraserlowther/Desktop/Python Stuff/General Python/GitCloneTrial/train.wav")
print('playing sound using pydub')
play(song)
