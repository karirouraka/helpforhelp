from django.contrib import admin
from help_system.models import *

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    pass

class ReferenceAdmin(admin.ModelAdmin):
    pass

class HelpAdmin(admin.ModelAdmin):
    pass

class HelpReceivedAdmin(admin.ModelAdmin):
    pass

class SpecialityAdmin(admin.ModelAdmin):
    pass

class SubjectAdmin(admin.ModelAdmin):
    pass

class HelpTimeAdmin(admin.ModelAdmin):
    pass

class HelpDateAdmin(admin.ModelAdmin):
    pass

class RecordAdmin(admin.ModelAdmin):
    pass

class TableAdmin(admin.ModelAdmin):
    pass




admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Reference, ReferenceAdmin)
admin.site.register(Help, HelpAdmin)
admin.site.register(Speciality, SpecialityAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(HelpReceived, HelpReceivedAdmin)
admin.site.register(HelpTime, HelpTimeAdmin)
admin.site.register(HelpDate, HelpDateAdmin)
admin.site.register(Record, RecordAdmin)
admin.site.register(Table, TableAdmin)