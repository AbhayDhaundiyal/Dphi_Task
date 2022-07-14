# Generated by Django 4.0.6 on 2022-07-14 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Educator',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.TextField()),
                ('Password', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.TextField()),
                ('Password', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='course',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.TextField()),
                ('Desc', models.TextField()),
                ('content', models.TextField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dash.educator')),
                ('enrolled', models.ManyToManyField(to='dash.student')),
            ],
        ),
    ]
