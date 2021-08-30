import moviepy.editor as mp

#TODO: Insert prompt for file name

#ID the video file to be split
my_clip = mp.VideoFileClip(r"ParkAccessOverview_with_Dave_2020-11-09_09-32-38.mkv")

#TODO: Insert prompt for output file name

#Write Audio file
my_clip.audio.write_audiofile(r"ParkAccessOverview_with_Dave.mp3")

#TODO Turn this into a graphical tool that let's you pick the file from the file browser

