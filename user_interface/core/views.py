from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
import os
from sr_api import whisperapi as wa

@csrf_exempt
def upload_audio(request):
    if request.method == 'POST' and request.FILES.get('audio'):
        audio_file = request.FILES['audio']
        fs = FileSystemStorage()
        filename = fs.save(audio_file.name, audio_file)
        uploaded_file_url = os.path.join(__file__, "..\\..\\media\\", filename)

        # TODO: Run Whisper and emotion analysis here
        transcribed_text = wa.speech_to_text_whisper(uploaded_file_url)
        emotion, scores = wa.detect_emotion(transcribed_text.strip())

        return render(request, 'core/result.html', {
            'emotion': emotion,
            'transcribed_text': transcribed_text,
            'scores': dict(zip(wa.emotion_labels, scores)),
            'filename': filename,
            'fileurl': uploaded_file_url
        })
    return render(request, 'core/upload.html')