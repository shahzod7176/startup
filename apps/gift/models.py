from django.db.models import Model, ForeignKey, CASCADE, CharField, TextField, DateField
from authentication.models import CustomUser


class GiftSent(Model):
    sender = ForeignKey('authentication.CustomUser', CASCADE, related_name='gift_sent')
    receiver = ForeignKey('authentication.CustomUser', CASCADE, related_name='gift_received')
    gift_description = CharField(max_length=255)
    provide = TextField()
    delivery_date = DateField()
    status = CharField(
        max_length=255,
        choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('declined', 'Declined')],
        default='pending'
    )

    def __str__(self):
        return f'Gift from {self.sender} to {self.receiver}'
