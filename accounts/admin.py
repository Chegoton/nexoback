from django.contrib import admin
from .models import SatisfactionSurvey, Recognition, Kaizen, CustomUser

admin.site.register(SatisfactionSurvey)
admin.site.register(Recognition)
admin.site.register(Kaizen)
admin.site.register(CustomUser)
