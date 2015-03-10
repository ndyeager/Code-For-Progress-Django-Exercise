from django.conf.urls import patterns, include, url
from django.contrib import admin

# Uses Regular Expression to route request to views in order to render the page
urlpatterns = patterns('',
    url(r'^$', 'questions.views.home', name='home'),
    url(r'^(?P<question_id>\d+)/$', 'questions.views.detail', name='detail'),
    url(r'^admin/', include(admin.site.urls)),
)