from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from django.urls import reverse


# Create your models here.
gender = (("F","femme"),("H","homme"))

class utilisateur (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    adresse = models.CharField(max_length=100)
    sexe = models.CharField(choices=gender, max_length=100)
    date_naissance = models.DateField()
    num_tel = models.CharField(max_length=15)



class Categorie(models.Model):
   name = models.CharField(max_length=100,db_index=True)
   slug = models.SlugField(max_length=200,
                           db_index=True,
                           unique=True)

   class Meta:
       ordering = ('name',)
       verbose_name = 'category'
       verbose_name_plural = 'categories'

   def __str__(self):
       return self.name

   def get_absolute_url(self):
       return reverse('shop:product_list_by_category',
                      args=[self.slug])

class product(models.Model):
      name = models.CharField(max_length=120)
      description = models.TextField()
      price = models.DecimalField(decimal_places=2, max_digits=20, null=True)
      stock = models.DecimalField(decimal_places=2, max_digits=20, null=True)
      dateAjout = models.DateField(("Date"), default=datetime.now())
      image = models.ImageField(upload_to="product/", null=True, blank=True)
      slug = models.SlugField(max_length=200, db_index=True)
      available = models.BooleanField(default=True)
      categorie = models.ForeignKey(Categorie, related_name="product",on_delete="")

      class Meta:
          ordering = ('name',)
          index_together = (('id', 'slug'),)

      def __str__(self):
          return self.name

      def get_absolute_url(self):
          return reverse('shop:product_detail',
                         args=[self.id, self.slug])


      def __str__(self):
          return self.name


class service(models.Model):
  name_person = models.CharField(max_length=100)
  discription_service= models.TextField()


