import django_filters
from .models import RegisterForm

class PeopleFilter(django_filters.FilterSet):
  age = django_filters.AllValuesFilter()

  class Meta:
      model = RegisterForm
      fields = ['age']