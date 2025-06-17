from django.db import models


class Folder(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Snippet(models.Model):
    folder = models.ForeignKey(
        Folder, related_name="snippets", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class CodeBlock(models.Model):
    snippet = models.OneToOneField(
        Snippet, related_name="code_block", on_delete=models.CASCADE
    )
    html_code = models.TextField(blank=True, null=True)
    css_code = models.TextField(blank=True, null=True)
    js_code = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"CodeBlock for {self.snippet.title}"
