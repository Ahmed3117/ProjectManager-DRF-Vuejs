from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='person_images/')

    def __str__(self):
        return self.name

class ToDo(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('done', 'Done'),
    ]

    body = models.TextField()
    end_date = models.DateField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default='pending')
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.body
