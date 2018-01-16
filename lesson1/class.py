#!/usr/bin/env python
# coding: utf-8

class Persion(object):
  def __init__(self, name = None, age = None):
    self.name = name;
    self.age = age;
  def eat(self):
    print 'eat food';

Persion.sex = None;

onePersion = Persion('小明', '24');
# onePersion.sex = 'male';

print onePersion.sex;

onePersion.eat();

######## split line ###########

import types;

def run(self, speed):
  print 'Keeping moving, the speed is %d km/h' %speed;

Persion.run = types.MethodType(run, None, Persion);

onePersion.run(100);


def testName(self):
  print self.name;

onePersion.testName = types.MethodType(testName, onePersion); #, Persion

onePersion.testName();