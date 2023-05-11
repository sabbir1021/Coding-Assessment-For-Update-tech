from django.urls import path
from .views import SaleCreateView, SaleUpdateView, ReportAPIView

app_name = "sales"

urlpatterns = [
    path('sale/', SaleCreateView.as_view()),
    path('sale/<int:pk>', SaleUpdateView.as_view()),
    path('report/', ReportAPIView.as_view()),
    
]

