from django.db import models

class Squirrel(models.Model):
    squirrelid = models.CharField(
        max_length=255,
        help_text="Unique Squirrel ID",
    )

    longitude = models.DecimalField(
        max_digits=50,
        decimal_places=30,
        help_text="longitude",
    )

    latitude = models.DecimalField(
        max_digits=50,
        decimal_places=30,
        help_text="latitude",
    )

    AM = "AM"
    PM = "PM"
    SHIFTS_CHOICES = [
        (AM, "AM"),
        (PM, "PM"),
    ]

    shifts = models.CharField(
        max_length=255,
        choices=SHIFTS_CHOICES,
        default=None,
        help_text="shifts",
    )

    date = models.DateField(
        help_text="shifts",
    )

    ADULT = "Adult"
    JUVENILE = "Juvenile"

    AGE_CHOICES = [
        (ADULT, "Adult"),
        (JUVENILE, "Juvenile"),
    ]

    age = models.CharField(
        max_length=255,
        choices=AGE_CHOICES,
        default=None,
        help_text="age",
    )

    GRAY = "Gray"
    CINNAMON = "Cinnamon"
    BLACK = "Black"

    COLOR_CHOICES = [
        (GRAY, "Gray"),
        (CINNAMON, "Cinnamon"),
        (BLACK, "Black"),
    ]

    color = models.CharField(
        max_length=255,
        choices=COLOR_CHOICES,
        default=None,
        help_text="Primary Fur Color",
    )

    GROUND_PLANE = "Ground Plane"
    ABOVE_GROUND = "Above Ground"

    LOCATION_CHOICES = [
        (GROUND_PLANE, "Ground Plane"),
        (ABOVE_GROUND, "Above Ground"),
    ]

    location = models.CharField(
        max_length=255,
        choices=LOCATION_CHOICES,
        default=None,
        help_text="Location",
    )

    specific_location = models.CharField(
        max_length=255,
        help_text="Specific Location",
    )

    running = models.BooleanField(
        default=False,
        help_text="Running",
    )

    chasing = models.BooleanField(
        default=False,
        help_text="Chasing",
    )

    climbing = models.BooleanField(
        default=False,
        help_text="Climbing",
    )

    eating = models.BooleanField(
        default=False,
        help_text="Eating",
    )

    foraging = models.BooleanField(
        default=False,
        help_text="Foraging",
    )

    other_activities = models.CharField(
        max_length=255,
        help_text="Other activities",
    )

    kuks = models.BooleanField(
        default=False,
        help_text="Kuks",
    )

    quaas = models.BooleanField(
        default=False,
        help_text="Quaas",
    )

    moans = models.BooleanField(
        default=False,
        help_text="Moans",
    )

    tail_flags = models.BooleanField(
        default=False,
        help_text="Tail flags",
    )

    tail_twitches = models.BooleanField(
        default=False,
        help_text="Tail twitches",
    )

    approaches = models.BooleanField(
        default=False,
        help_text="Approaches",
    )

    indifferent = models.BooleanField(
        default=False,
        help_text="indifferent",
    )

    runs_from = models.BooleanField(
        default=False,
        help_text="Runs from",
    )

    def __str__(self):
        return "Squirrel" + self.squirrelid

