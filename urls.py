from django.conf.urls import url, patterns, include
from django.contrib.auth.decorators import login_required
from incident import views

urlpatterns = patterns(
    "",
    url(
        regex=r"^create/$",
        view=login_required(views.IncidentCreateView.as_view()),
        name="incident_create",
    ),
    url(
        regex=r"^$",
        view=views.IncidentListView.as_view(),
        name='incident_list',
    ),
    url(
        regex=r"^(?P<pk>\d+)/$",
        view=views.IncidentDetailView.as_view(),
        name="incident_detail",
    ),
    url(
        regex=r"^update/(?P<pk>\d+)/$",
        view=login_required(views.IncidentUpdateView.as_view()),
        name="incident_update",
    ),
)
