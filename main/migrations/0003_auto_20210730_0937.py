# Generated by Django 3.2.5 on 2021-07-30 04:37

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_m_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='m_category',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='m_sprmenu',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='m_Trening',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='category/%Y/%m/%d')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='Порядок')),
                ('cansw', models.BooleanField(default=True, verbose_name='Отображать')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='main.m_category')),
            ],
            options={
                'verbose_name': 'Тренинг',
                'verbose_name_plural': 'Тренинги',
                'ordering': ['order'],
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
