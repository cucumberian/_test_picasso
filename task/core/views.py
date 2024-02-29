from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import authentication
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser, JSONParser
from rest_framework.views import APIView
from .serializers import FileSerializer
from .models import File


class FileUploadView(APIView):
    """
    post a file
    """
    # permission_classes = (permissions.AllowAny,)
    permission_classes = []
    # parser_classes = (FileUploadParser,)
    parser_classes = (MultiPartParser, )
    # parser_classes = (FileSerializer.parser_classes,)
    # parser_classes = (FileSerializer,)
    # parser_classes = (File)
    def post(self, request, *arg, **kwargs):
        
        up_file = request.FILES["file"]
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            with open(file="temp.file", mode='wb') as f:
                for chunk in up_file.chunks():
                    f.write(chunk)
            serializer.save()
            # celery
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileListView(APIView):
    """
    get all files
    """
    def get(self, request, format=None):
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data)

    # def get(self, request, format=None):
    #     files = File.objects.all()
    #     serializer = FileSerializer(files, many=True)
    #     return Response(serializer.data)
