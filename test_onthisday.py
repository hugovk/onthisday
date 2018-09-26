#!/usr/bin/env python
"""
Unit tests for contact_sheet.py
"""
import datetime
import unittest

import onthisday


class TestSequenceFunctions(unittest.TestCase):

    # def setUp(self):
    #     self.seq = range(10)

    def daterange(self, start_date, end_date):
        # https://stackoverflow.com/q/1060279/724176
        for n in range(int((end_date - start_date).days)):
            yield start_date + datetime.timedelta(n)

    def test_changed(self):
        """ Test return isn't same as parameter """
        input = datetime.datetime.now()
        output = onthisday.six_months_ago(input)
        self.assertNotEqual(input, output)

    def test_dec_to_june(self):
        """ Test 22 December 2013 -> 22 June 2013 """
        input = datetime.datetime(2013, 12, 22)
        expected_output = datetime.datetime(2013, 6, 22)
        output = onthisday.six_months_ago(input)
        self.assertEqual(expected_output, output)

    def test_jan_to_july(self):
        """ Test 20 January 2014 -> 20 July 2013 """
        input = datetime.datetime(2014, 1, 20)
        expected_output = datetime.datetime(2013, 7, 20)
        output = onthisday.six_months_ago(input)
        self.assertEqual(expected_output, output)

    def test_from_31st_jan(self):
        """ Test 31 January 2014 -> 31 July 2013 """
        input = datetime.datetime(2014, 1, 31)
        expected_output = datetime.datetime(2013, 7, 31)
        output = onthisday.six_months_ago(input)
        self.assertEqual(expected_output, output)

    def test_from_31st_march(self):
        """ Test 31 March 2014 -> 30 September 2013 """
        input = datetime.datetime(2014, 3, 31)
        expected_output = datetime.datetime(2013, 9, 30)
        output = onthisday.six_months_ago(input)
        self.assertEqual(expected_output, output)

    def test_to_last_of_feb(self):
        """ Test 31 August 2014 -> 28 Feb 2014 """
        input = datetime.datetime(2014, 8, 31)
        expected_output = datetime.datetime(2014, 2, 28)
        output = onthisday.six_months_ago(input)
        self.assertEqual(expected_output, output)

    def test_to_leap_day(self):
        """ Test 31 August 2012 -> 29 Feb 2012 """
        input = datetime.datetime(2012, 8, 31)
        expected_output = datetime.datetime(2012, 2, 29)
        output = onthisday.six_months_ago(input)
        self.assertEqual(expected_output, output)

    def test_lots_of_days(self):
        """ Tests:
            No "ValueError: day is out of range for month" exceptions raised
            (e.g. for 30 Feb),
            output value is different from input, and
            output value is earlier than input
        """
        start_date = datetime.datetime(2000, 1, 1)
        end_date = datetime.datetime(2030, 12, 31)
        for input in self.daterange(start_date, end_date):
            output = onthisday.six_months_ago(input)
            self.assertNotEqual(input, output)
            self.assertLess(output, input)

    def test_2_changed(self):
        """ Test return isn't same as parameter """
        input = datetime.datetime.now()
        output = onthisday.six_months_from(input)
        self.assertNotEqual(input, output)

    def test_2_dec_to_june(self):
        """ Test 22 December 2013 -> 22 June 2014 """
        input = datetime.datetime(2013, 12, 22)
        expected_output = datetime.datetime(2014, 6, 22)
        output = onthisday.six_months_from(input)
        self.assertEqual(expected_output, output)

    def test_2_jan_to_july(self):
        """ Test 20 January 2014 -> 20 July 2014 """
        input = datetime.datetime(2014, 1, 20)
        expected_output = datetime.datetime(2014, 7, 20)
        output = onthisday.six_months_from(input)
        self.assertEqual(expected_output, output)

    def test_2_from_31st_jan(self):
        """ Test 31 January 2014 -> 31 July 2014 """
        input = datetime.datetime(2014, 1, 31)
        expected_output = datetime.datetime(2014, 7, 31)
        output = onthisday.six_months_from(input)
        self.assertEqual(expected_output, output)

    def test_2_from_31st_march(self):
        """ Test 31 March 2014 -> None """
        input = datetime.datetime(2014, 3, 31)
        expected_output = None
        output = onthisday.six_months_from(input)
        self.assertEqual(expected_output, output)

    def test_2_to_last_of_feb(self):
        """ Test 31 August 2014 -> 28 Feb 2015 """
        input = datetime.datetime(2014, 8, 31)
        expected_output = None
        output = onthisday.six_months_from(input)
        self.assertEqual(expected_output, output)

    def test_2_to_leap_day(self):
        """ Test 31 August 2011 -> 29 Feb 2012 """
        input = datetime.datetime(2011, 8, 31)
        expected_output = None
        output = onthisday.six_months_from(input)
        self.assertEqual(expected_output, output)

    def test_2_lots_of_days(self):
        """ Some dates with day > 28 will return None. Forget those.
            Tests:
            days 1-28 don't return None
            output value is different from input, and
            output value is later than input
        """
        for year in range(2000, 2030 + 1):
            for month in range(1, 12):
                for day in range(1, 28):
                    input = datetime.datetime(year, month, day)
                    output = onthisday.six_months_from(input)
                    self.assertIsNotNone(output)
                    self.assertNotEqual(input, output)
                    self.assertGreater(output, input)


if __name__ == "__main__":
    unittest.main()
