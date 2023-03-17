import os
import subprocess

# Choose a codec & compression setting
codec = "libx265"
crf = "28"

# Path to the video files you want to compress
input_dir = r"C:\input"

# Path to directory where you want to save compressed files
output_dir = r"C:\output"

# Get a list of all .mp4 files in the directory
video_files = [f for f in os.listdir(input_dir) if f.endswith(".mp4")]

# Iterate through the files and compress them using ffmpeg
for file in video_files:
    input_video = os.path.join(input_dir, file)
    output_video = os.path.join(output_dir, file)
    
    # Run the ffmpeg command to compress the video
    subprocess.call(["ffmpeg", "-i", input_video, "-c:v", codec, "-crf", crf, output_video])