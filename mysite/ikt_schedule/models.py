# ! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models



class Class(models.Model):
    RELEVANCE_CHOICES = (
        (1, u'МУЛЬТИМЕДИЙНЫЕ ТЕХНОЛОГИИ'),
        (2, u'ОБЛАЧНЫЕ ТЕХНОЛОГИИ И УСЛУГИ'),
        (3, u'СОЗДАНИЕ КЛИЕНТ-СЕРВЕРНЫХ ПРИЛОЖЕНИЙ '),
        (4, u'МЕТРОЛОГИЯ И ТРЕБОВАНИЯ СТАНДАРТИЗАЦИИ В ИНФОКОММУНИКАЦИОННЫХ СИСТЕМАХ'),
        (5, u'СОЗДАНИЕ ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ ИНФОКОММУНИКАЦИОННЫХ СИСТЕМ'),
        (6, u'Планирование развития сервисов и услуг связи на базе инфокоммуникационных технологий'),
        (7, u'ОСНОВЫ ПОСТРОЕНИЯ ИНФОКОММУНИКАЦИОННЫХ СИСТЕМ И СЕТЕЙ'),
        (8, u'АДМИНИСТРИРОВАНИЕ OC '),
        (9, u'АДМИНИСТРИРОВАНИЕ СЕТЕЙ WINDOWS'),
    )


    # title = models.CharField(max_length=200)
    day_number_with0 = models.IntegerField()
    time = models.TimeField()
    week = models.CharField(max_length=20)
    teacher = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    homework = models.CharField(max_length=1000)
    subject = models.IntegerField(choices=RELEVANCE_CHOICES, default=1)



    def publish(self):
        self.save()

    def __str__(self):
        # title = self.get_unicode(self.title)
        day = self.get_unicode(str(self.day_number_with0))
        time = self.get_unicode(str(self.time))
        week = self.get_unicode(self.week)
        teacher = self.get_unicode(self.teacher)
        place = self.get_unicode(self.place)
        homework = self.get_unicode(self.homework)

        # return title + " " + day + " " + time + " " + week + " " + teacher + " " + place + " " + homework
        string = u' '.join((str(self.subject), str(self.day_number_with0), str(self.time), self.week, self.teacher, self.place, self.homework)).encode('utf-8').strip()
        print string
        return string
        # return self.title + " " + str(self.day_number_with0) + " " + str(self.time) + " " + self.week + " " +\
        #             self.teacher + " " + self.place + " " + self.homework

    def get_unicode(self, non_unicode_string):
        string = "%r" % non_unicode_string
        string = string.encode('cp1251')
        string = string.encode('latin1').decode('cp1251')
        return string