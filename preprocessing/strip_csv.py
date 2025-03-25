"""
Reformats MELD CSV files to only include necessary data.

The MELD dataset contains a lot of information that is unnecessary for training, such as the
speaker, season, episode, etc. This module is meant to reduce the amount of data in each CSV to make
training more efficient.
"""

### Imports
import pandas as pd

def main():

    # Load CSV file
    dataset_path = input("Enter path for dataset: ")
    print(f"Loading dataset {dataset_path}...")

    df = pd.read_csv(dataset_path)

    print(f"Successfully loaded dataset {dataset_path}.")
    print(df.head()) # Check dataset structure

    output_file = input("Enter output file path: ") # CSV file to output to.

    new_df = df[["Sr No.", "Utterance", "Emotion", "Sentiment", "Dialogue_ID", "Utterance_ID"]]

    new_df.to_csv(output_file, index = False)

    print(f"CSV successfully stripped and saved to {output_file}")
    print(new_df.head())
    

if __name__ == "__main__":
    main()