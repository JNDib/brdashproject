# Generated by Django 2.1.5 on 2019-02-27 01:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('batchrecords', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalbatchrecord',
            name='created_by',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalbatchrecord',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalbatchrecord',
            name='product',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='batchrecords.Product'),
        ),
        migrations.AddField(
            model_name='historicalbatchrecord',
            name='updated_by',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='batchrecordhistory',
            name='batchrecord',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='history', to='batchrecords.BatchRecord'),
        ),
        migrations.AddField(
            model_name='batchrecordhistory',
            name='updated_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='updatehistoryuser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='batchrecord',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='createuser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='batchrecord',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='batchrecords.Product'),
        ),
        migrations.AddField(
            model_name='batchrecord',
            name='updated_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='updateuser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='batchrecord',
            unique_together={('product', 'lot')},
        ),
    ]