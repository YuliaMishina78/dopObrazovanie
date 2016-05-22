# -*- coding: utf-8 -*-
import unicodecsv
import csv
from itertools import islice
from dopObrazovanieApp.models import Site, Teacher
import os
from pandas import read_csv


def csv_to_bd():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(BASE_DIR, 'static\\myresult2.csv')
    sites = Site.objects.all()
    for site in sites:
        site.delete()

    teachers = Teacher.objects.all()
    for teacher in teachers:
        teacher.delete()

    #Open csv

    result_file = read_csv(path, sep='$', encoding='utf-8')
    site = Site()
    site.Url = 'http://www.spb.repetit.ru/'
    site.Correl = 0.735641
    site.save()

    for index, row in result_file.iterrows():
        teacher = Teacher()
        teacher.Url = row['urls']
        teacher.Name = row['names']
        teacher.Money = row['money']
        teacher.Subjects = row['subjects']
        teacher.Metro = row['metro']
        teacher.ComeHome = row['comehome']
        teacher.Status = row['status']
        teacher.Feedback = row['feedback']
        teacher.SkypeNames = row['skypeNames']
        teacher.RatingSum = row['ratingSum']
        teacher.Rating = row['rating']
        teacher.RatingDivSum = row['ratDivMon']
        teacher.FeedDivSum = row['feedDivMon']
        teacher.Funct = 0
        teacher.FromSite = site
        teacher.save()

