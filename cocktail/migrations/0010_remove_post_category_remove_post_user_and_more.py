# Generated by Django 4.1 on 2022-10-15 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocktail', '0009_alter_cocktail_bookmark_alter_cocktail_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.RenameField(
            model_name='cocktail',
            old_name='category',
            new_name='cocktail_category',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
