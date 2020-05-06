# Generated by Django 2.1.5 on 2020-05-05 05:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cross',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('isdelete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('content', models.CharField(max_length=4000, verbose_name='内容')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cross', models.ManyToManyField(related_name='cross', to='zcr_joke.Cross')),
            ],
        ),
        migrations.CreateModel(
            name='HotCross',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('isdelete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('content', models.CharField(max_length=4000, verbose_name='内容')),
                ('istop', models.BooleanField(default=False, verbose_name='是否置顶')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PicturesCross',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('isdelete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('content', models.CharField(max_length=400, verbose_name='内容')),
                ('cover', models.ImageField(upload_to='banner/%Y/%m/%d', verbose_name='图片')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='hotcross',
            field=models.ManyToManyField(related_name='hotcross', to='zcr_joke.HotCross'),
        ),
        migrations.AddField(
            model_name='goods',
            name='picturescross',
            field=models.ManyToManyField(related_name='picturescross', to='zcr_joke.PicturesCross'),
        ),
        migrations.AddField(
            model_name='goods',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]