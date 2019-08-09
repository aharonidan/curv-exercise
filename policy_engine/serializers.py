from rest_framework import serializers
from .models import Transaction, Rule
import requests


class TransactionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Transaction
		fields = ('id', 'amount', 'address', 'status')
		read_only_fields = ('status',)

	def create(self, validated_data):

		transaction_amount = validated_data['amount']

		ticker = requests.get('https://blockchain.info/ticker')
		usd_rate = ticker.json()['USD']['last']
		# convert amount to usd
		usd_amount = usd_rate * transaction_amount

		usd_rules = Rule.objects.filter(whitelist_address__exact=validated_data['address']).filter(currency__exact='USD').filter(max_amount__gte=usd_amount)
		btc_rules = Rule.objects.filter(whitelist_address__exact=validated_data['address']).filter(currency__exact='BTC').filter(max_amount__gte=transaction_amount)
		rules = usd_rules | btc_rules
		validated_data['status'] = 'rejected' if not rules else 'confirmed'
		return super(TransactionSerializer, self).create(validated_data)

class RuleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Rule
		fields = ('id', 'max_amount', 'currency', 'whitelist_address')
