from django.shortcuts import render
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Sales
from .serializers import SalesSerializer
from rest_framework.views import APIView
from django.http import JsonResponse
import json
from django.db.models import Count,  Sum
from django.db.models.functions import ExtractYear
from django.db import connection
from sales.service import render_to_pdf
from django.http import HttpResponse
# Create your views here.

class SaleCreateView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = SalesSerializer
    queryset = Sales.objects.all()


class SaleUpdateView(UpdateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = SalesSerializer
    queryset = Sales.objects.all()


class ReportAPIView(APIView):
    permission_classes = (AllowAny,)
    http_method_names = ['get']

    def get(self, request, format=None):
        total_order_count_per_year = Sales.objects.annotate(year=ExtractYear('order_date')).values('year').annotate(counts=Count('year')).values('year','counts')
        customer_count = Sales.objects.distinct('customer_id')
        total_customer_transaction = Sales.objects.values('customer_id').annotate(counts=Sum('sales')).values('customer_id','counts').order_by('-counts')[0:3]    
        most_selling = Sales.objects.values('sub_category').annotate(counts=Count('sub_category')).values('sub_category','counts').order_by('-counts') 
        pie_chart = Sales.objects.values('region').annotate(counts=Sum('sales')).values('region','counts').order_by('-counts') 
        line_chart = Sales.objects.annotate(year=ExtractYear('order_date')).values('year').annotate(amounts=Sum('sales')).values('year','amounts')
        # Custom SQL Query for customer transactions per year
        cursor = connection.cursor()
        raw_query = "select customer_id, extract(year from order_date) as yyyy, count(*) from public.sales_sales group by customer_id, extract(year from order_date) ORDER BY customer_id, extract(year from order_date);"
        cursor.execute(raw_query)
        data = cursor.fetchall()
        customer_transactions_per_year = {}
        for i in data:
            if customer_transactions_per_year.get(i[0]):
                customer_transactions_per_year.get(i[0])[i[1]] = i[2]
            else:
                customer_transactions_per_year[i[0]] = {
                    i[1]: i[2]
                }

        context = {
            "items1" : total_order_count_per_year,
            "items2" : len(customer_count),
            "items3" : total_customer_transaction,
            "items4" : customer_transactions_per_year,
            "items5" : most_selling,
            "items6" : pie_chart,
            "items7" : line_chart
        }
        pdf = render_to_pdf('pdf.html', context)
        pdf_file = HttpResponse(pdf, content_type='application/pdf')
        return pdf_file
        