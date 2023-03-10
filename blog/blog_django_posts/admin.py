from django.contrib import admin

# Register your models here.
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "user")

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related("user")


admin.site.register(Post, PostAdmin)
