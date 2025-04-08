from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
import os

@csrf_exempt
def upload_audio(request):
    if request.method == 'POST' and request.FILES.get('audio'):
        audio_file = request.FILES['audio']
        fs = FileSystemStorage
        filename = fs.save(audio_file.name, audio_file)
        uploaded_file_url = fs.url(filename)

        # TODO: Run Whisper and emotion analysis here
        emotion = "neutral" # Placeholder for result

        return render(request, 'core/result.html', {
            'emotion': emotion,
            'filename': filename
        })
    return render(request, 'core/upload.html')