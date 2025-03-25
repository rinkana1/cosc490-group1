"""
Transcribes audio in to text.

In order to see how accurate the real-time audio transcription will be, we implemented this module
which transcribes each audio file and saves the transcriptions to a copy of the original CSV file.
This should only be done for testing purposes and with small datasets as the transcription takes
a very long time.

Advisory: This process takes 25 minutes for 1,112 audio files (~1.3 secs/file).
"""

### Imports
import os
import pandas as pd
import sys
from timer import Timer
import traceback
import whisper

### Functions

def transcribe_audio(
        audio_path: str,
        model: whisper.Whisper
    ) -> str:
    """
    Transcribes an audio file (.wav format) into text using OpenAI's Whisper model.

    Args:
        audio_path (str): The path of the audio file being transcribed
        model (Whisper): A Whisper model

    Returns:
        result (str): The transcription of the audio file
    """
    try:
        result = model.transcribe(audio_path)
        return result["text"]
    except Exception as e:
        print(f"Ran into an error during audio transcription:\n{traceback.format_exc()}")
        return ""


def transcribe_dir(
        input_dir: str, 
        model: whisper.Whisper,
        t: Timer
    ) -> dict:
    """
    Runs through each file in a directory and transcribes each audio file into text.

    Args:
        input_dir (str): The path of the input directory
        model (Whisper): A Whisper model
        t (Timer): A Timer object to keep track of elapsed time

    Returns:
        transcriptions (dict): A dictionary which maps the file name to each transcription

    Raises:
        OSError: Input directory not found. Please specfiy and existing directory.
        OSError: Selected input directory is empty. Please specify a different directory.
    """
    # Handle errors
    if not os.path.exists(input_dir):
        raise OSError("Input directory not found. Please specify an existing directory.")

    if len(os.listdir(input_dir)) == 0:
        raise OSError("Selected input directory is empty. Please specify a different directory.")
    
    transcriptions = {}
    counter = 1
    total = len(os.listdir(input_dir)) 

    for file in os.listdir(input_dir):
        if file.endswith(".wav"):
            audio_path = os.path.join(input_dir, file)

            sys.stdout.write(f"Transcribing {audio_path} ({counter}/{total}). Time elapsed: {t.get_elapsed_time()}")
            sys.stdout.flush()

            transcriptions[file] = transcribe_audio(audio_path, model)

            sys.stdout.write("\r" + " " * 120 + "\r")
            sys.stdout.flush()
        counter += 1
    
    return transcriptions


def merge_transcriptions(
        transcriptions: dict,
        df: pd.DataFrame,
        output_file: str,
        t: Timer
    ):
    """
    Merges transcriptions with existing dataset and saves to an output file.

    Args:
        transcriptions (dict): A dictionary mapping audio file names to their text transcriptions
        df (DataFrame): A dataframe containing utterance and emotion data
        output_file (str): The path of an output CSV file
        t (Timer): A Timer object to keep track of elapsed time

    Raises:
        KeyError: Missing required columns: Ensure the dataset contains 'Dialogue_ID' and 'Utterance_ID'.
    """
    print("Merging transcriptions...")
    t.start()

    if "Dialogue_ID" not in df.columns or "Utterance_ID" not in df.columns:
        raise KeyError("Missing required columns: Ensure the dataset contains 'Dialogue_ID' and 'Utterance_ID'.")
    
    df["Whisper_Transcriptions"] = df.apply(
        lambda row: transcriptions.get(f"dia{row['Dialogue_ID']}_utt{row['Utterance_ID']}.wav", ""),
        axis=1
    )

    df.to_csv(output_file, index=False)
    print(f"CSV saved successfully at {output_file} in {t.stop()}.")
    print(df.head())
    
    return

### Main Function

def main():
    t = Timer()
    
    # Load CSV file
    dataset_path = input("Enter path for dataset: ")
    print(f"Loading dataset {dataset_path}...")
    t.start()
    
    df = pd.read_csv(dataset_path)

    print(f"Successfully loaded dataset in {t.stop()}.")
    print(df.head()) # Check dataset structure

    # Allows the user to cancel execution in case the wrong file is selected
    continue_exe = input("Would you like to continue execution? (y/n): ")
    if continue_exe != "y": return

    input_dir = input("Enter input directory path: ")
    output_file = input("Enter output file path: ")
    
    # Load the Base Whisper Model
    print("Loading Whisper Model...")
    t.start()
    model = whisper.load_model("base")
    print(f"Whisper model successfully loaded in {t.stop()}!")

    # Transcribe the audio and create a CSV file with Whisper Transcriptions added to it
    print("\nBeginning audio transcription...")
    t.start()
    
    transcriptions = transcribe_dir(input_dir, model, t)
    print("Transcription keys:", list(transcriptions.keys())[:5])
    print(f"Audio transcription finished in {t.stop()}.")

    merge_transcriptions(transcriptions, df, output_file, t)

    return

if __name__ == "__main__":
    main()