from django.conf.urls import url
from . import views

app_name='recycle_app'


urlpatterns=[
        url(r'^events/register/$',views.Event_Register.as_view()),
        url(r'^events/list_events/$',views.Event_List.as_view()),
        url(r'^events/delete/([0-9]+)/$',views.UserDelete),
        # url(r'^events/delete/$',views.Delete_Event.as_view())
        # url(r'^events/delete/(?P<id>\d+)/$','Event_Delete.views.delete')
        # url(r'^ events/delete/(?p<id>d+)/$',views.Delete_Event.as_view()),
        # url(r'^$',views.Home.as_view()),
        url(r'^supportedby/register/$',views.Supportedby_Register.as_view()),
        url(r'^suppportedby/list_support/$',views.Supportedby_List.as_view()),
        url(r'^supportedby/delete/([0-9]+)/$',views.UserDelete),

       
        url(r'^partners/register/$',views.our_partner_Register.as_view()),
        url(r'^partners/list_support/$',views.our_partner_List.as_view()),
        url(r'^partners/delete/([0-9]+)/$',views.UserDelete),

        url(r'^associate/register/$',views.Association_Register.as_view()),
        url(r'^associate/list_support/$',views.Association_List.as_view()),
        url(r'^associate/delete/([0-9]+)/$',views.UserDelete),

        url(r'^media/register/$',views.Media_Partner_Register.as_view()),
        url(r'^media/list_support/$',views.Media_Partner_List.as_view()),
        url(r'^media/delete/([0-9]+)/$',views.UserDelete),

        url(r'^test/register/$',views.Testimonials_Register.as_view()),
        url(r'^test/list_support/$',views.Testimonials_List.as_view()),
        url(r'^test/delete/([0-9]+)/$',views.UserDelete),

        url(r'^speak/register/$',views.Speakers_Register.as_view()),
        url(r'^speak/list_support/$',views.Speakers_List.as_view()),
        url(r'^speak/delete/([0-9]+)/$',views.UserDelete),
]

