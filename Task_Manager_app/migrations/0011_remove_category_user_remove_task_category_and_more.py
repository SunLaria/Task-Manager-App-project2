# Generated by Django 4.2.7 on 2024-01-22 21:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Task_Manager_app', '0010_remove_category_user_category_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='User',
        ),
        migrations.RemoveField(
            model_name='task',
            name='Category',
        ),
        migrations.AddField(
            model_name='category',
            name='User',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='Category',
            field=models.ManyToManyField(to='Task_Manager_app.category'),
        ),
    ]
