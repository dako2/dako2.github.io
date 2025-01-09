from moviepy.editor import VideoFileClip

# Load the MP4 video
video = VideoFileClip("msa.mp4")

# Convert to GIF and save
video.write_gif("msa.gif")
