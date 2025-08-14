from django.db import models

class UploadedImage(models.Model):
    original = models.ImageField(upload_to="originals/")
    thumbnail_small = models.ImageField(upload_to="thumbnails/", null=True, blank=True)
    thumbnail_medium = models.ImageField(upload_to="thumbnails/", null=True, blank=True)
    thumbnail_large = models.ImageField(upload_to="thumbnails/", null=True, blank=True)

    def __str__(self):
        return f"Image {self.id}"
