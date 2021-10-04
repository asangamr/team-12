import sys
sys.path.append(".")
import unittest
import fileinput
import hw2

class TestGedcom(unittest.TestCase):

    def test_read(self):
        i=0
        for line in fileinput.input(files ='/Users/anj/Desktop/My-Family.txt'):
            self.assertEqual(project.lIne[i], line)
            i=i+1

    def test_isupper(self):
        i=0
        for line in fileinput.input(files ='/Users/anj/Desktop/My-Family.txt'):
            self.assertTrue(project.lIne[i].isupper)
            #self.assertFalse('Foo'.isupper())

    def test_split(self):
        i=0
        for line in fileinput.input(files ='/Users/anj/Desktop/My-Family.txt'):
            #self.assertEqual(s.split(), ['hello', 'world'])
            self.assertEqual(project.lIne[i].split(),line.split())
        # check that line.split fails when the separator is not a string
            with self.assertRaises(TypeError):
                line.split(2)
            i=i+1
    def test_raises(self):
        i=0
        for line in fileinput.input(files ='/Users/anj/Desktop/My-Family.txt'):
            with self.assertRaises(TypeError):
                line.split(2)
    def test_isdecimal(self):
        i=0
        for line in fileinput.input(files ='/Users/anj/Desktop/My-Family.txt'):
            self.assertTrue(line.isalnum)
        

if __name__ == '__main__':
    unittest.main()