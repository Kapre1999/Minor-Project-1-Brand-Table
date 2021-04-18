# Generated by Django 2.1 on 2018-10-06 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20181006_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='bevereges',
            name='prod_id',
            field=models.IntegerField(default=0, unique=True),
        ),
        migrations.AddField(
            model_name='burger',
            name='prod_id',
            field=models.IntegerField(default=0, unique=True),
        ),
        migrations.AddField(
            model_name='chinese',
            name='prod_id',
            field=models.IntegerField(default=0, unique=True),
        ),
        migrations.AddField(
            model_name='combo',
            name='prod_id',
            field=models.IntegerField(default=0, unique=True),
        ),
        migrations.AddField(
            model_name='icecream',
            name='prod_id',
            field=models.IntegerField(default=0, unique=True),
        ),
        migrations.AddField(
            model_name='paratha',
            name='prod_id',
            field=models.IntegerField(default=0, unique=True),
        ),
        migrations.AddField(
            model_name='rice',
            name='prod_id',
            field=models.IntegerField(default=0, unique=True),
        ),
        migrations.AddField(
            model_name='rolls',
            name='prod_id',
            field=models.IntegerField(default=0, unique=True),
        ),
        migrations.AddField(
            model_name='sandwitch',
            name='prod_id',
            field=models.IntegerField(default=0, unique=True),
        ),
        migrations.AddField(
            model_name='snacks',
            name='prod_id',
            field=models.IntegerField(default=0, unique=True),
        ),
        migrations.AddField(
            model_name='southindian',
            name='prod_id',
            field=models.IntegerField(default=0, unique=True),
        ),
        migrations.AddField(
            model_name='thali',
            name='prod_id',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
