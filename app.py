import os
import streamlit as st

# Title of the web app
st.title("Hello Guys")
st.write("This page showcases my work samples on object detection.")

# List of video file paths
video_files = [
    '/Users/hemanthsai/Downloads/Output samples/v1.mp4',
    '/Users/hemanthsai/Downloads/Output samples/v2.mp4',
    '/Users/hemanthsai/Downloads/Output samples/v3.mp4',
    '/Users/hemanthsai/Downloads/Output samples/v4.mp4',
    '/Users/hemanthsai/Downloads/Output samples/v5.mp4',
    '/Users/hemanthsai/Downloads/Output samples/v6.mp4',
    '/Users/hemanthsai/Downloads/Output samples/v7.mp4',
    '/Users/hemanthsai/Downloads/Output samples/v8.mp4',
    '/Users/hemanthsai/Downloads/Output samples/v9.mp4',
    '/Users/hemanthsai/Downloads/Output samples/v10.mp4',
    '/Users/hemanthsai/Downloads/Output samples/v11.mp4'
]

# Display all videos
if video_files:
    for i, video_path in enumerate(video_files, start=1):
        if os.path.exists(video_path):
            st.subheader(f"Video {i}")
            with open(video_path, "rb") as video_file:
                video_bytes = video_file.read()
            st.video(video_bytes)
        else:
            st.warning(f"Video {i} not found: {video_path}")
else:
    st.warning("No videos found in the specified folder.")

# Footer
st.write("Thanks for viewing!")
