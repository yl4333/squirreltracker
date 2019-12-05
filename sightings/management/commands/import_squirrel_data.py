from django.core.management.base import BaseCommand, CommandError
from sightings.models import Squirrel
import os
import csv
from datetime import datetime
# pylint: disable=no-member

class Command(BaseCommand):
    help = 'Use csv file to import squirrel data'
    def add_arguments(self, parser):
        parser.add_argument('file_path', nargs='?', type=str)

    def handle(self, *args, **options):
        with open(options['file_path'], 'r', encoding="utf8") as csvfile:
            csvreader = csv.DictReader(csvfile, delimiter=',')
            # print(csvreader.fieldnames)
            for row in csvreader:
                squirrels, created = Squirrel.objects.get_or_create(
                    squirrelid = row['Unique Squirrel ID'],
                    longtitude = row['X'],
                    latitude = row['Y'],
                    shifts = row['Shift'],
                    date = datetime.strptime(row['Date'], '%m%d%Y').date(),
                    age = row['Age'],
                    color = row['Primary Fur Color'],
                    location = row['Location'],
                    specific_location = row['Specific Location'],
                    running = (row['Running'].lower() == 'true'),
                    chasing = (row['Chasing'].lower() == 'true'),
                    climbing = (row['Climbing'].lower() == 'true'),
                    eating = (row['Eating'].lower() == 'true'),
                    foraging = (row['Foraging'].lower() == 'true'),
                    other_activities = row['Other Activities'],
                    kuks = (row['Kuks'].lower() == 'true'),
                    quaas = (row['Quaas'].lower() == 'true'),
                    moans = (row['Moans'].lower() == 'true'),
                    tail_flags = (row['Tail flags'].lower() == 'true'),
                    tail_twitches = (row['Tail twitches'].lower() == 'true'),
                    approaches = (row['Approaches'].lower() == 'true'),
                    indifferent = (row['Indifferent'].lower() == 'true'),
                )
                if created:
                    squirrels.save()
            