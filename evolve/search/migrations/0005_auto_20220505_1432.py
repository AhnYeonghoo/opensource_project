# Generated by Django 3.1.3 on 2022-05-05 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_auto_20220505_1129'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FirstBasicCulture',
            new_name='GaesinBasicCulture',
        ),
        migrations.RenameModel(
            old_name='FirstSemesterMajor',
            new_name='Lecture',
        ),
        migrations.DeleteModel(
            name='FirstGaesinBasicCulture',
        ),
        migrations.DeleteModel(
            name='FirstNaturalScience',
        ),
        migrations.DeleteModel(
            name='FirstSemesterSWMajor',
        ),
        migrations.DeleteModel(
            name='Ocu',
        ),
        migrations.DeleteModel(
            name='SecondBasicCulture',
        ),
        migrations.DeleteModel(
            name='SecondGaesinBasicCulture',
        ),
        migrations.DeleteModel(
            name='SecondNaturalScience',
        ),
        migrations.DeleteModel(
            name='SecondSemesterMajor',
        ),
        migrations.DeleteModel(
            name='SecondSemesterSWMajor',
        ),
    ]
