# Generated by Django 4.0.6 on 2022-07-18 22:39

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
            name='Password',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('passwrd', models.CharField(max_length=201)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passwrds', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]