# Generated by Django 3.0.5 on 2020-04-22 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='lancamentoConta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.IntegerField()),
                ('vencimento', models.DateField()),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
