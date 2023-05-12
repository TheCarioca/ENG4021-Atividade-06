from django.db import models

class Category(models.Model):
    title = models.CharField(max_length = 50)

    def __str__(self):
          return self.title
  
class Task(models.Model):
  title = models.CharField(max_length = 50)
  description = models.TextField()
  due_date = models.DateField()
  done = models.BooleanField()
  category = models.ForeignKey(Category, on_delete=models.CASCADE)

class University(models.Model):
  name = models.CharField(max_length = 50)
  rank = models.IntegerField()
  email = models.EmailField()
  description = models.TextField()

class Language(models.Model):
  LANGUAGE_LEVEL = [
        ("A", "Basico"),
        ("B", "Avançado"),
        ("C", "Fluente"),
    ]
  title = models.CharField(max_length = 50)
  proficiency = models.CharField(max_length=1, choices=LANGUAGE_LEVEL)
  description = models.TextField()

class Hability(models.Model):
  title = models.CharField(max_length = 50)
  level = models.CharField(max_length = 20)