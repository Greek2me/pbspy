from django.conf.urls import include, patterns, url
from django.contrib.auth import views as auth_views

from pbspy import views

urlpatterns = patterns('',
    url(r'^$', views.game_list, name='game_list'),
    url(r'^game/(?P<pk>\d+)/$', views.game_detail, name='game_detail'),
    url(r'^game/(?P<game_id>\d+)/log/$', views.game_log, name='game_log'),
    url(r'^game/(?P<game_id>\d+)/manage/(?P<action>[^/]*)/?$', views.game_manage, name='game_manage'),
    url(r'^game/(?P<game_id>\d+)/update/$', views.game_update_manual, name='game_update_manual'),
    url(r'^game/(?P<game_id>\d+)/change/$', views.game_change, name='game_change'),
    url(r'^game/(?P<game_id>\d+)/subscribe/$', views.game_subscribe, {'subscribe': True}, name='game_subscribe'),
    url(r'^game/(?P<game_id>\d+)/unsubscribe/$', views.game_subscribe, {'subscribe': False}, name='game_unsubscribe'),
    url(r'^game/(?P<game_id>\d+)/savefilter/$', views.game_save_filter, name='game_save_filter'),
    url(r'^game/(?P<game_id>\d+)/loadfilter/(?P<filter_name>[^/]*)$', views.game_load_filter, name='game_load_filter'),
    url(r'^game/(?P<game_id>\d+)/removefilter/(?P<filter_name>[^/]*)$', views.game_remove_filter, name='game_remove_filter'),
    url(r'^update$', views.game_update),
    url(r'^game/create/$', views.game_create, name='game_create'),
    url(r'^set_timezone$', views.set_timezone, name='set_timezone'),
    (r'^accounts/', include('registration.backends.default.urls')),
    # url(r'^login$', 'django.contrib.auth.views.login', name='login'),
    # url(r'^logout$', 'django.contrib.auth.views.logout', name='logout'),
    # url(r'', include('registration.backends.default.urls')),
    # url(r'', include('django.contrib.auth.urls')),
)
