# Generated by Django 2.1.5 on 2019-02-27 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('batchrecords', '0002_auto_20190226_1939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalbatchrecord',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='historicalbatchrecord',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalbatchrecord',
            name='product',
        ),
        migrations.RemoveField(
            model_name='historicalbatchrecord',
            name='updated_by',
        ),
        migrations.DeleteModel(
            name='HistoricalBatchRecord',
        ),
    ]
