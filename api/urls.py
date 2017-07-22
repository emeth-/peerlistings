from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^get_datatable_data$', "api.views.get_datatable_data"),
    url(r'^sell$', "api.views.sell"),
    url(r'^calc_fee$', "api.views.calc_fee"),
    url(r'^submit_sell$', "api.views.submit_sell"),
    url(r'^buy$', "api.views.buy"),
    url(r'^autocomplete/(?P<obj>\w+)/$', "api.views.autocomplete"),
    url(r'^$', "api.views.howitworks"),
)
