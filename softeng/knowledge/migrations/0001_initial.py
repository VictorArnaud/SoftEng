# Generated by Django 2.0.6 on 2018-06-24 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('curriculum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Knowledge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('slug', models.SlugField(help_text='URL string shortcut', verbose_name='Shortcut')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('core_content', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='knowledges', to='curriculum.CoreContent')),
            ],
            options={
                'verbose_name_plural': 'Knowledges',
                'ordering': ['title'],
                'verbose_name': 'Knowledge',
            },
        ),
        migrations.CreateModel(
            name='Subtopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('slug', models.SlugField(help_text='URL string shortcut', verbose_name='Shortcut')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
            options={
                'verbose_name_plural': 'Subtopics',
                'ordering': ['title'],
                'verbose_name': 'Subtopic',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('slug', models.SlugField(help_text='URL string shortcut', verbose_name='Shortcut')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('knowledge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='knowledge.Knowledge')),
            ],
            options={
                'verbose_name_plural': 'Topics',
                'ordering': ['title'],
                'verbose_name': 'Topic',
            },
        ),
        migrations.AddField(
            model_name='subtopic',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtopics', to='knowledge.Topic'),
        ),
    ]
