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
from tutor_account.views import register, show_all_tutors, show_all_helps, fill_out_profile

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/$', register, name='register'),
    url(r'^all_tutor_profiles/$', show_all_tutors, name='show_all_tutors'),
    url(r'^all_helps/$', show_all_helps, name='show_all_helps'),
    url(r'^profile_fill/$', fill_out_profile, name='fill_out_profile'),
]



from django.conf import settings
from django.views.static import serve

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
