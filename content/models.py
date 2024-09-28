from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    year= models.IntegerField()
    image= models.ImageField(upload_to="static/img")
    repository = models.URLField()
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return f"{self.name} - ({self.year})"
    
class Experience(models.Model):
    name = models.CharField(max_length=254)
    title = models.CharField(max_length=254)
    description = models.TextField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    xp_skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.title