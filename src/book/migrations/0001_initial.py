# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-26 12:10
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('total_no', models.IntegerField()),
                ('available_no', models.IntegerField()),
                ('page_amount', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Isbn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=50)),
                ('lend_from', models.DateField(blank=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Book')),
            ],
        ),
        migrations.CreateModel(
            name='LendPeriods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('days_amount', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Lending period',
                'get_latest_by': 'days_amount',
                'verbose_name_plural': 'Lending periods',
                'ordering': ['days_amount'],
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('course', models.CharField(choices=[('BTECH', 'B_Tech'), ('MTECH', 'M_Tech'), ('MBA', 'MBA')], max_length=5)),
                ('year', models.IntegerField(validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(1)])),
                ('branch', models.CharField(choices=[('CO', 'Computer_Engineering'), ('EE', 'Electrical_Engineering'), ('EC', 'Elecltronic_and_Communication_Engineering'), ('CE', 'Civil_Engineering'), ('ME', 'Mechanical_Engineering')], max_length=2)),
                ('roll_no', models.IntegerField(validators=[django.core.validators.MaxValueValidator(150), django.core.validators.MinValueValidator(1)])),
                ('mobile', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.EmailField(blank=True, max_length=30, null=True)),
                ('join_date', models.DateField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User profile',
                'get_latest_by': 'join_date',
                'verbose_name_plural': 'User profiles',
                'ordering': ['user'],
            },
        ),
        migrations.AddField(
            model_name='isbn',
            name='lend_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='book.UserProfile'),
        ),
        migrations.AddField(
            model_name='book',
            name='lend_period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.LendPeriods'),
        ),
    ]