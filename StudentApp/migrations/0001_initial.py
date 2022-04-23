# Generated by Django 4.0.1 on 2022-04-21 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_Us',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=55)),
                ('Email', models.EmailField(max_length=50)),
                ('Description', models.TextField(max_length=600)),
            ],
            options={
                'db_table': 'Contact_Us',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('About', models.CharField(max_length=500)),
                ('Date', models.DateTimeField()),
                ('Event_Pic', models.ImageField(upload_to='media/Event/')),
            ],
            options={
                'db_table': 'Event',
            },
        ),
        migrations.CreateModel(
            name='Notis',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('About', models.CharField(max_length=50)),
                ('Discription', models.TextField(max_length=2000)),
            ],
            options={
                'db_table': 'Notis',
            },
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
                ('Class', models.IntegerField(max_length=10)),
                ('Gender', models.CharField(max_length=10)),
                ('Father_Name', models.CharField(max_length=50)),
                ('Father_Nid', models.CharField(max_length=50)),
                ('Mother_Name', models.CharField(max_length=50)),
                ('Mother_Nid', models.CharField(max_length=50)),
                ('Present_Address', models.TextField(max_length=250)),
                ('Permanent_Address', models.TextField(max_length=250)),
                ('Contact', models.CharField(max_length=11, unique=True)),
                ('Student_Picture', models.ImageField(upload_to='media/Registration/')),
                ('Email', models.EmailField(max_length=50)),
            ],
            options={
                'db_table': 'Registration',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('About', models.CharField(max_length=50)),
                ('File', models.TextField(max_length=200)),
            ],
            options={
                'db_table': 'Result',
            },
        ),
        migrations.CreateModel(
            name='StudentDB',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
                ('Department', models.CharField(max_length=60)),
                ('Semester', models.CharField(max_length=50)),
                ('Roll', models.IntegerField(max_length=10, unique=True)),
                ('Section', models.CharField(max_length=5)),
                ('Gender', models.CharField(max_length=10)),
                ('Father_Name', models.CharField(max_length=50)),
                ('Mother_Name', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=200)),
                ('Contact', models.CharField(max_length=11, unique=True)),
                ('Picture', models.ImageField(upload_to='media/upload/')),
            ],
            options={
                'db_table': 'StudentDB',
            },
        ),
        migrations.CreateModel(
            name='User_Info',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Image', models.ImageField(upload_to='media/user/')),
            ],
            options={
                'db_table': 'User_Info',
            },
        ),
    ]