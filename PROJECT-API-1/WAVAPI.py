# In  the Terminal
# pip install transformers torch speechrecognition pydub
# Put the .wav file in the same folder as this code

import speech_recognition as sr
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

def speech_to_text(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)  # Uses Google Speech API
        return text
    except sr.UnknownValueError:
        return "Error: Could not understand audio"
    except sr.RequestError:
        return "Error: Could not request results"

# Example usage
audio_path = "dia1_utt0.wav"  # Replace with your .wav file
transcribed_text = speech_to_text(audio_path)
print("Transcribed Text:", transcribed_text)



# Load the model and tokenizer
model_name = "bhadresh-savani/bert-base-uncased-emotion"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Define emotion labels
emotion_labels = ["sadness", "joy", "love", "anger", "fear", "surprise"]

def detect_emotion(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        logits = model(**inputs).logits
    probabilities = torch.nn.functional.softmax(logits, dim=-1)
    
    # Get the highest emotion score
    top_emotion = emotion_labels[torch.argmax(probabilities)]
    return top_emotion, probabilities.numpy().tolist()[0]

# Run emotion detection on the transcribed text
if transcribed_text and "Error" not in transcribed_text:
    emotion, scores = detect_emotion(transcribed_text)
    print(f"Detected Emotion: {emotion}")
    print(f"Emotion Scores: {dict(zip(emotion_labels, scores))}")
else:
    print("Could not analyze emotion due to transcription error.")
