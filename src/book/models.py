from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    """
    An Book class - to describe book in the system.
    """
    book_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    total_no = models.IntegerField()
    available_no = models.IntegerField()
    lend_period = models.ForeignKey('LendPeriods')
    page_amount = models.IntegerField()
    
    def __unicode__(self):
        return 'Book: ' + self.title
    
    class Meta:
        ordering = ['title']
        verbose_name = "Book"
        verbose_name_plural = "Books"

class Isbn(models.Model):
     isbn = models.CharField(max_length=50)
     book = models.ForeignKey(Book, on_delete=models.CASCADE)
     lend_by = models.ForeignKey('UserProfile', null=True, blank=True)
     lend_from = models.DateField(null=True, blank=True)



class LendPeriods(models.Model):
    """
    Users can borrow books from library for different
    time period. This class defines frequently-used
    lending periods.
    """
    name = models.CharField(max_length=50)
    days_amount = models.IntegerField()

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        get_latest_by = "days_amount"
        ordering = ['days_amount']
        verbose_name = "Lending period"
        verbose_name_plural = "Lending periods"


class UserProfile(models.Model):

    """
    Class provides more information according the system's users
     """
    user = models.OneToOneField(User)
    name = models.CharField(max_length=30, null=True, blank=True)
     
    Btech = 'BTECH'
    Mtech = 'MTECH'
    Mba = 'MBA'
    course_choices = (
         (Btech,'B_Tech'),
         (Mtech,'M_Tech'),
         (Mba,'MBA')
     )
    course = models.CharField(max_length=5,choices=course_choices)
 
    year = models.IntegerField(
         validators=[MaxValueValidator(4), MinValueValidator(1)]
      )
 
    computer = 'CO'
    electrical = 'EE'
    electronics = 'EC'
    civil = 'CE'
    mechanical = 'ME'
    branch_choices = (
        (computer,'Computer_Engineering'),
         (electrical,'Electrical_Engineering'),
         (electronics,'Elecltronic_and_Communication_Engineering'),
         (civil,'Civil_Engineering'),
         (mechanical,'Mechanical_Engineering') )
    branch = models.CharField(max_length=2,choices = branch_choices)
 
    roll_no = models.IntegerField(validators=[MaxValueValidator(150), MinValueValidator(1)])
    mobile = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(max_length=30, null=True, blank=True)
    join_date = models.DateField(auto_now_add=True)
 
    def __unicode__(self):
         return 'User profile: ' + self.user.username + ', ' + self.user.first_name + ' ' + self.user.last_name
 
    def gravator_url(self):
         return "http://www.gravatar.com/avatar/%s?s=50" % hashlib.md5(self.user.email).hexdigest()
 
    class Meta:
         get_latest_by = "join_date"
         ordering = ['user']
         verbose_name = "User profile"
         verbose_name_plural = "User profiles"
 
 
def get_or_create_userprofile(user):
     if user:
         # up = get_object_or_404(UserProfile, user=user)
         try:
             up = UserProfile.objects.get(user=user)
             if up:
                 return up
         except ObjectDoesNotExist:
             pass
     up = UserProfile(user=user, join_date=timezone.now())
     up.save()
     return up
 
 
User.profile = property(lambda u: get_or_create_userprofile(user=u))