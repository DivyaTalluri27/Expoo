from django.conf.urls import url
from . import views

app_name='recycle_app'


urlpatterns=[
        
        #for retrieving the data'''
        url(r'^tables/$',views.eventApi),

        #for inserting the data'''
         url(r'^event/insert/$',views.eventApi),
        url(r'^supportedby/insert/$',views.supportedbyApi),
        url(r'^ourpartner/insert/$',views.ourpartnerApi),
        url(r'^association/insert/$',views.associationApi),
        url(r'^mediapartner/insert/$',views.mediapartnerApi),
        url(r'^testimonials/insert/$',views.testimonialsApi),
        url(r'^speakers/insert/$',views.speakersApi),
]

