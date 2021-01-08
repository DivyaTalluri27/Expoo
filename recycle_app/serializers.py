from rest_framework import serializers
from recycle_app.models import Event
from recycle_app.models import Supportedby
from recycle_app.models import our_partner
from recycle_app.models import Association
from recycle_app.models import Media_Partner
from recycle_app.models import Testimonials
from recycle_app.models import Speakers



class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id',
                 'name',
                 'startDate',
                 'endDate',
                 'status',
                 'registrationCharge',
                 'registrationTax',
                 'registrationTotal',
                 'fileUpload',
                 'description'
                 )

class SupportedbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Supportedby
        fields = (
                 'nameofthecompany',
                 'imgurl'
                 )


class our_partnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = our_partner
        fields = (
                 'name',
                 'imgurl',
                 'link'
                 )

class AssociationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Association
        fields = (
                 'name',
                 'imgurl',
                 'link'
                 )

class Media_PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media_Partner
        fields = (
                 'name',
                 'imgurl',
                 'link'
                 )

class TestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        fields = (
                 'byname',
                 'img_url',
                 'vidio_url',
                 'comment',
                 )

class SpeakersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speakers
        fields = (
                 'name',
                 'designation',
                 'img_url',
                 'fb_link',
                 'twitter_link',
                 'description'
                 )
    
