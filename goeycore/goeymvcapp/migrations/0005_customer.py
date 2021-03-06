# Generated by Django 2.1.2 on 2018-12-20 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goeymvcapp', '0004_companyskills_companystats_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=8)),
                ('vpassword', models.CharField(max_length=8)),
                ('status', models.BooleanField(default=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
