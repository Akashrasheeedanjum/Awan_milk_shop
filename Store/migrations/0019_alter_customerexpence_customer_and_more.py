# Generated by Django 4.2.6 on 2023-10-15 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0018_alter_milksale_fat_alter_milksale_lr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerexpence',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store.employee'),
        ),
        migrations.AlterField(
            model_name='makepayment',
            name='milk_center',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store.employee'),
        ),
        migrations.AlterField(
            model_name='milkpurchase',
            name='milk_center',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store.employee'),
        ),
        migrations.AlterField(
            model_name='milksale',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store.employee'),
        ),
        migrations.AlterField(
            model_name='receivedpayment',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store.employee'),
        ),
    ]
