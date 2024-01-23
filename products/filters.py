from django_filters import FilterSet
from .models import customer
class CustomeUserFilter(FilterSet):
    class Meta:
        model = customer
        fields = {
            
            # "gender":['gt','lt'],
            "gender":['exact'],

        }