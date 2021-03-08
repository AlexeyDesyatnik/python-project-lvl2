# import pytest
from gendiff import generate_diff


FIXTURES_PATH = './tests/fixtures/'
FNAME1 = 'testfile1.json'
FNAME2 = 'testfile2.json'


def file_test(fname1, fname2, test_result):
    expected = open(FIXTURES_PATH + test_result)
    actual = generate_diff(
        FIXTURES_PATH + fname1,
        FIXTURES_PATH + fname2
    ).splitlines(True)

    for line1, line2 in zip(expected, actual):
        assert line1 == line2


def test_diff1():
    file_test(FNAME1, FNAME2, 'testresult1.txt')


def test_diff2():
    file_test(FNAME2, FNAME1, 'testresult2.txt')


def test_diff3():
    file_test(FNAME1, FNAME1, 'testresult3.txt')
