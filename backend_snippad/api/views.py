from rest_framework import generics
from .models import Folder, Snippet
from .serializers import FolderSerializer, SnippetSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class FolderList(generics.ListCreateAPIView):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer

class FolderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class FolderSnippetList(APIView):
    def get(self, request, pk):
        try:
            folder = Folder.objects.get(pk=pk)
        except Folder.DoesNotExist:
            return Response({"detail": "Folder not found."}, status=404)
        
        snippets = folder.snippets.all()  # related_name='snippets' olduğu için
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)