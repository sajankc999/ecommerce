from django_filters import FilterSet
from .models import Customer
class CustomeUserFilter(FilterSet):
    class Meta:
        model = Customer
        fields = {
            
            # "gender":['gt','lt'],
            "gender":['exact'],

        }