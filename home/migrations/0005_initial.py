# Generated by Django 4.2.4 on 2024-05-22 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0004_delete_category_delete_department_delete_entity_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Global', models.CharField(max_length=200)),
                ('Local', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HR_Department', models.CharField(max_length=200)),
                ('IT_Department', models.CharField(max_length=200)),
                ('Marketing_Department', models.CharField(max_length=200)),
                ('Finance_Department', models.CharField(max_length=200)),
                ('Business_Teams_Department', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FY',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='vision_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vision1', models.CharField(max_length=200)),
                ('vision2', models.CharField(max_length=200)),
                ('vision3', models.CharField(max_length=200)),
                ('vision4', models.CharField(max_length=200)),
                ('vision5', models.CharField(max_length=200)),
                ('vision6', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='visions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vision1', models.CharField(max_length=200)),
                ('vision2', models.CharField(max_length=200)),
                ('vision3', models.CharField(max_length=200)),
                ('vision4', models.CharField(max_length=200)),
                ('vision5', models.CharField(max_length=200)),
                ('vision6', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('East', models.CharField(max_length=20)),
                ('West', models.CharField(max_length=20)),
                ('North', models.CharField(max_length=20)),
                ('South', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.country')),
            ],
        ),
    ]
