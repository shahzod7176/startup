from root import settings
from django.db.models import Model, ForeignKey, CASCADE, CharField, TextField, BooleanField, DateTimeField


class Notification(Model):
    user = ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=CASCADE,
        related_name="notifications"
    )
    title = CharField(max_length=255)
    message = TextField()
    is_read = BooleanField(default=False)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} -> {self.user.username}"
