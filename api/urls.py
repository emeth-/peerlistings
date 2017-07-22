from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^get_datatable_data$', "api.views.get_datatable_data"),
    url(r'^sell$', "api.views.sell"),
    url(r'^autocomplete/(?P<obj>\w+)/$', "api.views.autocomplete"),
    url(r'^$', "api.views.dtables_example"),
)
