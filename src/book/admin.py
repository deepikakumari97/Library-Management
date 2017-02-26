from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Book, LendPeriods, Publisher, Author, UserProfile 

admin.site.Register(Book)
admin.site.Register(LendPeriods)
admin.site.Register(Publisher)
admin.site.Register(Author)
admin.site.Register(UserProfile)