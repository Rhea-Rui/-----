# Generated by Django 2.1.5 on 2020-05-05 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zcr_joke', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tread_cross', models.ManyToManyField(related_name='Tread_cross', to='zcr_joke.Cross')),
                ('Tread_hotcross', models.ManyToManyField(related_name='Tread_hotcross', to='zcr_joke.HotCross')),
                ('Tread_picturescross', models.ManyToManyField(related_name='Tread_picturescross', to='zcr_joke.PicturesCross')),
                ('Tread_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]