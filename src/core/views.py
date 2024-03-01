from django.db import transaction
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from .serializers import FileSerializer
from .models import File
from .tasks import file_process


class HealthCheckView(APIView):
    def get(self, request, format=None):
        return Response(data={"status": "ok"}, status=status.HTTP_200_OK)


class FileUploadView(APIView):
    permission_classes = []
    parser_classes = (MultiPartParser,)

    def post(self, request, *arg, **kwargs):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # celery task
            file_id = serializer.data.get("id")
            transaction.on_commit(lambda: file_process.delay(file_id=file_id))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileListView(APIView):
    def get(self, request, format=None):
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data)
