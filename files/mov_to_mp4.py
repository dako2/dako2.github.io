from moviepy.video.io.VideoFileClip import VideoFileClip

# Input and output file paths
input_file = "/Users/dako22/Desktop/msa.mov"
output_file = "/Users/dako22/Desktop/msa.mp4"

# Load the video and write it as an MP4
clip = VideoFileClip(input_file)
clip.write_videofile(output_file, codec="libx264", audio_codec="aac")

print("Conversion complete!")

