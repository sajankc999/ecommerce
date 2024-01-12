from rest_framework.pagination import PageNumberPagination

class Custompagination(PageNumberPagination):
    page_size= 2