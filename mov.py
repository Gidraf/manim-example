from moviepy import VideoFileClip, concatenate_videoclips

def combine_videos():
    # Load videos
    clip1 = VideoFileClip("media/videos/what_is_an_array/480p15/ArrayExplanation.mp4")
    clip2 = VideoFileClip("media/videos/array_process/480p15/ArrayAnimation.mp4")

    # Concatenate clips
    final_clip = concatenate_videoclips([clip1, clip2])

    # Export the final video
    final_clip.write_videofile("final.mp4", codec="libx264", fps=15)

if __name__ == "__main__":
    combine_videos()
