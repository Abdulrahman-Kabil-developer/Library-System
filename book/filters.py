from django.db.models.fields import CharField
import django_filters
from .models import book
class booktFilter(django_filters.FilterSet):
    title=django_filters.CharFilter(lookup_expr='icontains')
    description=django_filters.CharFilter(lookup_expr='icontains')
    author=django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = book

        fields = '__all__'
        exclude=['owner','image','slug','publishedAt','numberOfPages','borrowingPeriod']