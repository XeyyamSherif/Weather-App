<<<<<<< HEAD
# Generated by Django 3.0.3 on 2020-03-01 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='added_cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=100)),
                ('added_time', models.DateField()),
            ],
        ),
    ]
=======
# Generated by Django 3.0.3 on 2020-03-01 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='added_cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=100)),
                ('added_time', models.DateField()),
            ],
        ),
    ]
>>>>>>> 2001d54b7f6aa08db2779480e425bd1c54579a2f
