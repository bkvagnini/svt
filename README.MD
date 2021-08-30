This is for searching for a specific phrase inside of a meeting video.
There are several distinct steps to this process

Process:
1-Split video file into audio and video - use split_movie.py (via https://towardsdatascience.com/extracting-audio-from-video-using-python-58856a940fd tutorial)
2-Run audio file through speech transcription https://github.com/Uberi/speech_recognition/blob/master/examples/audio_transcribe.py 
3-Use Regex to find certain keywords

Resources: 
https://github.com/Uberi/speech_recognition/blob/master/examples/audio_transcribe.py 
https://realpython.com/python-speech-recognition/ tutorial for how to use the previous module
https://pythonbasics.org/transcribe-audio/
https://www.fullstackpython.com/blog/transcribe-recordings-speech-text-assemblyai.html
https://towardsdatascience.com/extracting-audio-from-video-using-python-58856a940fd splitting video into sep audio and video files
https://zulko.github.io/moviepy/install.html
https://pypi.org/project/moviepy/
http://pydub.com/
https://www.thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python

NOTE: MUST run split_movie.py in CMD terminal and NOT Powershell 
(no virtual environment in PS- virtual environment command (".speech\Scripts\activate.bat" works just fine in CMD)) 
- tested fine with a .MKV file for movie source and .MP3 as the audio output file 
- THIS fixes the audio level fixing issue in OpenShot, BTW!!