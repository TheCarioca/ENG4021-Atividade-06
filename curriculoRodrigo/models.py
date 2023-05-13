# Importando a biblioteca models do Django
from django.db import models

# Definindo a classe Category que herda da classe Model do Django
class Category(models.Model):
    # Definindo o campo title, do tipo CharField com tamanho máximo de 50 caracteres
    title = models.CharField(max_length=50)
    
    # Sobrescrevendo a função __str__ para retornar o título da categoria
    def __str__(self):
        return self.title

# Definindo a classe Task que herda da classe Model do Django
class Task(models.Model):
    # Definindo o campo title, do tipo CharField com tamanho máximo de 50 caracteres
    title = models.CharField(max_length=50)
    
    # Definindo o campo description, do tipo TextField
    description = models.TextField()
    
    # Definindo o campo due_date, do tipo DateField
    due_date = models.DateField()
    
    # Definindo o campo done, do tipo BooleanField
    done = models.BooleanField()
    
    # Definindo o campo category como uma chave estrangeira (ForeignKey) para a classe Category
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

# Definindo a classe University que herda da classe Model do Django
class University(models.Model):
    # Definindo o campo name, do tipo CharField com tamanho máximo de 50 caracteres
    name = models.CharField(max_length=50)
    
    # Definindo o campo rank, do tipo IntegerField
    rank = models.IntegerField()
    
    # Definindo o campo email, do tipo EmailField
    email = models.EmailField()
    
    # Definindo o campo description, do tipo TextField
    description = models.TextField()

# Definindo a classe Language que herda da classe Model do Django
class Language(models.Model):
    # Definindo uma tupla com opções de escolha de nível de proficiência em linguagem
    LANGUAGE_LEVEL = [
        ("A", "Basico"),
        ("B", "Avançado"),
        ("C", "Fluente"),
    ]
    # Definindo o campo title, do tipo CharField com tamanho máximo de 50 caracteres
    title = models.CharField(max_length=50)
    
    # Definindo o campo proficiency, do tipo CharField com tamanho máximo de 1 caractere, que recebe a tupla LANGUAGE_LEVEL
    proficiency = models.CharField(max_length=1, choices=LANGUAGE_LEVEL)
    
    # Definindo o campo description, do tipo TextField
    description = models.TextField()

# Definindo a classe Hability que herda da classe Model do Django
class Hability(models.Model):
    # Definindo o campo title, do tipo CharField com tamanho máximo de 50 caracteres
    title = models.CharField(max_length=50)
    
    # Definindo o campo level, do tipo CharField com tamanho máximo de 20 caracteres
    level = models.CharField(max_length=20)
