from rest_framework.parsers import JSONParser
from django.db import IntegrityError
from . models import Event
from . models import Supportedby
from . models import our_partner
from . models import Association
from . models import Media_Partner
from . models import Testimonials
from . models import Speakers

from . serializers import EventSerializer
from . serializers import SupportedbySerializer
from . serializers import EventSerializer
from . serializers import SupportedbySerializer
from . serializers import our_partnerSerializer
from . serializers import AssociationSerializer
from . serializers import Media_PartnerSerializer
from . serializers import TestimonialsSerializer
from . serializers import SpeakersSerializer

from django.http.response import JsonResponse
from rest_framework.views import APIView
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt



# from django.shortcuts import (get_object_or_404)

# Create your views here.
# class Table(APIView):

'''Event'''
def eventApi(request): 
    if request.method=='GET':

        events = Event.objects.all()
        eventserializer = EventSerializer(events, many=True)

        supportedby = Supportedby.objects.all()
        supportedbyserializer = SupportedbySerializer(supportedby, many=True)

        ourpartner = our_partner.objects.all()
        ourpartnerSerializer = our_partnerSerializer(ourpartner, many=True)

        association = Association.objects.all()
        associationserializer = AssociationSerializer(association, many=True)

        mediapartner = Media_Partner.objects.all()
        mediapartnerSerializer = Media_PartnerSerializer(association, many=True)

        testimonials = Testimonials.objects.all()
        testimonialsserializer = TestimonialsSerializer(testimonials, many=True)

        speakers = Speakers.objects.all()
        speakersserializer = SpeakersSerializer(speakers, many=True)

        return JsonResponse({
            'event':eventserializer.data,
            'support':supportedbyserializer.data,
            'partner':ourpartnerSerializer.data,
            'associate':associationserializer.data,
            'media':mediapartnerSerializer.data,
            'test':testimonialsserializer.data,
            'speak':speakersserializer.data
            }, safe=False)
        
    elif request.method=='POST':
        event_data = JSONParser().parse(request)
        eventSerializer = EventSerializer(data=event_data)
        if eventserializer.is_valid():
            eventserializer.save()
            return JsonResponse(" Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)


        
'''SUPPORTED BY'''
def supportedbyApi(self,request): #id is delect method to delete based on id number
    if request.method=='GET':
        supportedby = Supportedby.objects.all()
        supportedbyserializer = SupportedbySerializer(supportedby, many=True)
        return JsonResponse(supportedbyserializer.data, safe=False)
        
    elif request.method=='POST':
        supportedby_data = JSONParser().parse(request)
        supportedbyserializer = SupportedbySerializer(data=supportedby_data)
        if supportedbyserializer.is_valid():
            supportedbyserializer.save()
            return JsonResponse(" Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
        

'''OUR PARTNERS'''
def ourpartnerApi(self,request): #id is delect method to delete based on id number
    if request.method=='GET':
        ourpartner = our_partner.objects.all()
        ourpartnerSerializer = our_partnerSerializer(ourpartner, many=True)
        return JsonResponse(ourpartnerSerializer.data, safe=False)
        
    elif request.method=='POST':
        ourpartner_data = JSONParser().parse(request)
        ourpartnerSerializer = our_partnerSerializer(data=ourpartner_data)
        if ourpartnerSerializer.is_valid():
            ourpartnerSerializer.save()
            return JsonResponse(" Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)



'''ASSOCIATION'''
def associationApi(self,request): #id is delect method to delete based on id number
    if request.method=='GET':
        association = Association.objects.all()
        associationserializer = AssociationSerializer(association, many=True)
        return JsonResponse(associationserializer.data, safe=False)
        
    elif request.method=='POST':
        association_data = JSONParser().parse(request)
        associationserializer = AssociationSerializer(data=association_data)
        if associationserializer.is_valid():
            associationserializer.save()
            return JsonResponse(" Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)



'''MEDIA PARTNER'''
def mediapartnerApi(self,request): #id is delect method to delete based on id number
    if request.method=='GET':
        mediapartner = Media_Partner.objects.all()
        mediapartnerSerializer = Media_PartnerSerializer(association, many=True)
        return JsonResponse(mediapartnerSerializer.data, safe=False)
        
    elif request.method=='POST':
        mediapartner_data = JSONParser().parse(request)
        mediapartnerserializer = Media_PartnerSerializer(data=association_data)
        if mediapartnerserializer.is_valid():
            mediapartnerserializer.save()
            return JsonResponse(" Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)


'''TESTIMONIALS'''
def testimonialsApi(self,request): #id is delect method to delete based on id number
    if request.method=='GET':
        testimonials = Testimonials.objects.all()
        testimonialsserializer = TestimonialsSerializer(testimonials, many=True)
        return JsonResponse(testimonialsserializer.data, safe=False)
        
    elif request.method=='POST':
        testimonials_data = JSONParser().parse(request)
        testimonialsserializer = TestimonialsSerializer(data=testimonials_data)
        if testimonialsserializer.is_valid():
            testimonialsserializer.save()
            return JsonResponse(" Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)


'''SPEAKERS'''
def speakersApi(self,request): #id is delect method to delete based on id number
    if request.method=='GET':
        speakers = Speakers.objects.all()
        speakersserializer = SpeakersSerializer(speakers, many=True)
        return JsonResponse(speakersserializer.data, safe=False)
        
    elif request.method=='POST':
        speakers_data = JSONParser().parse(request)
        speakersserializer = SpeakersSerializer(data=speakers_data)
        if speakersserializer.is_valid():
            speakersserializer.save()
            return JsonResponse(" Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)


      

    


