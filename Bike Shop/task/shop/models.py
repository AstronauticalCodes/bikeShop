from django.db import models

# write your models here


class Frame(models.Model):
    color = models.CharField(max_length=100)
    quantity = models.IntegerField()


class Seat(models.Model):
    color = models.CharField(max_length=100)
    quantity = models.IntegerField()


class Tire(models.Model):
    type = models.CharField(max_length=100)
    quantity = models.IntegerField()


class Basket(models.Model):
    quantity = models.IntegerField()


class Bike(models.Model):
    frame = models.ForeignKey(Frame, on_delete=models.DO_NOTHING)
    tire = models.ForeignKey(Tire, on_delete=models.DO_NOTHING)
    seat = models.ForeignKey(Seat, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    description = models.TextField()
    has_basket = models.BooleanField()

    def __str__(self):
        return f'{self.name} (with basket)' if self.has_basket else self.name


class Order(models.Model):
    STATUS_OPTIONS = [
        ('P', 'pending'),
        ('R', 'ready')
    ]

    bike = models.ForeignKey(Bike, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    status = models.CharField(max_length=1, choices=STATUS_OPTIONS)