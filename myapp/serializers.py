from rest_framework import serializers
from .models import UploadedImage

class UploadedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedImage
        fields = "__all__"
        read_only_fields = ["thumbnail_small", "thumbnail_medium", "thumbnail_large"]
