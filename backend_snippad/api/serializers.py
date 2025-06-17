from rest_framework import serializers, generics
from .models import Folder, Snippet, CodeBlock


class CodeBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeBlock
        fields = ["id", "html_code", "css_code", "js_code"]


class SnippetSerializer(serializers.ModelSerializer):
    code_block = CodeBlockSerializer()

    folder = serializers.PrimaryKeyRelatedField(queryset=Folder.objects.all())

    class Meta:
        model = Snippet
        fields = ["id", "title", "folder", "code_block"]

    def create(self, validated_data):
        code_block_data = validated_data.pop("code_block")
        snippet = Snippet.objects.create(**validated_data)
        CodeBlock.objects.create(snippet=snippet, **code_block_data)
        return snippet

    def update(self, instance, validated_data):
        code_block_data = validated_data.pop("code_block", None)
        instance.title = validated_data.get("title", instance.title)
        instance.folder = validated_data.get("folder", instance.folder)
        instance.save()

        if code_block_data:
            code_block = instance.code_block
            code_block.html_code = code_block_data.get(
                "html_code", code_block.html_code
            )
            code_block.css_code = code_block_data.get("css_code", code_block.css_code)
            code_block.js_code = code_block_data.get("js_code", code_block.js_code)
            code_block.save()

        return instance


class FolderSerializer(serializers.ModelSerializer):
    snippets = SnippetSerializer(many=True, read_only=True)

    class Meta:
        model = Folder
        fields = ["id", "title", "snippets"]


# Views:


class FolderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer


class FolderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer


class SnippetListCreateAPIView(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
