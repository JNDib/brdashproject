# Generated by Django 2.1.5 on 2019-02-27 01:39

import datetime
from django.db import migrations, models
import django.utils.timezone
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BatchRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lot', models.CharField(help_text='10 alphanumeric characters or less', max_length=10)),
                ('workorder', models.CharField(max_length=7)),
                ('manufacture_date', models.DateField(default=django.utils.timezone.now, help_text='YYYY-MM-DD')),
                ('expiration_date', models.DateField(help_text='YYYY-MM-DD')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('current_status', models.IntegerField(choices=[(1, 'Creation'), (2, 'Ready'), (3, 'In Production'), (4, 'Tier 1 Review'), (5, 'Tier 2 Review'), (6, 'Complete')], default=1)),
                ('status_changes', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='BatchRecordHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'Creation'), (2, 'Ready'), (3, 'In Production'), (4, 'Tier 1 Review'), (5, 'Tier 2 Review'), (6, 'Complete')])),
                ('timestamp_start', models.DateTimeField()),
                ('timestamp_end', models.DateTimeField()),
                ('duration', models.DurationField(default=datetime.timedelta(2))),
            ],
            options={
                'ordering': ('timestamp_start',),
            },
        ),
        migrations.CreateModel(
            name='HistoricalBatchRecord',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('lot', models.CharField(help_text='10 alphanumeric characters or less', max_length=10)),
                ('workorder', models.CharField(max_length=7)),
                ('manufacture_date', models.DateField(default=django.utils.timezone.now, help_text='YYYY-MM-DD')),
                ('expiration_date', models.DateField(help_text='YYYY-MM-DD')),
                ('created_at', models.DateTimeField(blank=True, editable=False)),
                ('updated_at', models.DateTimeField(blank=True, editable=False)),
                ('current_status', models.IntegerField(choices=[(1, 'Creation'), (2, 'Ready'), (3, 'In Production'), (4, 'Tier 1 Review'), (5, 'Tier 2 Review'), (6, 'Complete')], default=1)),
                ('status_changes', models.IntegerField(default=0)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'get_latest_by': 'history_date',
                'verbose_name': 'historical batch record',
                'ordering': ('-history_date', '-history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='part number')),
                ('description', models.CharField(max_length=30)),
                ('family', models.IntegerField(choices=[(1, 'red'), (2, 'white'), (3, 'blue')])),
                ('total_target_time', models.DurationField(default=datetime.timedelta(1))),
                ('target_duration_1', models.DurationField(default=datetime.timedelta(1))),
                ('target_duration_2', models.DurationField(default=datetime.timedelta(2))),
                ('target_duration_3', models.DurationField(default=datetime.timedelta(3))),
                ('target_duration_4', models.DurationField(default=datetime.timedelta(4))),
                ('target_duration_5', models.DurationField(default=datetime.timedelta(5))),
            ],
        ),
    ]
