from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Book, LendPeriods, Isbn

admin.site.register(Book)
admin.site.register(LendPeriods)
admin.site.register(Isbn)