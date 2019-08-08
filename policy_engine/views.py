from django.shortcuts import render
from rest_framework import viewsets
# from rest_framework.decorators import api_view
from .models import Transaction, Rule
from .serializers import TransactionSerializer, RuleSerializer
# Create your views here.


class TransactionView(viewsets.ModelViewSet):
	queryset = Transaction.objects.all()
	serializer_class = TransactionSerializer

	# @api_view(['POST',])
	# def create(self, request):
	# 	amount = request.data["amount"],
	# 	address = request.data["address"]
	# 	breakpoint()
	# 	Rule.objects.filter(address__exact=address).filter(max_amount__gte=amount).all()




class RuleView(viewsets.ModelViewSet):
	queryset = Rule.objects.all()
	serializer_class = RuleSerializer
