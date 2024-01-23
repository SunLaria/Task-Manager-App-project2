# Generated by Django 4.2.7 on 2024-01-21 19:57

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
                ('Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Date', models.DateField()),
                ('Tag', models.CharField(choices=[('high-priority', 'High Priority'), ('medium-priority', 'Medium Priority'), ('low-priority', 'Low Priority'), ('no-priority', 'No Priority')], default='no-priority', max_length=16)),
                ('Description', models.TextField()),
                ('Created_at', models.DateField(auto_now_add=True)),
                ('Updated_at', models.DateField(auto_now=True)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Task_Manager_app.category')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]