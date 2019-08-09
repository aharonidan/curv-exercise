from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Transaction(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	amount  = models.FloatField(default=0, validators=[MinValueValidator(0)])
	address = models.CharField(max_length=34)
	status = models.CharField(max_length=10, choices=[('confirmed', 'Confirmed'), ('rejected', 'Rejected')])


class Rule(models.Model):

	CURRENCIES = ['BTC', 'USD', 'AUD', 'BRL', 'CAD', 'CHF', 'CLP', 'CNY', 'DKK', 'EUR', 'GBP', 'HKD', 'INR', 'ISK', 'JPY', 'KRW', 'NZD', 'PLN', 'RUB', 'SEK', 'SGD', 'THB', 'TWD']

	created = models.DateTimeField(auto_now_add=True)
	max_amount = models.FloatField(default=0, validators=[MinValueValidator(0)])
	currency = models.CharField(max_length=3, choices=[(ticker, ticker) for ticker in CURRENCIES])
	whitelist_address = models.CharField(max_length=34)

