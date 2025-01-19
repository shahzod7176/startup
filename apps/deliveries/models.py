from root import settings
from django.db.models import Model, OneToOneField, ForeignKey, SET_NULL, CASCADE, TextChoices, TextField, CharField, \
    DateTimeField


class DeliveryStatus(TextChoices):
    PENDING = 'PENDING', 'Pending'
    IN_PROGRESS = 'IN_PROGRESS', 'In Progress'
    COMPLETED = 'COMPLETED', 'Completed'
    CANCELLED = 'CANCELLED', 'Cancelled'


class Delivery(Model):
    courier = ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=SET_NULL,
        null=True,
        blank=True,
        related_name='deliveries'
    )
    address = TextField()
    status = CharField(
        max_length=20,
        choices=DeliveryStatus.choices,
        default=DeliveryStatus.PENDING
    )
    delivered_at = DateTimeField(null=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Delivery{self.status}"
