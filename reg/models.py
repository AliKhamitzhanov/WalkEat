from django.db import models
from django.db import models
from django.contrib.auth.models import (
    AbstractUser,
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)
# Create your models here.

from phonenumber_field.modelfields import PhoneNumberField
from card.models import Card

from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  

class MyUserManager(BaseUserManager):
    def _create_user(self, email, username, password, phone, **extra_fields):
        if not email:
            raise ValueError("Нету Email")
        if not username:
            raise ValueError("Нету Логин")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            password=password,
            phone=phone,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password, phone):
        return self._create_user(email, username, password, phone)

    def create_superuser(self, email, username, password, phone):
        return self._create_user(
            email, username, password, phone, is_staff=True, is_superuser=True
        )


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone = PhoneNumberField(unique=True)
    photo = models.ImageField(default='media/avatar.jpeg', blank=True)
    payment = models.ForeignKey(Card, on_delete=models.CASCADE, null=True, related_name='user_card')
    birthday = models.DateField(null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["email", "username"]
    objects = MyUserManager()

    def __str__(self):
        return self.username

    @property
    def get_card(self):
        return self.payment.objects.all()




@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )