from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Employee
from .serializers import EmployeeModelSerializer
from .paginations import EmployeeCursorPagination

# Create your views here.
class EMPCRUDVIEW(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer
    pagination_class=EmployeeCursorPagination
    