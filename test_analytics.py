import unittest
from analytics import summarize
class Tests(unittest.TestCase):
    def test_metrics(self):
        self.assertEqual(summarize([{'hours':24,'category':'access'},{'hours':26,'category':'access'}]),{'count':2,'average_hours':25,'sla_breaches':1,'categories':{'access':2}})
    def test_empty(self):
        self.assertIsNone(summarize([])['average_hours'])
    def test_invalid(self):
        with self.assertRaises(ValueError): summarize([{'hours':-1,'category':'access'}])
