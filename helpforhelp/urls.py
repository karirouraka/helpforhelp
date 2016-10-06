"""helpforhelp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.conf.urls import url
from django.contrib import admin
from tutor_account.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/$', register, name='register'),
    url(r'^log_in/$', log_in, name='log_in'),
    url(r'^log_out/$', log_out, name='log_out'),
    url(r'^loged_out_successfully/$', loged_out_successfully, name='loged_out_successfully'),

    url(r'^profile_fill/$', fill_out_profile, name='fill_out_profile'),
    url(r'^all_tutor_profiles/$', show_all_tutors, name='show_all_tutors'),
    url(r'^get_tutor_by_name/(?P<tutor_pk>\d+)/$', get_tutor_by_pk, name='get_tutor_by_name'),
    url(r'^send_reference/(?P<tutor_pk>\d+)/$', send_reference, name='send_reference'),
    url(r'^all_helps/$', show_all_helps, name='show_all_helps'),
    url(r'^get_help/(?P<help_pk>\d+)/$', get_help, name='get_help'),
    url(r'^detailed_help_information/(?P<help_pk>\d+)/$', get_help, name='detailed_help_information'),
    # url(r'^get_content_by_title/(?P<post_pk>\d+)/$', get_content_by_title, name='get_content_by_title'),
    url(r'^register_help/$', fill_out_help, name='register_help'),
    url(r'^edit_help/(?P<help_pk>\d+)/$', edit_help, name='edit_help'),
    url(r'^delete_help/(?P<help_pk>\d+)/$', delete_help, name='delete_help'),



]



from django.conf import settings
from django.views.static import serve

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
