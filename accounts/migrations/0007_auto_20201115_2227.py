# Generated by Django 3.0.8 on 2020-11-15 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_professor_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='id_number',
            field=models.IntegerField(max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='id_number',
            field=models.IntegerField(max_length=11, null=True),
        ),
    ]
