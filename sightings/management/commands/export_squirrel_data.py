from django.core.management.base import BaseCommand, CommandError
from sightings.models import Squirrel
import os
import csv
from datetime import datetime
# pylint: disable=no-member

class Command(BaseCommand):
    help = 'Help to export to csv'
    def add_arguments(self, parser):
        parser.add_argument('file_path', nargs='?', type=str)
    def handle(self, *args, **options):
        meta = Squirrel._meta
        field_names = [f.name for f in meta.fields]
        with open(options['file_path'], 'w', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(field_names)
            for obj in Squirrel.objects.all():
                    # print(field)
                    # print(getattr(obj, field))
                row = [getattr(obj, field) for field in field_names]
                print(row)
                writer.writerow(row)