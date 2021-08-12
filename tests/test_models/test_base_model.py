#!/usr/bin/python3
''' Unittest for BaseModel '''

import models
import unittest
from models.base_model import BaseModel
from datetime import datetime
import pep8


class TestBaseModel(unittest.TestCase):
    '''Test for BaseModel'''

    def test_basemodel(self):
        '''  Test for BaseModel '''
        b1 = BaseModel()
        up = b1.updated_at
        b1.name = "Hi"
        b1.save()
        self.assertEqual(b1.name, "Hi")
        self.assertIn(b1, models.storage.all().values())
        self.assertEqual(datetime, type(b1.created_at))
        self.assertEqual(datetime, type(b1.updated_at))
        self.assertEqual(dict, type(b1.to_dict()))
        self.assertEqual(str, type(b1.id))
        prin = "[{}] ({}) {}".format(
            b1.__class__.__name__,
            b1.id,
            b1.__dict__
        )
        self.assertEqual(prin, str(b1))
        b1.save()
        self.assertNotEqual(up, b1.updated_at)
        b2 = BaseModel()
        b2.save()
        self.assertNotEqual(b2, models.storage.all())
        b2.name = "Aaa"
        dic = b2.to_dict()
        self.assertEqual('name' in dic, True)
        self.assertEqual(type(str(b1)), str)

    ''' Test for BaseModel Ex 3'''

    def test_basemodels(self):
        ''' Test for 2 classes BaseModel '''
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)
        self.assertNotEqual(b1.created_at, b2.created_at)
        self.assertNotEqual(b1.updated_at, b2.updated_at)

    def test_pep8_console(self):
        """test pep8 style"""
        s = pep8.StyleGuide(quiet=True)
        pep = s.check_files(['models/base_model.py'])
        self.assertEqual(pep.total_errors, 0, 'Found errors.')

if __name__ == '__main__':
    unittest.main()
