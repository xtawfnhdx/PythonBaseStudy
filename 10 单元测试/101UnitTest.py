import unittest


class TestStringMethods(unittest.TestCase):
    # 会在每个测试方法之前执行
    def setUp(self):
        print('初始化操作')

    # 会在每个测试方法之后执行
    def tearDown(self):
        print('测试完成执行的操作')

    def test_upper(self):
        self.assertEqual('Abc'.upper(), 'ABC')

    def test_isupper(self):
        self.assertTrue('ABC'.isupper())
        self.assertFalse('abc'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)
