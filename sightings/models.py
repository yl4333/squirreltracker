from django.db import models

class squirrel(models.Model):
    id = models.CharField(
        max_length=200,
        primary_key=True,
        help_text="Unique Squirrel ID",
    )

    longtitude = models.DecimalField(
        max_digits=50,
        decimal_places=30,
        help_text="longtitude",
    )

    latitude = models.DecimalField(
        max_digits=50,
        decimal_places=30,
        help_text="latitude",
    )

    AM = "am"
    PM = "pm"
    SHIFTS = [
        (AM, "am"),
        (PM, "pm"),
    ]

    shifts = models.CharField(
        max_length=200,
        choices=SHIFTS,
        default=None,
        help_text="shifts"
    )

    date = models.DateField(
        help_text="shifts"
    )

    ADULT = "Adult"
    JUVENILE = "Juvenile"

    AGE = [
        (ADULT, "Adult"),
        (JUVENILE, "Juvenile"),
    ]

    age = models.CharField(
        max_length=200,
        choices=AGE,
        default=None,
        help_text="age"
    )