# Generated by Django 3.1 on 2020-08-06 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_item', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('calories', models.IntegerField()),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]