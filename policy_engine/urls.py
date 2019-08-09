from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('transactions', views.TransactionView)
router.register('rules', views.RuleView)

urlpatterns = [
	path('transactions/confirmed', views.TransactionView.confirmed, name='confirmed'),
	path('transactions/rejected', views.TransactionView.rejected, name='rejected'),
	path('transactions/all', views.TransactionView.all, name='rejected'),
	path('', include(router.urls)),
]
