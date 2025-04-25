# NeuroVoice – Real-Time Emotion Detection from Voice for Neurodivergent Support

## Abstract
Communication is a key part of human interaction. However, individuals with neurological conditions such as Autism Spectrum Disorder (ASD) and Attention Deficit Hyperactivity Disorder (ADHD) may struggle to identify emotions and tones in spoken language, leading to misunderstanding and communication barriers.

This project proposes an AI-powered system to assist neurodivergent individuals by analyzing voice messages in real time. The system detects emotional tone through auditory and linguistic cues using machine learning models. It integrates a speech-to-text transcription system with emotion detection to provide users with real-time emotional insights, enhancing accessibility and improving interpersonal communication.

## Team Members
- Mackinley Hill
- Anthony Williams
- Xavier Preston
- Dominique Paige

## Development Environment
The following tools and libraries were used throughout the project:
- **Jupyter Notebooks** – For modular development and iterative testing.
- **PyTorch** – Used in combination with Hugging Face Transformers to build and train deep learning models.
- **OpenAI Whisper** – A state-of-the-art speech-to-text model used for transcription.
- **Pandas** – For structured data manipulation, cleaning, and formatting.
- **FFmpeg** – For audio preprocessing and conversion to WAV format.
- **Electron + Django** – Used to develop a desktop user interface backed by a Python web framework.
- **GitHub** – Version control, collaboration, and issue tracking.

System Architecture
1. **Audio Preprocessing**  
    - Audio is converted and cleaned using FFmpeg.
    - Noise reduction and volume normalization are applied.  

2. **Speech Transcription**  
    - The Whisper API transcribes audio into text, supporting multiple accents and noisy environments.  

3. **Emotion Detection**  
    - The text is passed through a transformer-based model trained on the MELD dataset to detect emotional tone.  

4. **User Interface**  
    - The Electron frontend allows users to upload or record audio.
    - Django serves as the backend interface to interact with models.

## Installation and Setup
#### 1. **Clone the Repository**
```sh
$ git clone https://github.com/rinkana1/cosc490-group1.git`
$ cd cosc490-group1
```

#### 2. **Install Necessary Frameworks**
1. Install Python for your system: https://www.python.org/downloads/
2. Install Node.js for your system: https://nodejs.org/en/download
3. Ensure these frameworks are installed correctly using the following commands:
```sh
$ python --version
Python 3.X.XX
$ node -v
v22.14.0
```


#### 3. **Install Dependencies**
Run the setup file for your system:  
`setup.bat` for Windows  
`setup_mac.sh` for MacOS  
`setup_linux.sh` for Linux  

##### **For Windows Systems**
Install FFMPEG

1. Go to https://ffmpeg.org/download.html
2. Under “More Downloading Options”, hover over the Windows logo
3. Click on “Windows Builds from gyan.dev”
4. Download “ffmpeg-git-full.7z”
5. Once downloaded, extract files into C:\ffmpeg
6. Ensure that the files are in the correct directory, and not a subdirectory inside C:\ffmpeg
7. Open Start Search, type “env”, and select “Edit the system environment variables”.
8. Click the “Environment Variables…” button.
9. In the “System Variables” section, locate “Path”, and click edit.
10. In the “Edit environment variable” UI, click “New” and add “C:\ffmpeg\bin”
11. Press OK on all windows and restart your computer to ensure changes are accepted.
12. Ensure installation was successful using the following command:
```sh
$ ffmpeg -version
ffmpeg version 2025-03-03-git-d21ed2298e-essentials_build-www.gyan.dev Copyright (c) 2000-2025 the FFmpeg developers
...
```

##### **Troubleshooting**
If installation fails using setup files, run the following commands:  
```sh
$ pip install pydub openai-whisper transformers ffmpeg-python django
```
```sh
$ cd neurovoice_electron
$ npm install
```
\
For MacOS:
```sh
$ brew install ffmpeg
```
\
For Linux:
```sh
$ sudo apt update
$ sudo apt install ffmpeg
```

## Usage Instructions
1. Launch the UI using `start.bat` or `start.sh`:
	- Electron serves the frontend application.
	- Django runs the backend inference service.
2. Record, upload an audio file, or enter text to detect the emotion.
3. The system will output both a transcript and an emotional label in real time.

## Changelog
### February 6, 2025
- Initial commit
- Repository setup and team assigned
### March 25, 2025
- Preprocessing scripts added 
- MELD dataset imported and formatted
- Whisper STT integration completed
- Basic Electron/Django UI prototype created
### March 27, 2025
- STT implementation
- Baseline sentiment analysis
### April 8, 2025
- Implemented audio file upload for emotion detection
### April 10, 2025
- Updated UI for audio file upload page and homepage
### April 15, 2025
- Implemented real-time audio transcription and emotion detection
### April 17, 2025
- Cleaned up `main` branch
- Added setup files for easy installation  
### April 22, 2025
- Implemented text submission for emotion detection
- Updated setup files to ensure smooth installation
## References
1. Poria, S., Hazarika, D., Majumder, N., Zadeh, A., & Morency, L.-P. (2018). MELD: A Multimodal Multi-Party Dataset for Emotion Recognition in Conversations. Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics.
2. Radford, A., et al. (2022). Whisper: Robust Speech Recognition via Large-Scale Weak Supervision. OpenAI.
3. American Psychiatric Association. (2013). Diagnostic and Statistical Manual of Mental Disorders (5th ed.)