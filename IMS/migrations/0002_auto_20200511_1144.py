# Generated by Django 3.0.5 on 2020-05-11 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMS', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='belowcontent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_contentname', models.CharField(max_length=100)),
                ('b_contentdesc', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='insurance_list',
            name='Insurance_img',
            field=models.ImageField(upload_to='policyimage'),
        ),
    ]
