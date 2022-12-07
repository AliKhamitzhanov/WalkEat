from django.db import models
from creditcards.models import CardExpiryField, CardNumberField, SecurityCodeField
from master import settings

class Card(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_card"
    , null=True)

    cc_expiry = CardExpiryField('expiration_date')
    cc_number = CardNumberField('card_number')
    cc_code = SecurityCodeField('security_code')

    def __str__(self):
        return f'{self.cc_number}{self.user} card'  