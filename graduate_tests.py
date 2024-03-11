# Project 3 Graduate Rate (2017-2018)
# Name: Berfredd Quezon
# Instructor: Dr. S. Einakian
# Section: 11

# unittest cases for graduate rate will include here
# At least two test cases for each function
import unittest
from graduate_funcs import *

class TestCases(unittest.TestCase):
    def test_read_file1(self):
        expected = ['3200,Agriculture operations and related sciences,,,,,,\n',
                    '3201,Agriculture general ,1096,1098,120,181,11,3\n',
                    '3400,Computer and information sciences and support services,,,,,,\n',
                    '3401,Computer and information sciences ,17024,3683,7948,3269,508,140']
        self.assertEqual(read_file('small_test.csv'), expected)

    def test_read_file2(self):
        expected = ['3200,Agriculture operations and related sciences,,,,,,\n',
                    '3201,Agriculture general ,1096,1098,120,181,11,3\n',
                    '3202,Agricultural business and management general,745,379,40,26,0,1\n',
                    '3400,Computer and information sciences and support services,,,,,,\n',
                    '3401,Computer and information sciences ,17024,3683,7948,3269,508,140\n',
                    '3413,Data entry/microcomputer applications  general ,0,0,12,8,0,0\n',
                    '3416,Data modeling/warehousing and database administration    ,94,36,460,306,0,0\n',
                    '3600,Education,,,,,,\n',
                    '3618,Educational/instructional technology ,27,35,1404,3772,69,108\n',
                    '3619,Educational evaluation and research ,0,0,37,59,44,100\n',
                    '3800,Engineering technologies/construction trades/mechanics and repairers,,,,,,\n',
                    '3855,Engineering design,1,1,43,34,2,0\n',
                    '3856,Packaging science,223,167,23,15,0,2',]
        self.assertEqual(read_file('big_test.csv'), expected)

    def test_create_division1(self):
        expected = [Division(3200, 'Agriculture operations and related sciences'),
                    Division(3400, 'Computer and information sciences and support services')]
        self.assertEqual(create_division(read_file('small_test.csv')), expected)

    def test_create_division2(self):
        expected = [Division(3200, 'Agriculture operations and related sciences'),
                    Division(3400, 'Computer and information sciences and support services'),
                    Division(3600, 'Education'),
                    Division(3800, 'Engineering technologies/construction trades/mechanics and repairers')]
        self.assertEqual(create_division(read_file('big_test.csv')), expected)

    def test_create_graduate1(self):
        expected = [Graduate(3201, 'Agriculture general ', (1096,1098), (120,181),(11,3)),
                    Graduate(3401, 'Computer and information sciences ',(17024,3683),(7948,3269),(508,140))]
        self.assertEqual(create_graduate(read_file('small_test.csv')), expected)

    def test_create_graduate2(self):
        expected = [Graduate(3201, 'Agriculture general ', (1096, 1098), (120, 181), (11, 3)),
                    Graduate(3202,'Agricultural business and management general',(745,379),(40,26),(0,1)),
                    Graduate(3401, 'Computer and information sciences ', (17024, 3683), (7948, 3269), (508, 140)),
                    Graduate(3413,'Data entry/microcomputer applications  general ',(0,0),(12,8),(0,0)),
                    Graduate(3416,'Data modeling/warehousing and database administration    ',(94,36),(460,306),(0,0)),
                    Graduate(3618,'Educational/instructional technology ',(27,35),(1404,3772),(69,108)),
                    Graduate(3619,'Educational evaluation and research ',(0,0),(37,59),(44,100)),
                    Graduate(3855,'Engineering design',(1,1),(43,34),(2,0)),
                    Graduate(3856,'Packaging science',(223,167),(23,15),(0,2))]
        self.assertEqual(create_graduate(read_file('big_test.csv')), expected)

    def test_create_files1(self):
        expected = None
        self.assertEqual(create_files(create_division(read_file('small_test.csv')),
                         create_graduate(read_file('small_test.csv'))), expected)

    def test_create_files2(self):
        expected = None
        self.assertEqual(create_files(create_division(read_file('big_test.csv')),
                                      create_graduate(read_file('big_test.csv'))), expected)

    def test_find_total_avg_all_divisions1(self):
        divisions = create_division(read_file('med_test.csv'))
        graduates = create_graduate(read_file('med_test.csv'))
        expected = [(2509,418.17),(32572,5428.67),(5415,902.5),(81,13.5)]
        self.assertEqual(find_total_avg_all_divisions(divisions,graduates), expected)

    def test_find_total_avg_all_divisions2(self):
        divisions = create_division(read_file('small_test.csv'))
        graduates = create_graduate(read_file('small_test.csv'))
        expected = [(2509, 418.17), (32572, 5428.67)]
        self.assertEqual(find_total_avg_all_divisions(divisions, graduates), expected)

    def test_find_graduate_rate_major1(self):
        graduates = [Graduate(3201, 'Agriculture general ', (1096, 1098), (120, 181), (11, 3)),
                     Graduate(3401, 'Computer and information sciences ', (17024, 3683), (7948, 3269), (508, 140))]
        expected = (1227,1282)
        self.assertEqual(find_graduate_rate_major(graduates,'Agriculture general'), expected)

    def test_find_graduate_rate_major2(self):
        graduates = [Graduate(3201, 'Agriculture general ', (1096, 1098), (120, 181), (11, 3)),
                     Graduate(3202, 'Agricultural business and management general', (745, 379), (40, 26), (0, 1)),
                     Graduate(3401, 'Computer and information sciences ', (17024, 3683), (7948, 3269), (508, 140)),
                     Graduate(3413, 'Data entry/microcomputer applications  general ', (0, 0), (12, 8), (0, 0)),
                     Graduate(3416, 'Data modeling/warehousing and database administration    ', (94, 36), (460, 306),(0, 0)),
                     Graduate(3618, 'Educational/instructional technology ', (27, 35), (1404, 3772), (69, 108)),
                     Graduate(3619, 'Educational evaluation and research ', (0, 0), (37, 59), (44, 100)),
                     Graduate(3855, 'Engineering design', (1, 1), (43, 34), (2, 0)),
                     Graduate(3856, 'Packaging science', (223, 167), (23, 15), (0, 2))]
        expected = (46, 35)
        self.assertEqual(find_graduate_rate_major(graduates, 'Engineering design'), expected)

    def test_check_graduate_eq(self):
        grad1 = Graduate(3619, 'Educational evaluation and research ', (0, 0), (37, 59), (44, 100))
        grad2 = Graduate(3619, 'Educational evaluation and research ', (0, 0), (37, 59), (44, 100))
        self.assertEqual(grad1,grad2)

    def test_total_grad_in_div1(self):
        graduates = create_graduate(read_file('big_test.csv'))
        self.assertEqual(total_grad_in_div(graduates, '3400'), (7442,26046))

    def test_total_grad_in_div2(self):
        graduates = create_graduate(read_file('big_test.csv'))
        self.assertEqual(total_grad_in_div(graduates, '3800'), (219,292))

# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
