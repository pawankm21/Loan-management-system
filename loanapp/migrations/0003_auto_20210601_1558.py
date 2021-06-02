# Generated by Django 3.2.3 on 2021-06-01 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loanapp', '0002_rename_on_date_approved_loan_on_date_issued'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='on_date_approved',
        ),
        migrations.AddField(
            model_name='loan',
            name='on_date_issued',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
