from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
import whisper

def speech_to_text_whisper(audio_file):
    model = whisper.load_model("base")  # Use "small", "medium", or "large" for better accuracy
    result = model.transcribe(audio_file)
    return result["text"]

# Example usage
# audio_path = "dia1_utt0.wav"  # Replace with your actual file
# transcribed_text = speech_to_text_whisper(audio_path)
# print("Transcribed Text:", transcribed_text)


# Load the emotion detection model
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
# if transcribed_text.strip():
#     emotion, scores = detect_emotion(transcribed_text)
#     print(f"Detected Emotion: {emotion}")
#     print(f"Emotion Scores: {dict(zip(emotion_labels, scores))}")
# else:
#     print("Could not analyze emotion due to transcription error.")
