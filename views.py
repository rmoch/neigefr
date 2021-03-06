import datetime
from django.views.generic import ListView
from django.conf import settings
from neigefr.models import Snowflake


class IndexView(ListView):
    "Home page"
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(IndexView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['GOOGLE_MAPS_KEY'] = settings.GOOGLE_MAPS_KEY
        return context

    def get_queryset(self):
        datetime_limit = datetime.datetime.now() - datetime.timedelta(hours=4)
        queryset = Snowflake.objects.exclude(date_created__lt=datetime_limit)[:100]
        return queryset


class TextView(ListView):
    "View for text rendering of the latest flakes. Used by the Leaflet JS toolkit"
    template_name = 'textview.txt'

    def get_queryset(self):
        datetime_limit = datetime.datetime.now() - datetime.timedelta(hours=4)
        queryset = Snowflake.objects.exclude(date_created__lt=datetime_limit)[:100]
        return queryset
