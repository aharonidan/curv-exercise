from django.db import models

# Create your models here.
class Transaction(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	amount  = models.FloatField(default=0)
	address = models.CharField(max_length=34)
	status = models.CharField(max_length=10, choices=[('confirmed', 'Confirmed'), ('rejected', 'Rejected')])

class Rule(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	max_amount = models.FloatField(default=0)
	currency = models.CharField(max_length=10, choices=[('USD', 'USD'), ('BTC', 'BTC')])
	whitelist_address = models.CharField(max_length=34)


