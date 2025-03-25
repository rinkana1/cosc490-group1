"""
Converts all video files from MELD dataset into audio.

The MELD dataset provides clips from the show Friends for emotional dataset training, but all of the
provided files are in MP4 format, which is both an inefficient use of storage and unnecessary since
our AI will only be processing the audio and not any visual data.

This module fixes that by converting all MP4 files in a specified directory into WAV audio files
with a sample rate of 16k MHz and mono channels.

Advisory: This code on average takes about 25 minutes for 9,988 video files (~0.15 secs/file)
"""

# Imports
import ffmpeg
import librosa
import os
import sys
from timer import Timer
import traceback

def convert_mp4_to_wav(
        input_dir: str,
        output_dir: str,
        t: Timer
        ):
    """
    Convert all audio files in a given directory to 16kHz mono WAV

    Args:
        input_dir (str): The path to the input directory
        output_dir (str): The path to the output directory
        t (Timer): A Timer object to keep track of elapsed time

    Throws:
        OSError: Input directory not found. Please specify an existing directory.
        OSError: Selected input directory is empty. Please specify a different directory.
    """
    if not os.path.exists(input_dir):
        raise OSError("Input directory not found. Please specify an existing directory.")

    input_dir_list = os.listdir(input_dir)

    if len(input_dir_list) == 0:
        raise OSError("Selected input directory is empty. Please specify a different directory.")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    print("Beginning MP4 to WAV conversion...")
    t.start()
    errors = []
    err_count = 0

    for file in input_dir_list:
        try:
            if file.endswith(".mp4"):
                input_path = os.path.join(input_dir, file)
                output_path = os.path.join(output_dir, file.replace(".mp4", ".wav"))
            
                # Convert using FFmpeg
                process = (
                    ffmpeg.input(input_path)
                    .output(output_path, ac=1, ar=16000, format="wav")
                    .global_args("-y") # Overwrites files if they already exist
                    .run_async(pipe_stdout=True, pipe_stderr=True)
                )

                # Logs progress in the console
                while True:
                    output = process.stderr.readline()
                    if not output:
                        break
                    output = output.decode().strip()
                    if "time=" in output:
                        sys.stdout.write(f"\rProcessing {file}: {output} Time elapsed: {t.get_elapsed_time()}    ")
                        sys.stdout.flush()

                process.wait()

                sys.stdout.write("\r" + " " * 120 + "\r")
                sys.stdout.flush()
                
        except ffmpeg.Error as e: # Catch specifically ffmpeg exceptions
            err = f"Error processing {file}:\n{traceback.format_exc()}\nFFmpeg stderr:\n{e.stderr.decode()}"
            errors.append(err)
            err_count += 1
        
        except Exception as e: # Catch any other exception
            err = f"Error processing {file}:\n{traceback.format_exc()}"
            errors.append(err)
            err_count += 1

    print(f"Audio preprocessor successfully completed MP4 to WAV conversion in {t.stop()}.")

    # Print errors if any
    if errors:
        print("Audio preprocessor ran into the following errors during conversion: ")
        for err in errors:
            print(f"{err}\n")


def verify_audio_format(
        sample_file: str,
        t: Timer
        ):
    """
    Verifies that the audio file is in the correct format on Mono and 16000 Hz

    Args:
        sample_file (str): An audio file
        t (Timer): A Timer object to keep track of elapsed time
    
    Throws:
        FileNotFoundError: Cannot find specified sample file for audio verification: {sample_file}
    """
    if not os.path.exists(sample_file):
        raise FileNotFoundError(f"Cannot find specified sample file for audio verification: {sample_file}")
    
    print("Beginning audio verification")
    print(f"Loading sample file {sample_file}...")
    t.start()

    try:
        y, sr = librosa.load(sample_file, sr=None) # Load audio file
    except Exception as e:
        print(f"Error thrown during audio verification: {traceback.format_exc}")
        t.stop()
        return

    print(f"Sample file loaded in {t.stop()}.")
    print(f"Sample Rate: {sr} Hz") # Expected: 16000
    print(f"Channels: {'Mono' if len(y.shape) == 1 else 'Stereo'}") # Expected: Mono

### Main Function

if __name__ == "__main__":
    # Training Data
    input_dir = input("Enter input directory path: ")
    output_dir = input("Enter output directory path: ")

    t = Timer()

    convert_mp4_to_wav(input_dir, output_dir, t)

    sample_file_path = os.path.join(output_dir, os.listdir(output_dir)[0])

    verify_audio_format(sample_file_path, t)