# Generated by Django 2.2.7 on 2019-12-08 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('squirrelid', models.CharField(help_text='Unique Squirrel ID', max_length=255)),
                ('longitude', models.DecimalField(decimal_places=30, help_text='longitude', max_digits=50)),
                ('latitude', models.DecimalField(decimal_places=30, help_text='latitude', max_digits=50)),
                ('shifts', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], default=None, help_text='shifts', max_length=255)),
                ('date', models.DateField(help_text='shifts')),
                ('age', models.CharField(choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], default=None, help_text='age', max_length=255)),
                ('color', models.CharField(choices=[('Gray', 'Gray'), ('Cinnamon', 'Cinnamon'), ('Black', 'Black')], default=None, help_text='Primary Fur Color', max_length=255)),
                ('location', models.CharField(choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground')], default=None, help_text='Location', max_length=255)),
                ('specific_location', models.CharField(help_text='Specific Location', max_length=255)),
                ('running', models.BooleanField(default=False, help_text='Running')),
                ('chasing', models.BooleanField(default=False, help_text='Chasing')),
                ('climbing', models.BooleanField(default=False, help_text='Climbing')),
                ('eating', models.BooleanField(default=False, help_text='Eating')),
                ('foraging', models.BooleanField(default=False, help_text='Foraging')),
                ('other_activities', models.CharField(help_text='Other activities', max_length=255)),
                ('kuks', models.BooleanField(default=False, help_text='Kuks')),
                ('quaas', models.BooleanField(default=False, help_text='Quaas')),
                ('moans', models.BooleanField(default=False, help_text='Moans')),
                ('tail_flags', models.BooleanField(default=False, help_text='Tail flags')),
                ('tail_twitches', models.BooleanField(default=False, help_text='Tail twitches')),
                ('approaches', models.BooleanField(default=False, help_text='Approaches')),
                ('indifferent', models.BooleanField(default=False, help_text='indifferent')),
                ('runs_from', models.BooleanField(default=False, help_text='Runs from')),
            ],
        ),
    ]
