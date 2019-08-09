from rest_framework import serializers
from .models import Transaction, Rule
import requests


class TransactionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Transaction
		fields = ('id', 'amount', 'address', 'status')

	def create(self, validated_data):
		transaction = super(TransactionSerializer, self).create(validated_data)

		ticker = requests.get('https://blockchain.info/ticker').json()
		usd_amount = ticker['USD']['last'] * transaction.amount

		usd_rules = Rule.objects.filter(whitelist_address__exact=transaction.address).filter(currency__exact='USD').filter(max_amount__gte=usd_amount)
		btc_rules = Rule.objects.filter(whitelist_address__exact=transaction.address).filter(currency__exact='BTC').filter(max_amount__gte=transaction.amount)
		rules = usd_rules | btc_rules


		transaction.status = 'rejected' if not rules else 'confirmed'

		return transaction

class RuleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Rule
		fields = ('id', 'max_amount', 'currency', 'whitelist_address')
