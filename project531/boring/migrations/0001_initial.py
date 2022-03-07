# Generated by Django 2.2.27 on 2022-03-07 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('lift', models.CharField(choices=[('Squat', 'Squat'), ('Deadlift', 'Deadlift'), ('Overhead Press', 'Overhead Press'), ('Bench Press', 'Bench Press')], max_length=10)),
                ('weight', models.PositiveIntegerField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Cycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lift', models.CharField(choices=[('Squat', 'Squat'), ('Deadlift', 'Deadlift'), ('Overhead Press', 'Overhead Press'), ('Bench Press', 'Bench Press')], max_length=10)),
                ('weight', models.PositiveIntegerField()),
                ('date', models.DateField()),
                ('cycle', models.PositiveIntegerField()),
                ('tm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boring.Tm')),
            ],
        ),
    ]