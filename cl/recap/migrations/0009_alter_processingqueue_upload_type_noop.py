# Generated by Django 3.2.16 on 2022-11-21 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recap', '0008_alter_nos_noop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacerhtmlfiles',
            name='upload_type',
            field=models.SmallIntegerField(choices=[(1, 'HTML Docket'), (2, 'HTML attachment page'), (3, 'PDF'), (4, 'Docket history report'), (5, 'Appellate HTML docket'), (6, 'Appellate HTML attachment page'), (7, 'Internet Archive XML docket'), (8, 'Case report (iquery.pl) page'), (9, 'Claims register page'), (10, 'Zip archive of RECAP Documents'), (11, 'Email in the SES storage format'), (12, 'Docket iQuery page')], help_text='The type of object that is uploaded'),
        ),
        migrations.AlterField(
            model_name='processingqueue',
            name='upload_type',
            field=models.SmallIntegerField(choices=[(1, 'HTML Docket'), (2, 'HTML attachment page'), (3, 'PDF'), (4, 'Docket history report'), (5, 'Appellate HTML docket'), (6, 'Appellate HTML attachment page'), (7, 'Internet Archive XML docket'), (8, 'Case report (iquery.pl) page'), (9, 'Claims register page'), (10, 'Zip archive of RECAP Documents'), (11, 'Email in the SES storage format'), (12, 'Docket iQuery page')], help_text='The type of object that is uploaded'),
        ),
    ]
