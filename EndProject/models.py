from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name}'

class User(models.Model):
    username = models.EmailField( unique=True)
    password = models.CharField(max_length=15)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null = True, blank = True)
    role = models.CharField(choices=[('manager','manager'),('worker','worker')],default='worker')
    def __str__(self):
        return f'{self.username}'


class Task(models.Model):
    title = models.CharField(max_length=100)
    describe = models.CharField(max_length=1000)
    deadline = models.DateTimeField()
    myTeam = models.ForeignKey(Team, on_delete=models.CASCADE)
    status = models.CharField(choices=[('New','New'),('Process', 'Process'), ('Done', 'Done')], default='New')
    myDoner= models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}\n {self.describe}'




