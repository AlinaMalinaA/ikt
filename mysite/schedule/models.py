# ! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import smart_str



class Class(models.Model):


    title = models.CharField(max_length=200)
    # day_number_with0 = models.IntegerField()
    # time = models.TimeField()
    # week = models.CharField(max_length=20)
    # teacher = models.CharField(max_length=200)
    # place = models.CharField(max_length=200)
    homework = models.CharField(max_length=1000)



    def publish(self):
        self.save()

    def __str__(self):
        # title = self.get_unicode(self.title)
        # day = self.get_unicode(str(self.day_number_with0))
        # time = self.get_unicode(str(self.time))
        # week = self.get_unicode(self.week)
        # teacher = self.get_unicode(self.teacher)
        # place = self.get_unicode(self.place)
        # homework = self.get_unicode(self.homework)

        # return title + " " + day + " " + time + " " + week + " " + teacher + " " + place + " " + homework
        # string = u' '.join((str(self.time), str(self.day_number_with0), str(self.time), self.week, self.teacher, self.place, self.homework)).encode('utf-8').strip()

        # homework = str(self.homework.encode('CP866'))
        return ""
        # return self.title + " " + str(self.day_number_with0) + " " + str(self.time) + " " + self.week + " " +\
        #             self.teacher + " " + self.place + " " + self.homework
