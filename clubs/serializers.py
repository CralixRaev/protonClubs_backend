from rest_framework.serializers import ModelSerializer

from clubs.models import Club, ClubAttribute, Attribute, ClubDay, ClubPicture


class AttributeSerializer(ModelSerializer):
    class Meta:
        model = Attribute
        fields = "__all__"


class ClubAttributeSerializer(ModelSerializer):
    attribute = AttributeSerializer(source="attribute_id")
    
    class Meta:
        model = ClubAttribute
        fields = ['value', 'attribute']


class ClubDaySerializer(ModelSerializer):
    class Meta:
        model = ClubDay
        fields = ['day', 'start_time', 'end_time']


class ClubPictureSerializer(ModelSerializer):
    class Meta:
        model = ClubPicture
        fields = ["image"]


class ClubSerializer(ModelSerializer):
    attributes = ClubAttributeSerializer(source='clubattribute_set', many=True)
    days = ClubDaySerializer(source='clubday_set', many=True)
    pictures = ClubPictureSerializer(source="clubpicture_set", many=True)

    class Meta:
        model = Club
        fields = ['id', 'name', 'mosru_link', 'attributes', 'days', 'pictures', 'description', 'price']
