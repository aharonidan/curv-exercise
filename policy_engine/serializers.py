from rest_framework import serializers
from .models import Transaction, Rule


class TransactionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Transaction
		fields = ('id', 'amount', 'address', 'status')

class RuleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Rule
		fields = ('id', 'max_amount', 'currency', 'whitelist_address')
