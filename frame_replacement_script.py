import cv2

def replace_frames_in_video(input_video_path, output_video_path, start_frame, end_frame, new_frame_path):
    # Open the input video file
    cap = cv2.VideoCapture(input_video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video file {input_video_path}.")
        return

    # Get video properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Read the new frame from the image file
    new_frame = cv2.imread(new_frame_path)
    if new_frame is None:
        print(f"Error: Could not open new frame image {new_frame_path}.")
        cap.release()
        return

    # Resize the new frame to match the video frame size
    new_frame = cv2.resize(new_frame, (frame_width, frame_height))

    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

    # Process and write each frame
    for i in range(total_frames):
        ret, frame = cap.read()
        if not ret:
            break

        # Replace the specified range of frames
        if start_frame <= i <= end_frame:
            frame = new_frame

        # Write the frame to the output video
        out.write(frame)

    # Release resources
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"Frames {start_frame} to {end_frame} replaced and saved to {output_video_path}")

# Parameters
input_video_path = '/Users/abhinav/Downloads/khushi_reels_edit/atharva_video_denoised.mp4'
output_video_path = '/Users/abhinav/Downloads/khushi_reels_edit/atharva_video_denoised_range_test.mp4'
start_frame = 0  # Start frame (0-indexed)
end_frame = 200    # End frame (0-indexed)
new_frame_path = '/Users/abhinav/Downloads/replacement.png'

# Replace the frames in the video
replace_frames_in_video(input_video_path, output_video_path, start_frame, end_frame, new_frame_path)

