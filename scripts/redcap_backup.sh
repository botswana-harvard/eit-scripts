#!/bin/bash 

cd /home/django/source/bhp074_data_management/scripts && . /home/django/.virtualenvs/django_1.6.5/bin/activate && python export_records.py && mv export_* /home/django/eit_db_archives/
