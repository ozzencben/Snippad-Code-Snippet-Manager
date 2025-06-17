from django.contrib import admin
from .models import CodeBlock, Folder, Snippet

admin.site.register(CodeBlock)
admin.site.register(Folder)
admin.site.register(Snippet)
