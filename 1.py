from pydub import AudioSegment
from pydub.playback import play
 
song = AudioSegment.from_wav("lo.wav")
play(song)