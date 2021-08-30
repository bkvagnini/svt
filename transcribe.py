#import speech_recognition as sr
import speech_recognition as sr
from os import path
from pydub import AudioSegment

# convert mp3 file to wav  
# TODO: prompt for file name                                                     
sound = AudioSegment.from_mp3("ParkAccessOverview_with_Dave.mp3")
# TODO: prompt for file name   
sound.export("ParkAccessOverview_with_Dave.wav", format="wav")


# transcribe audio file                                                         
AUDIO_FILE = "ParkAccessOverview_with_Dave.wav"

# use the audio file as the audio source                                        
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file                  

        print("Transcription: " + r.recognize_google(audio))