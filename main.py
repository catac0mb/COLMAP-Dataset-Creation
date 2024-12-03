# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# Importing all necessary libraries
import cv2
import os



def extract_images_from_video(video_path, output_folder):
    """Extracts images from a video and saves them to a folder."""

    # Create a VideoCapture object
    video = cv2.VideoCapture(video_path)

    # Check if the video opened successfully
    if not video.isOpened():
        print("Error opening video file")
        return

    # Initialize frame counter
    frame_count = 0

    while True:
        # Read the next frame
        ret, frame = video.read()

        # Break the loop if the end of the video is reached
        if not ret:
            break

        # Save the frame as an image
        image_path = f"{output_folder}/frame_{frame_count:04d}.jpg"
        cv2.imwrite(image_path, frame)

        # Increment the frame counter
        frame_count += 1

    # Release the VideoCapture object
    video.release()

    print("Images extracted successfully!")

# Example usage
video_path = "/Users/vivianajohnson/Desktop/Splat/room/IMG_4900.mov"
output_folder = "/Users/vivianajohnson/Desktop/Splat/room/images"

extract_images_from_video(video_path, output_folder)


