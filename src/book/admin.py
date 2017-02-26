from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Book, LendPeriods, Isbn, UserProfile

admin.site.register(Book)
admin.site.register(LendPeriods)
admin.site.register(Isbn)
admin.site.register(UserProfile)