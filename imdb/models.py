from django.db import models

# Create your models here.
class Movie_Data(models.Model):
	id= models.AutoField
	movie_title= models.CharField(max_length=100)
	movie_rating= models.DecimalField(max_digits=3, decimal_places=1)
	movie_release_date= models.DateField()
	movie_duration= models.IntegerField(default="0")
	movie_description= models.CharField(max_length=100)
	def __str__(self):
		return self.movie_title