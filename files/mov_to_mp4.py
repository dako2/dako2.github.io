from moviepy.video.io.VideoFileClip import VideoFileClip

# Input and output file paths
input_file = "P1020975.MOV"
output_file = "P1020975.mp4"

# Load the video and write it as an MP4
clip = VideoFileClip(input_file)
clip.write_videofile(output_file, codec="libx264", audio_codec="aac")

print("Conversion complete!")

