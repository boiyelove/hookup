# Generated by Django 2.0.6 on 2018-08-12 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matchmaker', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='interests',
            field=models.ManyToManyField(related_name='interest_list', to='matchmaker.Interest'),
        ),
    ]
