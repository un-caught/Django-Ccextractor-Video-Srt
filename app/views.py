# myapp/views.py

import os
from subprocess import Popen, PIPE
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import VideoForm

def extract_subtitles(video_file_path):
    # Command to run CCExtractor
    ccextractor_command = os.path.join(settings.BASE_DIR, 'CCExtractor_win_portable/ccextractorwinfull.exe')
    output_directory = os.path.join(settings.MEDIA_ROOT, 'static/subtitles')  # Adjust output directory as needed

    # Ensure output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Example command to extract subtitles
    cmd = [
        ccextractor_command,
        '-out=srt',  # Specify output format (e.g., srt, ttml, etc.)
        '-o', os.path.join(output_directory, 'output.srt'),  # Output file path
        video_file_path
    ]

    # Run CCExtractor
    process = Popen(cmd, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        return True, 'Subtitles extracted successfully'
    else:
        return False, f'Failed to extract subtitles: {stderr.decode("utf-8")}'

def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video_file = request.FILES['video_file']

            # Save the uploaded file temporarily
            temp_video_path = os.path.join(settings.MEDIA_ROOT, 'static/temp', video_file.name)
            with open(temp_video_path, 'wb') as f:
                for chunk in video_file.chunks():
                    f.write(chunk)

            # Process the video file with CCExtractor
            success, message = extract_subtitles(temp_video_path)

            # Clean up temporary file
            os.remove(temp_video_path)

            if success:
                return redirect('success/')
            else:
                return redirect('error/')

    else:
        form = VideoForm()

    return render(request, 'app/upload.html', {'form': form})


def successPage(request):

    return render(request, 'app/success.html')

def errorPage(request):

    return render(request, 'app/error.html')
    
