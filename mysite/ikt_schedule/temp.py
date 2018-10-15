#! /usr/bin/env python
# -*- coding: utf-8 -*-


source = 'проверка'
print type(source), source
s = "%r" % source
print type(s), s
s = s.encode('cp1251')
print type(s), s
s = s.encode('latin1')
print type(s), s
s = s.decode('cp1251')
print type(s), s
