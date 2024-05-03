import django_filters
from .models import BusinessUnit


class CountryFilter(django_filters.FilterSet):
    """
    Фильтр для сортировки по стране.
    Этот фильтр позволяет фильтровать объекты BusinessUnit по полю country.
    """

    country = django_filters.CharFilter(field_name='country', lookup_expr='icontains', distinct=True)

    class Meta:
        model = BusinessUnit
        fields = ['country']
