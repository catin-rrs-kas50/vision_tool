from django.db import models

# Create your models here.
class Entity(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class FY(models.Model):
    year=models.IntegerField()

    def __str__(self):
        return self.FY
    
class visions(models.Model):
    vision1=models.CharField(max_length=200)
    vision2=models.CharField(max_length=200)
    vision3=models.CharField(max_length=200)
    vision4=models.CharField(max_length=200)
    vision5=models.CharField(max_length=200)
    vision6=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.visions
    

class category(models.Model):
    Global=models.CharField(max_length=200)
    Local=models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.Global


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.Country

    
class Zone(models.Model):
    East=models.CharField(max_length=20)
    West=models.CharField(max_length=20)
    North=models.CharField(max_length=20)
    South=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.Zone
    

class State(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Department(models.Model):
    HR_Department=models.CharField(max_length=200)
    IT_Department=models.CharField(max_length=200)
    Marketing_Department=models.CharField(max_length=200)
    Finance_Department=models.CharField(max_length=200)
    Business_Teams_Department=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.Department
    
class vision_Details(models.Model):
    vision1=models.CharField(max_length=200)
    vision2=models.CharField(max_length=200)
    vision3=models.CharField(max_length=200)
    vision4=models.CharField(max_length=200)
    vision5=models.CharField(max_length=200)
    vision6=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.vision_Details



