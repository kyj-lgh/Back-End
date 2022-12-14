# Generated by Django 4.1 on 2022-09-04 10:26

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
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(blank=True, help_text='simple one-line text.', max_length=100, verbose_name='DESCRIPTION')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ingredient1', models.CharField(max_length=50, null=True)),
                ('Ingredient2', models.CharField(max_length=50, null=True)),
                ('Ingredient3', models.CharField(max_length=50, null=True)),
                ('Ingredient4', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='TITLE')),
                ('description', models.CharField(blank=True, help_text='simple one-line text.', max_length=100, verbose_name='DESCRIPTION')),
                ('content', models.TextField(verbose_name='CONTENT')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='CREATE DT')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='UPDATE DT')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cocktail.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('update_dt',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='CONTENT')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='CREATE DT')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='UPDATE DT')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cocktail.post')),
            ],
        ),
        migrations.CreateModel(
            name='Cocktail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='TITLE')),
                ('image', models.ImageField(blank=True, null=True, upload_to='cocktail/%Y/%m/', verbose_name='IMAGE')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='CREATE DT')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='UPDATE DT')),
                ('bookmark', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cocktail.category')),
                ('ingredient', models.ManyToManyField(to='cocktail.ingredient')),
            ],
            options={
                'ordering': ('update_dt',),
            },
        ),
    ]
