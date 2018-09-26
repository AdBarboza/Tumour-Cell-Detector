# Generated by Django 2.1.1 on 2018-09-26 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tratamiento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObservacionTratamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('fk_tratamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tratamiento.Tratamiento')),
            ],
        ),
    ]
