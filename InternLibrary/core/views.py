from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from django_filters import rest_framework as filters
from .filters import AuthorFilter, BookFilter
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('name')
    serializer_class = AuthorSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = AuthorFilter

    @action(detail=True)
    def book(self, request, pk=None):
        return Response(list(Book.objects.filter(author=pk).values()))

class BookAuthorViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('name')
    serializer_class = AuthorSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = AuthorFilter

    @action(detail=True)
    def book(self, request, pk=None):
        return Response(list(Book.objects.filter(author=pk).values()))

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('name')
    serializer_class = BookSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = BookFilter

    @action(detail=True)
    def author(self, request, pk=None):

        return Response(list(Author.objects.filter(book=pk).values()))

