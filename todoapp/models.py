from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # <- 여기!

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.user.name}] {self.title}"
