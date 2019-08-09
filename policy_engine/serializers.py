from rest_framework import serializers
from .models import Transaction, Rule
from .helpers import btc_to_usd


class TransactionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Transaction
		fields = ('id', 'amount', 'address', 'status')
		read_only_fields = ('status',)

	def create(self, validated_data):

		btc_amount = validated_data['amount']
		usd_amount = btc_to_usd(btc_amount)

		whitelisted_address_rules = Rule.objects.filter(whitelist_address__exact=validated_data['address'])
		usd_rules = whitelisted_address_rules.filter(currency__exact='USD').filter(max_amount__gte=usd_amount)
		btc_rules = whitelisted_address_rules.filter(currency__exact='BTC').filter(max_amount__gte=btc_amount)
		rules = usd_rules | btc_rules

		validated_data['status'] = 'rejected' if not rules else 'confirmed'

		return super(TransactionSerializer, self).create(validated_data)

class RuleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Rule
		fields = ('id', 'max_amount', 'currency', 'whitelist_address')
