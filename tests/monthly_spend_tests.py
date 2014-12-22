# monthly_spend tests

from nose.tools import *
from monthly_spend.monthly_spend import MonthlySpend

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"

def test_for_month():
    ms = MonthlySpend()

    assert_equal(ms.for_month(1, '10000000000'), False)
    assert_equal(ms.for_month(1, '1000000000000'), False)
    assert_equal(ms.for_month(0, '111111111111'), False)
    assert_equal(ms.for_month(1, '100000000000'), True)
    assert_equal(ms.for_month(12, '000000000001'), True)
    assert_equal(ms.for_month(5, '000010000000'), True)
    assert_equal(ms.for_month(1, '000000000000'), False)

def test_read_input_file():
    # These tests are only valid with the supplied test input file

    ms = MonthlySpend()
    ms.read_input_file()

    assert_equal(ms.data[0], '1 111111111111 12.01 Test bill 1')
    assert_equal(ms.data[1], '11 101010101010 23.00 This is my gas bill')
    assert_equal(ms.data[2], '9 001001001001 123.65 Electric Bill')
    assert_equal(ms.data[3], '25 100010001000 98.54 Internet bill')

def test_parse_data_entry():
    ms = MonthlySpend()

    assert_equal(ms.parse_data_entry('0 111111111111 1.20 test data'), 'ERROR')
    assert_equal(ms.parse_data_entry('1 12.00 data'), 'ERROR')
    assert_equal(ms.parse_data_entry('1 111111111111 23.87 test'), ['1', '111111111111','23.87','test'])
    assert_equal(ms.parse_data_entry('1 111111111111 1.01 test data'), ['1', '111111111111','1.01','test data'])
    assert_equal(ms.parse_data_entry('11 111111111111 7.00 test data'), ['11', '111111111111','7.00','test data'])

def test_create_full_list():
    ms = MonthlySpend()
    ms.read_input_file()
    ms.create_full_list()

    assert_equal(ms.full_list[0], [1, 1, 12.01, 'Test bill 1'])
    assert_equal(ms.full_list[1], [1, 11, 23, 'This is my gas bill'])
    assert_equal(ms.full_list[2], [1, 25, 98.54, 'Internet bill'])
    assert_equal(ms.full_list[3], [2, 1, 12.01, 'Test bill 1'])
    assert_equal(ms.full_list[4], [3, 1, 12.01, 'Test bill 1'])
    assert_equal(ms.full_list[5], [3, 9, 123.65, 'Electric Bill'])
    assert_equal(ms.full_list[6], [3, 11, 23, 'This is my gas bill'])
    assert_equal(ms.full_list[7], [4, 1, 12.01, 'Test bill 1'])
    assert_equal(ms.full_list[8], [5, 1, 12.01, 'Test bill 1'])
    assert_equal(ms.full_list[9], [5, 11, 23, 'This is my gas bill'])
    assert_equal(ms.full_list[10], [5, 25, 98.54, 'Internet bill'])
    assert_equal(ms.full_list[11], [6, 1, 12.01, 'Test bill 1'])
    assert_equal(ms.full_list[12], [6, 9, 123.65, 'Electric Bill'])
    assert_equal(ms.full_list[13], [7, 1, 12.01, 'Test bill 1'])

def test_calculate():
    ms = MonthlySpend()
    ms.read_input_file()
    ms.create_full_list()

    assert_equal(ms.calculate(1, 5, 0.0), -23)
    assert_equal(ms.calculate(1, 5, 100.0), 77)
    assert_equal(ms.calculate(1, 21, 0.0), (0.0 - 98.54 - 12.01))
    assert_equal(ms.calculate(1, 21, 100.0), (100.0 - 98.54 - 12.01))
    assert_equal(ms.calculate(3, 23, 0.0), -12.01)
    assert_equal(ms.calculate(3, 23, 112.0), 99.99)
    assert_equal(ms.calculate(5, 22, 0.0), (0.0 - 98.54 - 12.01 - 123.65))
    assert_equal(ms.calculate(5, 22, 1020.32), (1020.32 - 98.54 - 12.01 - 123.65))
    assert_equal(ms.calculate(12, 22, 0.0), (0.0 - 12.01 - 23.0))
    assert_equal(ms.calculate(12, 22, 100.0), (100.0 - 12.01 - 23.0))
