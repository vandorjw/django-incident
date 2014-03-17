django-incident
===============

This is a django application which allows you to report incidents.

To use it, clone this repository as 'incident'.

Add 'incident' to your installed_applications

Modify your urls.py file to inlude

urlpatterns = patterns(
    '',
    ...
    url(r'^incident/', include('incident.urls', namespace='incident', app_name='incident')),
    ...
)


