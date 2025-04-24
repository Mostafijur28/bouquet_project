from django.contrib import admin
from .models import Bouquet, Comment, Vote

@admin.register(Bouquet)
class BouquetAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_at')
    readonly_fields = ('share_id',)
    search_fields = ('title', 'description')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'bouquet', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('text', 'author__username')

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'bouquet', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'bouquet__title')
