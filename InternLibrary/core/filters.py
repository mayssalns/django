from django_filters import rest_framework as filters
from .models import Author, Book


class AuthorFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Author
        fields = '__all__'


class BookFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Book
        fields = '__all__'


class BookDetailFilter(filters.FilterSet):
    author = filters.Filter('author', lookup_expr='exact')

    class Meta:
        model = Book
        fields = '__all__'