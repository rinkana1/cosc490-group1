from transformers import AutoModelForSequenceClassification, AutoTokenizer
import subprocess
import torch
import whisper

# Define emotion labels
emotion_labels = ["sadness", "joy", "love", "anger", "fear", "surprise"]

# Load Whisper model
whisper_model = whisper.load_model("base")

# Load the emotion detection model
model_name = "bhadresh-savani/bert-base-uncased-emotion"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

def speech_to_text_whisper(audio_file):
    result = whisper_model.transcribe(audio_file)
    return result["text"]
    
def convert_to_wav(source_path):
    target_path = source_path.replace('.webm', '.wav')
    subprocess.run([
        'ffmpeg', '-y', '-i', source_path, '-ar', '16000', '-ac', '1', target_path
    ])
    return target_path

def detect_emotion(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        logits = model(**inputs).logits
    probabilities = torch.nn.functional.softmax(logits, dim=-1)
    
    # Get the highest emotion score
    top_emotion = emotion_labels[torch.argmax(probabilities)]
    return top_emotion, probabilities.numpy().tolist()[0]
