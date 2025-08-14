from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import UploadedImage
from .serializers import UploadedImageSerializer
from .tasks import generate_thumbnails

class UploadedImageViewSet(viewsets.ModelViewSet):
    queryset = UploadedImage.objects.all()
    serializer_class = UploadedImageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        image_obj = serializer.save()
        
        # Trigger Celery task
        task = generate_thumbnails.delay(image_obj.id)
        return Response({"task_id": task.id, "image_id": image_obj.id})

    @action(detail=False, methods=["get"])
    def status(self, request):
        from celery.result import AsyncResult
        task_id = request.query_params.get("task_id")
        if not task_id:
            return Response({"error": "task_id is required"}, status=400)
        result = AsyncResult(task_id)
        return Response({"task_id": task_id, "status": result.status, "result": result.result})
