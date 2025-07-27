from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company, Employee
from api.serializers import CompanySerializer, EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


    #  companies/{companyId}/employee
    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        try:
            company = Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            return Response({"error": "Company not found"}, status=404)

        employees = Employee.objects.filter(Company=company)
        employees_serializer = EmployeeSerializer(employees, many=True, context={'request': request})
        return Response(employees_serializer.data)

# class MyViewSet(viewsets.ModelViewSet):
#     def get_serializer_class(self):
#         if self.action == 'list':
#             return CompanyListSerializer
#         return CompanyDetailSerializer  # Returns the class, not an instance

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer



