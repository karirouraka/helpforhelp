from django.contrib import admin
from tutor_account.models import UserProfile, Reference, Help, Speciality, Subject

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    pass

class ReferenceAdmin(admin.ModelAdmin):
    pass

class HelpAdmin(admin.ModelAdmin):
    pass

class SpecialityAdmin(admin.ModelAdmin):
    pass

class SubjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Reference, ReferenceAdmin)
admin.site.register(Help, HelpAdmin)
admin.site.register(Speciality, SpecialityAdmin)
admin.site.register(Subject, SubjectAdmin)
