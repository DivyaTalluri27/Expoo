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
class Event_Register(APIView):
    def post(self,request):
        try:
            register_data=JSONParser().parse(request)
            event_data= Event.objects.create(
                                            name=register_data['name'],
                                            startDate=register_data['startDate'],
                                            endDate=register_data['endDate'],
                                            status=register_data['status'],
                                            registrationCharge=register_data['registrationCharge'],
                                            registrationTax=register_data['registrationTax'],
                                            registrationTotal=register_data['registrationTotal'],
                                            fileUpload=register_data['fileUpload'],
                                            description=register_data['description']
                                            )
            event_data.save()
            return JsonResponse("successfully registered!!",safe=False)

        except IntegrityError:
            return JsonResponse('user of this data is already exist!!',safe=False)

class Event_List(APIView):
    def get(self,request):
        events=Event.objects.all()
        serializer=EventSerializer(events,many=True)
        return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def UserDelete(request,id=0):
    try:
        if request.method=='DELETE':
            event=Event.objects.get(id=id)
            event.delete()
            return JsonResponse('deleted successfully!!',safe=False)
    except Exception:
        return JsonResponse('Id not found!!',safe=False)
        
    
    
    # def delete(self,request,id):
        # delete_event=request.data
        # delete_event=self.get_object(id=id)
         # delete_event = delete_event.objects.filter(pk=id).delete()
        # event=Event.objects.get(id=delete_event["id"])
        # event.delete()
        # return JsonResponse("successfully deleted!!",safe=False)


class Supportedby_Register(APIView):
    def post(self,request):
        try:
            register_data=JSONParser().parse(request)
            supportedby_data= Supportedby.objects.create(
                                            nameofthecompany=register_data['nameofthecompany'],
                                            imgurl=register_data['imgurl']
                                           )
            supportedby_data.save()
            return JsonResponse("successfully registered!!",safe=False)

        except IntegrityError:
            return JsonResponse('user of this data is already exist!!',safe=False)


class Supportedby_List(APIView):
    def get(self,request):
        supportedby=Supportedby.objects.all()
        serializer=SupportedbySerializer(supportedby,many=True)
        return JsonResponse(serializer.data,safe=False)  

@csrf_exempt
def UserDelete(request,id=0):
    try:
        if request.method=='DELETE':
            supportedby=Supportedby.objects.get(id=id)
            supportedby.delete()
            return JsonResponse('deleted successfully!!',safe=False)
    except Exception:
        return JsonResponse('Id not found!!',safe=False)


'''OUR PARTNERS'''
class our_partner_Register(APIView):
    def post(self,request):
        try:
            register_data=JSONParser().parse(request)
            ourpartner_data= our_partner.objects.create(
                                            name=register_data['name'],
                                            img_url=register_data['img_url'],
                                            link=register_data['link']
                                           )

            ourpartner_data.save()
            return JsonResponse("successfully registered!!",safe=False)

        except IntegrityError:
            return JsonResponse('user of this data is already exist!!',safe=False)


class our_partner_List(APIView):
    def get(self,request):
        ourpartner=our_partner.objects.all()
        serializer=our_partnerSerializer(ourpartner,many=True)
        return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def UserDelete(request,id=0):
    try:
        if request.method=='DELETE':
            ourpartner=our_partner.objects.get(id=id)
            ourpartner.delete()
            return JsonResponse('deleted successfully!!',safe=False)
    except Exception:
        return JsonResponse('Id not found!!',safe=False)


'''ASSOCIATION'''
class Association_Register(APIView):
    def post(self,request):
        try:
            register_data=JSONParser().parse(request)
            association_data= Association.objects.create(
                                            name=register_data['name'],
                                            img_url=register_data['img_url'],
                                            link=register_data['link']
                                           )
            association_data.save()
            return JsonResponse("successfully registered!!",safe=False)

        except IntegrityError:
            return JsonResponse('user of this data is already exist!!',safe=False)


class Association_List(APIView):
    def get(self,request):
        association=Association.objects.all()
        serializer=AssociationSerializer(association,many=True)
        return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def UserDelete(request,id=0):
    try:
        if request.method=='DELETE':
            association=Association.objects.get(id=id)
            association.delete()
            return JsonResponse('deleted successfully!!',safe=False)
    except Exception:
        return JsonResponse('Id not found!!',safe=False)


'''MEDIA PARTNER'''
class Media_Partner_Register(APIView):
    def post(self,request):
        try:
            register_data=JSONParser().parse(request)
            mediapartner_data= Media_Partner.objects.create(
                                            name=register_data['name'],
                                            img_url=register_data['img_url'],
                                            link=register_data['link']
                                           )
            mediapartner_data.save()
            return JsonResponse("successfully registered!!",safe=False)

        except IntegrityError:
            return JsonResponse('user of this data is already exist!!',safe=False)


class Media_Partner_List(APIView):
    def get(self,request):
        mediapartner=Media_Partner.objects.all()
        serializer=AssociationSerializer(mediapartner,many=True)
        return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def UserDelete(request,id=0):
    try:
        if request.method=='DELETE':
            mediapartner=Media_Partner.objects.get(id=id)
            mediapartner.delete()
            return JsonResponse('deleted successfully!!',safe=False)
    except Exception:
        return JsonResponse('Id not found!!',safe=False)



'''TESTIMONIALS'''
class Testimonials_Register(APIView):
    def post(self,request):
        try:
            register_data=JSONParser().parse(request)
            testimonials_data= Testimonials.objects.create(
                                            name=register_data['name'],
                                            img_url=register_data['img_url'],
                                            link=register_data['link']
                                           )
            testimonials_data.save()
            return JsonResponse("successfully registered!!",safe=False)

        except IntegrityError:
            return JsonResponse('user of this data is already exist!!',safe=False)


class Testimonials_List(APIView):
    def get(self,request):
        testimonials=Testimonials.objects.all()
        serializer=TestimonialsSerializer(testimonials,many=True)
        return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def UserDelete(request,id=0):
    try:
        if request.method=='DELETE':
            testimonials=Testimonials.objects.get(id=id)
            testimonials.delete()
            return JsonResponse('deleted successfully!!',safe=False)
    except Exception:
        return JsonResponse('Id not found!!',safe=False)



'''SPEAKERS'''
class Speakers_Register(APIView):
    def post(self,request):
        try:
            register_data=JSONParser().parse(request)
            speakers_data= Speakers.objects.create(
                                            name=register_data['name'],
                                            img_url=register_data['img_url'],
                                            link=register_data['link']
                                           )
            speakers_data.save()
            return JsonResponse("successfully registered!!",safe=False)

        except IntegrityError:
            return JsonResponse('user of this data is already exist!!',safe=False)


class Speakers_List(APIView):
    def get(self,request):
        speakers=Speakers.objects.all()
        serializer=SpeakersSerializer(testimonials,many=True)
        return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def UserDelete(request,id=0):
    try:
        if request.method=='DELETE':
            speakers=Speakers.objects.get(id=id)
            speakers.delete()
            return JsonResponse('deleted successfully!!',safe=False)
    except Exception:
        return JsonResponse('Id not found!!',safe=False)
      

    


