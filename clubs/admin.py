from django.contrib import admin

# Register your models here.
from clubs.models import Club, Attribute, ClubAttribute, ClubPicture, ClubDay

admin.site.register(Club)
admin.site.register(Attribute)
admin.site.register(ClubAttribute)
admin.site.register(ClubPicture)
admin.site.register(ClubDay)
