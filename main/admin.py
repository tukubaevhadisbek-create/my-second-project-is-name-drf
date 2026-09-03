from django.contrib import admin
from .models import Employer,Category,Vacancy,Applicant,Resume

admin.site.register(Employer)
admin.site.register(Category)
admin.site.register(Vacancy)
admin.site.register(Applicant)
admin.site.register(Resume)

