# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-12-14 16:00
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('article_from', models.IntegerField(choices=[(0, '原创'), (1, '转载')], default=0, verbose_name='文章来源')),
                ('summary', models.TextField(verbose_name='摘要')),
                ('tags', models.CharField(blank=True, help_text='用逗号分隔', max_length=100, null=True, verbose_name='标签')),
                ('content', DjangoUeditor.models.UEditorField(default='', verbose_name='正文')),
                ('reading_num', models.IntegerField(default=0, verbose_name='阅读量')),
                ('is_top', models.BooleanField(default=False, verbose_name='是否置顶')),
                ('rank', models.IntegerField(default=0, verbose_name='排序')),
                ('status', models.IntegerField(choices=[(0, '发表'), (1, '草稿'), (2, '丢弃')], default=0, verbose_name='文章状态')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(blank=True, null=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='类型名称')),
                ('rank', models.IntegerField(default=0, verbose_name='排序')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(blank=True, null=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '文章类型',
                'verbose_name_plural': '文章类型',
                'ordering': ['rank', '-create_time'],
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='链接名')),
                ('url', models.URLField(max_length=40, verbose_name='链接地址')),
                ('rank', models.IntegerField(default=0, verbose_name='排序')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(blank=True, null=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '友情链接',
                'verbose_name_plural': '友情链接',
            },
        ),
    ]
