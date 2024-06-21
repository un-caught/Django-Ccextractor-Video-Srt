# myapp/management/commands/extract_subtitles.py

import os
from django.core.management.base import BaseCommand
from subprocess import Popen, PIPE

class Command(BaseCommand):
    help = 'Extract subtitles using CCExtractor'

    def handle(self, *args, **kwargs):
        video_file = 'C:/Users/uncaught/Desktop/django/subtitle_project/videos/8849331ddae9c3169024d569ce17b9a4fdd917401cd6c6bfb8dc1fd59c6af21e.mp4'  # Replace with actual path to your video file

        # Command to run CCExtractor
        ccextractor_command = 'C:/Users/uncaught/Desktop/django/subtitle_project/CCExtractor_win_portable/ccextractorwinfull.exe'
        output_directory = 'C:/Users/uncaught/Desktop/django/subtitle_project/videos'

        # Example command to extract subtitles
        cmd = [
            ccextractor_command,
            '-out=txt',  # Specify output format (e.g., srt, ttml, etc.)
            '-o', os.path.join(output_directory, 'output.txt'),  # Output file path
            video_file
        ]

        # Run CCExtractor
        process = Popen(cmd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()

        if process.returncode == 0:
            self.stdout.write(self.style.SUCCESS('Subtitles extracted successfully'))
        else:
            self.stderr.write(self.style.ERROR(f'Failed to extract subtitles: {stderr.decode("utf-8")}'))
