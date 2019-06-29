from django.contrib import admin
from .models import TutorApply, TutorRequest, TutorComment, TuteeComment
# Register your models here.
admin.site.register(TutorApply)
admin.site.register(TutorRequest)
admin.site.register(TutorComment)
admin.site.register(TuteeComment)
