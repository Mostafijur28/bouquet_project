from django.db import models
from django.contrib.auth.models import User
import uuid

class Bouquet(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='bouquets/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    share_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    bouquet = models.ForeignKey(Bouquet, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.bouquet.title}'

class Vote(models.Model):
    bouquet = models.ForeignKey(Bouquet, on_delete=models.CASCADE, related_name='votes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('bouquet', 'user')

    def __str__(self):
        return f'Vote by {self.user.username} on {self.bouquet.title}'
