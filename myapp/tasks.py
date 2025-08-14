import os
from PIL import Image
from celery import shared_task
from django.conf import settings
from .models import UploadedImage

@shared_task
def generate_thumbnails(image_id):
    image_obj = UploadedImage.objects.get(id=image_id)
    img_path = image_obj.original.path
    sizes = {
        "small": (100, 100),
        "medium": (300, 300),
        "large": (500, 500)
    }

    for size_name, size in sizes.items():
        img = Image.open(img_path)
        img.thumbnail(size)
        filename = f"{size_name}_{os.path.basename(img_path)}"
        save_path = os.path.join(settings.MEDIA_ROOT, "thumbnails", filename)
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        img.save(save_path)

        setattr(image_obj, f"thumbnail_{size_name}", f"thumbnails/{filename}")

    image_obj.save()
    return f"Thumbnails generated for Image {image_id}"
