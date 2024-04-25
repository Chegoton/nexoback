# Generated by Django 5.0.3 on 2024-04-23 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_recognition'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kaizen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField()),
                ('fullName', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('department', models.CharField(max_length=100)),
                ('target_date', models.DateField()),
                ('area_of_improvement', models.CharField(max_length=100)),
                ('expected_impact', models.TextField()),
                ('required_resources', models.TextField()),
                ('implementation_method', models.TextField()),
                ('evaluation_plan', models.TextField()),
            ],
        ),
    ]
