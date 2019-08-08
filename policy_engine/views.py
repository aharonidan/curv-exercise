from django.shortcuts import render
from rest_framework import viewsets
from .models import Transaction, Rule
from .serializers import TransactionSerializer, RuleSerializer

class TransactionView(viewsets.ModelViewSet):
	queryset = Transaction.objects.all()
	serializer_class = TransactionSerializer

class RuleView(viewsets.ModelViewSet):
	queryset = Rule.objects.all()
	serializer_class = RuleSerializer
