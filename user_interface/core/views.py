from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
import os
from sr_api import whisperapi as wa

def homepage(request):
    return render(request, 'core/home.html')

@csrf_exempt
def upload_audio(request):
    if request.method == 'POST' and request.FILES.get('audio'):
        audio_file = request.FILES['audio']
        fs = FileSystemStorage()
        filename = fs.save(audio_file.name, audio_file)
        uploaded_file_url = os.path.join(__file__, "..\\..\\media\\", filename)

        transcribed_text = wa.speech_to_text_whisper(uploaded_file_url)
        emotion, scores = wa.detect_emotion(transcribed_text.strip())

        return render(request, 'core/result.html', {
            'emotion': emotion.upper(),
            'transcribed_text': transcribed_text,
            'sadness': round(scores[0] * 100, 2) if scores[0] > 0.01 else 1,
            'joy': round(scores[1] * 100, 2) if scores[1] > 0.01 else 1,
            'love': round(scores[2] * 100, 2) if scores[2] > 0.01 else 1,
            'anger': round(scores[3] * 100, 2) if scores[3] > 0.01 else 1,
            'fear': round(scores[4] * 100, 2) if scores[4] > 0.01 else 1,
            'surprise': round(scores[5]  * 100, 2) if scores[5] > 0.01 else 1,
            'filename': filename,
            'fileurl': uploaded_file_url
        })
    return render(request, 'core/upload.html')

def record_audio(request):
    return render(request, 'core/record.html')

@csrf_exempt
def analyze_audio(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST only'}, status=405)

    if request.FILES.get('audio'):
        print("I got to the backend")

        audio_file = request.FILES['audio']
        fs = FileSystemStorage()
        filename = fs.save(audio_file.name, audio_file)
        uploaded_file_url = os.path.join(__file__, "..\\..\\media\\", filename)

        print(uploaded_file_url)

        transcribed_text = wa.speech_to_text_whisper(uploaded_file_url)
        print("Transcribed Text:", transcribed_text)

        emotion, scores = wa.detect_emotion(transcribed_text.strip())

        
        print("Emotion", emotion)

        return JsonResponse({
            'emotion': emotion.upper(),
            'transcribed_text': transcribed_text,
            'sadness': round(scores[0] * 100, 2) if scores[0] > 0.01 else 1,
            'joy': round(scores[1] * 100, 2) if scores[1] > 0.01 else 1,
            'love': round(scores[2] * 100, 2) if scores[2] > 0.01 else 1,
            'anger': round(scores[3] * 100, 2) if scores[3] > 0.01 else 1,
            'fear': round(scores[4] * 100, 2) if scores[4] > 0.01 else 1,
            'surprise': round(scores[5]  * 100, 2) if scores[5] > 0.01 else 1
        })
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def submit_text(request):
    return render(request, 'core/text.html')