from django.db import models


# Create your models here.
class Movie(models.Model):
    """Model representing a movie

    Args:
        models (Model): used to specify data type of fields for model
    """
    title = models.CharField()
    description = models.CharField()
    release_date = models.DateTimeField("release date")
    duration = models.DurationField()


class Seat(models.Model):
    """Model representing a seat

    Args:
        models (Model): used to specify data type of fields for model
    """
    seat_number = models.IntegerField()
    booking_status = models.BooleanField()


class Booking(models.Model):
    """Model representing a booking

    Args:
        models (Model): used to specify data type of fields for model
    """
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    booking_date = models.DateTimeField("booking date")
