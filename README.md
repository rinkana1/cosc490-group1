# cosc490-group1
Communication is a fundamental aspect of human interaction, yet it can present significant challenges for individuals with neurological conditions such as Autism Spectrum Disorder (ASD) and Attention Deficit Hyperactivity Disorder (ADHD). These individuals may struggle to identify emotions and tones in spoken language, leading to misunderstanding and communication barriers. 

This project aims to develop an AI-driven system that analyzes voice messages in real-time, detecting the speaker’s tone through various linguistic and auditory cues. By leveraging machine learning techniques, this system will provide accurate emotional interpretations, enhancing interpersonal communication for individuals with neurodivergent conditions.

## How to Use
### Preprocessing
Once you clone this repository, you can run each individual file from the command line using the following command:

`$ python .\preprocessing\[file_name]`

The file should walk through through what input is needed, such as input directories and output file paths. For consistency, we recommend that you specify the absolute file path instead of relative paths, however either will work.

`preprocessing/timer.py` is used within the other files and should not be run standalone (it won't do anything).

## Todo
- [x] Preprocess data
- [ ] Train an auditory emotion detection model
- [ ] Train a speech-to-text model
- [ ] Combine speech-to-text and auditory model
- [ ] Record audio in real-time
- [ ] Create UI
- [ ] Decide on a name (the most important step of course)

## Changelog
### February 6, 2025 - Initial Commit
- Created repository
- Added collaborators to repository
### March 25, 2025 - Add preprocessing code and data
- Created `preprocessing/preprocess_audio.py`
- Created `preprocessing/transcribe_audio.py`
- Created `preprocessing/timer.py`
- Created `preprocessing/strip_csv.py`
- Added preexisting data from the MELD dataset (in `unprocessed_csv`)
- Added to processed data created by our code (in `processed_csv`)