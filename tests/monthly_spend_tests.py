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
    assert_equal(ms.for_month(0, '111111111111'), False)
    assert_equal(ms.for_month(1, '100000000000'), True)
    assert_equal(ms.for_month(1, '000000000000'), False)

def test_read_input_file():
    # These tests are only valid with the supplied test input file

    ms = MonthlySpend()
    ms.read_input_file()

    assert_equal(ms.data[0], '1 111111111111 Test bill 1')
    assert_equal(ms.data[1], '11 101010101010 This is my gas bill')
    assert_equal(ms.data[2], '9 001001001001 Electric Bill')
