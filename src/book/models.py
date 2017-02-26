from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Book(models.Model):
    """
    An Book class - to describe book in the system.
    """
    book_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    publisher = models.ForeignKey('Publisher')
    author = models.ForeignKey('Author')
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


