# Generated by Django 2.1.2 on 2018-11-07 10:14

from django.db import migrations, models

import gnosis.eth.django.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('address', gnosis.eth.django.models.EthereumAddressField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15)),
                ('code', models.CharField(max_length=5)),
                ('description', models.TextField(blank=True)),
                ('decimals', models.PositiveSmallIntegerField()),
                ('logo_uri', models.URLField(blank=True)),
                ('website_uri', models.URLField(blank=True)),
                ('gas_token', models.BooleanField(default=False)),
                ('fixed_eth_conversion', models.DecimalField(decimal_places=15, default=None, max_digits=25, null=True)),
            ],
        ),
    ]
