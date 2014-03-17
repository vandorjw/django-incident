django-incident
===============

This is a django application which allows you to report incidents.

To use it, clone this repository as 'incident'.

Add 'incident' to your installed_applications

    INSTALLED_APPS = (
        ...
        'incident',
        ...
    )

Modify your urls.py file to inlude


    urlpatterns = patterns(
        '',
        ...
        url(r'^incident/', include('incident.urls', namespace='incident', app_name='incident')),
        ...
    )
    
I have already included South_Migrations.
These may not work with django 1.7

Requirements:

 - Python3
 - Django 1.5+


