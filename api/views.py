from api.models import Company, Employee
from api.serializers import CompanySerializer, EmployeeSerializer
from rest_framework.decorators import action
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        pass

# class MyViewSet(viewsets.ModelViewSet):
#     def get_serializer_class(self):
#         if self.action == 'list':
#             return CompanyListSerializer
#         return CompanyDetailSerializer  # Returns the class, not an instance

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer



