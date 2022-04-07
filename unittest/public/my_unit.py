import unittest


class MyUnit(unittest.TestCase):

    @classmethod  # 装饰器: 完成一种特定功能的函数(事物，比如：口红) 以@开头，有类装饰器和函数装饰器
    def setUpClass(cls) -> None:
        print("\n在每个类之前运行一次 用于创建数据库链接，创建日志对象")

    def setUp(self) -> None:
        print("\n在每个用例之前运行一次 用于打开浏览器加载网页")

    def tearDown(self) -> None:
        print("\n在每个用例之后运行一次 用于关闭网页")

    @classmethod
    def tearDownClass(cls) -> None:
        print("\n在每个类之后运行一次 用于关闭数据库链接，销毁日志对象")