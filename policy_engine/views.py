from rest_framework import viewsets, mixins
from .models import Transaction, Rule
from .serializers import TransactionSerializer, RuleSerializer

class TransactionView(mixins.CreateModelMixin,
					  mixins.ListModelMixin,
					  mixins.RetrieveModelMixin,
					  viewsets.GenericViewSet):

	queryset = Transaction.objects.all()
	serializer_class = TransactionSerializer

class RuleView(viewsets.ModelViewSet):
	queryset = Rule.objects.all()
	serializer_class = RuleSerializer
