from django.conf.urls import url

from .views import AppraisalListView, AppraisalUpdateView, AppraisalCreateView, AppraisalDeleteView

urlpatterns = [
    url(r'^$', AppraisalListView.as_view(), name='list'),
    url(r'^create/$', AppraisalCreateView.as_view(), name="create"),
    # url(r'^(?P<slug>[\w-]+)/$', AppraisalUpdateView.as_view(), name="update"),
    url(r'^delete/(?P<pk>\d+)/$', AppraisalDeleteView.as_view(), name="delete"),
    url(r'^(?P<pk>\d+)/edit/$', AppraisalUpdateView.as_view(), name="detail"),
    # url(r'^(?P<pk>\d+)/$', AppraisalDetailView.as_view(), name="detail"),

]