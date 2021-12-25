# Generated by Django 3.0.7 on 2021-11-09 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='phones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titles', models.CharField(max_length=150)),
                ('images', models.CharField(max_length=1000)),
                ('prices', models.CharField(max_length=150)),
                ('discounts', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Shopify mobiles',
            },
        ),
    ]
