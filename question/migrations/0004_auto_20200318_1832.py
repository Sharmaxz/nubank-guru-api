# Generated by Django 3.0.3 on 2020-03-18 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0003_auto_20200318_1745'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='título')),
                ('position', models.PositiveIntegerField(verbose_name='número da questão')),
                ('text', models.CharField(max_length=200, verbose_name='texto da questão')),
            ],
            options={
                'verbose_name': 'Questão',
                'verbose_name_plural': 'Questões',
            },
        ),
        migrations.RemoveField(
            model_name='answer',
            name='level',
        ),
        migrations.RemoveField(
            model_name='level',
            name='description',
        ),
        migrations.RemoveField(
            model_name='level',
            name='number',
        ),
        migrations.RemoveField(
            model_name='level',
            name='question_number',
        ),
        migrations.AddField(
            model_name='level',
            name='content',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='descrição'),
        ),
        migrations.AddField(
            model_name='level',
            name='position',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='número da fase'),
        ),
        migrations.AddField(
            model_name='level',
            name='title',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='título'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='question.Question', verbose_name='Respostas'),
        ),
    ]
