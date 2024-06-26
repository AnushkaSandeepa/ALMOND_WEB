# Generated by Django 3.2 on 2022-07-20 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Measurements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measure_id', models.TextField(max_length=14)),
                ('session_id', models.TextField(max_length=14)),
                ('X1', models.FloatField(null=True)),
                ('Y1', models.FloatField(null=True)),
                ('X2', models.FloatField(null=True)),
                ('Y2', models.FloatField(null=True)),
                ('place', models.TextField(max_length=30)),
                ('distance', models.TextField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='MeasureTemp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('click_id', models.TextField(max_length=14)),
                ('X1', models.FloatField(null=True)),
                ('Y1', models.FloatField(null=True)),
                ('X2', models.FloatField(null=True)),
                ('Y2', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ModelInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_id', models.TextField(max_length=14)),
                ('cloth_type', models.TextField(max_length=30)),
                ('sh_width', models.TextField(max_length=30)),
                ('chest', models.TextField(max_length=30)),
                ('length', models.TextField(max_length=30)),
                ('width', models.TextField(max_length=30)),
                ('sl_length', models.TextField(max_length=30)),
                ('nk_width', models.TextField(max_length=30)),
                ('c_rgb', models.TextField(max_length=30)),
                ('c_html', models.TextField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.TextField(max_length=14)),
                ('model_id', models.TextField(max_length=30)),
                ('date', models.TextField(max_length=8)),
                ('time', models.TextField(max_length=6)),
                ('invest_id', models.TextField(max_length=50)),
                ('investigator', models.TextField(max_length=50)),
                ('country', models.TextField(max_length=15)),
            ],
        ),
    ]
