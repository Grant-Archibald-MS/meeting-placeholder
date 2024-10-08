import ffmpeg
import os

def stream_image_to_rtmps(image_path, rtmps_url, stream_key):
    # Combine the RTMPS URL and stream key
    full_rtmps_url = f'{rtmps_url}/{stream_key}'

    # Create an ffmpeg input from the image
    input_stream = ffmpeg.input(image_path, loop=1, framerate=1)

    # Set up the output stream to the RTMPS feed
    output_stream = ffmpeg.output( input_stream, full_rtmps_url, vcodec='libx264', b='100k', s='1280x720', pix_fmt='yuv420p', f='flv')

    # Run the ffmpeg command
    ffmpeg.run(output_stream)

# Example usage
image_path = 'Placeholder.jpeg'
rtmps_url = input("Enter the RTMPS URL: ")
stream_key = input("Enter the stream key: ")

script_dir = os.getcwd()
full_image_path = os.path.join(script_dir, image_path)

print(full_image_path)

stream_image_to_rtmps(full_image_path, rtmps_url, stream_key)