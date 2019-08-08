from rest_framework import serializers
from .models import Transaction, Rule


class TransactionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Transaction
		fields = ('id', 'amount', 'address', 'status')

	def create(self, validated_data):
		transaction = super(TransactionSerializer, self).create(validated_data)
		rules = Rule.objects.filter(whitelist_address__exact=transaction.address).filter(max_amount__gte=transaction.amount)
		transaction.status = 'rejected' if not rules else 'confirmed'

		return transaction

class RuleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Rule
		fields = ('id', 'max_amount', 'currency', 'whitelist_address')
