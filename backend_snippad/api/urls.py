from django.urls import path
from .views import (
    FolderList,
    FolderDetail,
    SnippetList,
    SnippetDetail,
    FolderSnippetList,
)

urlpatterns = [
    path("folders/", FolderList.as_view(), name="folder-list"),
    path("folders/<int:pk>/", FolderDetail.as_view(), name="folder-detail"),
    path(
        "folders/<int:pk>/snippets/",
        FolderSnippetList.as_view(),
        name="folder-snippets",
    ),
    path("snippets/", SnippetList.as_view(), name="snippet-list"),
    path("snippets/<int:pk>/", SnippetDetail.as_view(), name="snippet-detail"),
]
