# Generated by Django 4.2.7 on 2024-07-18 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('v_core', '0002_animes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='animes',
            options={'verbose_name': 'animes', 'verbose_name_plural': 'animes'},
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mtitle', models.CharField(max_length=50)),
                ('mdescription', models.TextField(max_length=300)),
                ('mvideo', models.FileField(upload_to='video')),
                ('mimage', models.ImageField(upload_to='img/thumbnail')),
                ('mcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v_core.category')),
            ],
            options={
                'verbose_name': 'animes',
                'verbose_name_plural': 'animes',
            },
        ),
    ]