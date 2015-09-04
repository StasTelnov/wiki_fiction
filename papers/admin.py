from django.contrib import admin
from .models import Paper, Tag, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class PaperAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    list_display = ('title', 'text')

admin.site.register(Paper, PaperAdmin)
admin.site.register(Tag)
