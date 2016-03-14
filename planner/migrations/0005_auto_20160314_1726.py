# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-14 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0004_remove_subject_sem_offered'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='grade',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='subject',
            name='area',
            field=models.CharField(choices=[('SE', 'software_engineering (SE)'), ('DBI', 'databases_and_information_systems (DBI)'), ('AIR', 'artificial_intelligence_and_robotics (AIR)'), ('CGV', 'computer_graphics_and_vision (CGV)'), ('CA', 'computer_architecture (CA)'), ('DNS', 'distributed_systems_networks_and_security (DNS)'), ('FMA', 'formal_methods_and_applications (FMA)'), ('ASC', 'algorithms_and_scientific_computing (ASC)'), ('OR', 'orientation (OR)'), ('IDP', 'interdisciplinary_project (IDP)'), ('SUPP', 'support_electives (SUPP)'), ('SEM', 'master_seminar (SEM)'), ('PRAC', 'master_practical (PRAC)')], max_length=4),
        ),
        migrations.AlterField(
            model_name='subject',
            name='sem_taken',
            field=models.CharField(blank=True, choices=[('', '---'), ('WS2015', 'WS 2015'), ('SS2016', 'SS 2016'), ('WS2016', 'WS 2016'), ('SS2017', 'SS 2017')], max_length=6),
        ),
    ]