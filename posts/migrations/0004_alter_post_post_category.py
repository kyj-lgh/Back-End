# Generated by Django 4.1 on 2022-10-15 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_rename_user_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='posts.category'),
        ),
    ]
