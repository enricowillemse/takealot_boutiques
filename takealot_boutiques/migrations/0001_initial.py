# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-22 13:18
from __future__ import unicode_literals

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
            name='Products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_id', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('active', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('cost_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('images', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserOrders',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='takealot_boutiques.Products')),
                ('user_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProducts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='takealot_boutiques.Products')),
                ('user_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]