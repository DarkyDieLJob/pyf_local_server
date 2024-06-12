# Generated by Django 4.0.6 on 2024-06-12 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='precio_cantidad',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='articulo',
            name='precio_cantidad_efectivo',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='articulo',
            name='precio_efectivo',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='articulo',
            name='precio_final',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='articulo',
            name='stock',
            field=models.FloatField(default=1.0),
        ),
        migrations.AddField(
            model_name='articulo',
            name='trabajado',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='CodigoBarras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barras', models.IntegerField(default=0)),
                ('Articulo', models.ManyToManyField(to='inventario.articulo')),
            ],
        ),
    ]
