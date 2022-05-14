# Generated by Django 4.0.4 on 2022-05-13 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greenthumb', '0003_alter_houseplant_options_alter_user_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='houseplant',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default='2022-05-09T20:06:44Z'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='houseplant',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='pref_day1',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='pref_day2',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_img',
            field=models.CharField(blank=True, default='', max_length=512),
        ),
    ]