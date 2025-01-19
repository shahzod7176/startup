from django.db.models import DateTimeField, TextField, CharField, OneToOneField, Model, CASCADE

from root.settings import AUTH_USER_MODEL


class CustomerProfile(Model):
    user = OneToOneField(AUTH_USER_MODEL, CASCADE, related_name='profile')
    address = TextField(blank=True, null=True, help_text="Foydalanuvchining manzili")
    phone_number = CharField(max_length=15, blank=True, null=True, help_text="Telefon raqami")
    additional_info = TextField(blank=True, null=True, help_text="Qo'shimcha ma'lumotlar")
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
