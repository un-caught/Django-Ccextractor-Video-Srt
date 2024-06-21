from django.db import models

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/')
    subtitles = models.TextField(blank=True)