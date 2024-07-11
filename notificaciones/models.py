from django.db import models
from usuarios.models import Personal

class Notification(models.Model):
    user = models.ForeignKey(Personal, on_delete=models.PROTECT, related_name='notifications')
    message = models.TextField()
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.nombrePersonal}"
