from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=250)
    description = RichTextUploadingField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.summary
