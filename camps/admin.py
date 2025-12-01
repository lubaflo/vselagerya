from django.contrib import admin
from .models import Camp, Program, ProgramShift, CampDocument


admin.site.register(Camp)
admin.site.register(Program)
admin.site.register(ProgramShift)
admin.site.register(CampDocument)
