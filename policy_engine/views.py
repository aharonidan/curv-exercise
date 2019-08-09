from rest_framework import viewsets, mixins
from .models import Transaction, Rule
from .serializers import TransactionSerializer, RuleSerializer

class TransactionView(mixins.CreateModelMixin,
					  mixins.ListModelMixin,
					  mixins.RetrieveModelMixin,
					  viewsets.GenericViewSet):

	queryset = Transaction.objects.all()
	serializer_class = TransactionSerializer

	def confirmed(request):
		return Transaction.objects.filter(status__exact='confirmed').all()

	def rejected(request):
		return Transaction.objects.filter(status__exact='rejected').all()

	def all(request):
		return Transaction.objects.all()

class RuleView(viewsets.ModelViewSet):
	queryset = Rule.objects.all()
	serializer_class = RuleSerializer
