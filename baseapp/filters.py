import django_filters
from .models import Member, Organization, OrganizationPosts


class MemberFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Member
        fields = ['email', 'username', 'isOrganizationMember']
# {'title': ['icontains'],
# 		          'duration': ['exact'],
#                   'price': ['gt', 'lt'],
#                  }
