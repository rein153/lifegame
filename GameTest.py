import unittest
from MainFrame import MainFrame
from GUI import GUI


class GameTest(unittest.TestCase):

    # 开始测试标志
    def setUp(self):
        print("start test")

    # 测试游戏开始
    def test_start(self):
        gui = GUI(10, 10)
        self.assertEqual(gui.start(), 1, "error")

    # 测试游戏暂停
    def test_pause(self):
        gui = GUI(10, 10)
        self.assertEqual(gui.pause(), 0, "error")

    # 测试GUI界面重置
    def test_resetgui(self):
        gui = GUI(10, 10)
        for i in range(10):
            for j in range(10):
                gui.frame.GameMap[i][j] = 1
        gui.reset()
        for i in range(10):
            for j in range(10):
                self.assertEqual(gui.frame.GameMap[i][j], 0, "error")

    # 测试获取单个细胞周围存活细胞数
    def test_getneighbor(self):
        mainframe = MainFrame(100, 100)
        mainframe.GameMap[0][0] = 1
        mainframe.GameMap[0][1] = 1
        mainframe.GameMap[0][2] = 1
        mainframe.GameMap[1][0] = 1
        mainframe.GameMap[1][1] = 1
        mainframe.GameMap[1][2] = 1
        mainframe.GameMap[2][0] = 1
        mainframe.GameMap[2][1] = 1
        mainframe.GameMap[2][2] = 1
        # 本格子以及周围格子设置为1
        self.assertEqual(mainframe.get_neighbor(1, 1), 8, "error")
        # 检测周围或者数量是否为8

        mainframe.GameMap[0][0] = 0
        self.assertEqual(mainframe.get_neighbor(1, 1), 7, "error")
        # 逐渐递减
        mainframe.GameMap[0][1] = 0
        self.assertEqual(mainframe.get_neighbor(1, 1), 6, "error")
        mainframe.GameMap[0][2] = 0
        self.assertEqual(mainframe.get_neighbor(1, 1), 5, "error")
        mainframe.GameMap[1][0] = 0
        self.assertEqual(mainframe.get_neighbor(1, 1), 4, "error")
        mainframe.GameMap[1][1] = 0
        self.assertEqual(mainframe.get_neighbor(1, 1), 4, "error")  # 本格子设置为0.没有影响
        mainframe.GameMap[1][2] = 0
        self.assertEqual(mainframe.get_neighbor(1, 1), 3, "error")
        mainframe.GameMap[2][0] = 0
        self.assertEqual(mainframe.get_neighbor(1, 1), 2, "error")
        mainframe.GameMap[2][1] = 0
        self.assertEqual(mainframe.get_neighbor(1, 1), 1, "error")
        mainframe.GameMap[2][2] = 0
        self.assertEqual(mainframe.get_neighbor(1, 1), 0, "error")

    # 测试改变单个细胞状态
    def test_change_status(self):
        mainframe = MainFrame(100, 100)
        mainframe.GameMap[0][0] = 1
        mainframe.GameMap[0][1] = 1
        mainframe.GameMap[0][2] = 1
        mainframe.GameMap[1][0] = 1
        mainframe.GameMap[1][2] = 1
        mainframe.GameMap[2][0] = 1
        mainframe.GameMap[2][1] = 1
        mainframe.GameMap[2][2] = 1
        mainframe.change_status(1, 1)
        self.assertEqual(mainframe.NextMap[1][1], 0, "error")  # 死亡

        mainframe.GameMap[0][0] = 1
        mainframe.GameMap[0][1] = 1
        mainframe.GameMap[0][2] = 0
        mainframe.GameMap[1][0] = 1
        mainframe.GameMap[1][2] = 0
        mainframe.GameMap[2][0] = 0
        mainframe.GameMap[2][1] = 0
        mainframe.GameMap[2][2] = 0
        mainframe.change_status(1, 1)
        self.assertEqual(mainframe.NextMap[1][1], 1, "error")  # 一定活

        mainframe.GameMap[0][0] = 1
        mainframe.GameMap[0][1] = 0
        mainframe.GameMap[0][2] = 0
        mainframe.GameMap[1][0] = 1
        mainframe.GameMap[1][2] = 0
        mainframe.GameMap[2][0] = 0
        mainframe.GameMap[2][1] = 0
        mainframe.GameMap[2][2] = 0
        mainframe.GameMap[1][1] = 1
        mainframe.change_status(1, 1)
        self.assertEqual(mainframe.NextMap[1][1], 1, "error")  # 不变

        mainframe.GameMap[0][0] = 1
        mainframe.GameMap[0][1] = 0
        mainframe.GameMap[0][2] = 0
        mainframe.GameMap[1][0] = 1
        mainframe.GameMap[1][2] = 0
        mainframe.GameMap[2][0] = 0
        mainframe.GameMap[2][1] = 0
        mainframe.GameMap[2][2] = 0
        mainframe.GameMap[1][1] = 0
        mainframe.change_status(1, 1)
        self.assertEqual(mainframe.NextMap[1][1], 0, "error")  # 不变

        # 边界测试
        mainframe.GameMap[99][99] = 1
        mainframe.GameMap[0][99] = 0
        mainframe.GameMap[1][99] = 0
        mainframe.GameMap[99][0] = 1
        mainframe.GameMap[1][0] = 0
        mainframe.GameMap[99][1] = 0
        mainframe.GameMap[0][1] = 1
        mainframe.GameMap[1][1] = 0
        mainframe.change_status(0, 0)
        self.assertEqual(mainframe.NextMap[0][0], 1, "error")  # 不变

    # 测试全部细胞状态更新
    def test_next_phrase(self):
        mainframe = MainFrame(100, 100)
        mainframe.GameMap[0][0] = 1
        mainframe.GameMap[0][1] = 1
        mainframe.GameMap[0][2] = 1
        mainframe.GameMap[1][0] = 1
        mainframe.GameMap[1][2] = 1
        mainframe.GameMap[2][0] = 1
        mainframe.GameMap[2][1] = 1
        mainframe.GameMap[2][2] = 1
        mainframe.next_phrase()
        self.assertEqual(mainframe.GameMap[0][0], 1, "error")
        self.assertEqual(mainframe.GameMap[1][1], 0, "error")
        self.assertEqual(mainframe.GameMap[99][1], 1, "error")

        mainframe.GameMap[97][97] = 1
        mainframe.GameMap[97][98] = 1
        mainframe.GameMap[97][99] = 1
        mainframe.GameMap[98][97] = 0
        mainframe.GameMap[98][98] = 1
        mainframe.GameMap[98][99] = 0
        mainframe.GameMap[99][97] = 0
        mainframe.GameMap[99][98] = 1
        mainframe.next_phrase()
        self.assertEqual(mainframe.GameMap[98][98], 0, "error")

    # 将所有单元格置为1，检测清空函数是否正常进行。如果正常运行，则应该数组全为0
    def test_reset(self):
        mainframe = MainFrame(100, 100)
        for i in range(100):
            for j in range(100):
                mainframe.GameMap[0][0] = 1
        mainframe.reset()
        for i in range(100):
            for j in range(100):
                self.assertEqual(mainframe.GameMap[i][j], 0, "error")

    def tearDown(self):
        print("tear down")


if __name__ == '__main__':
    suite = unittest.TestSuite()

    suite.addTest(GameTest("test_start"))  # 测试游戏开始
    suite.addTest(GameTest("test_pause"))  # 测试游戏暂停
    suite.addTest(GameTest("test_getneighbor"))  # 测试 获取该方格周边存活数量
    suite.addTest(GameTest("test_change_status"))  # 测试 改变该方格存活状态
    suite.addTest(GameTest("test_next_phrase"))  # 测试 改变全部方格状态
    suite.addTest(GameTest("test_reset"))  # 测试 重置内部数组
    suite.addTest(GameTest("test_resetgui"))  # 测试 重置棋盘

    runner = unittest.TextTestRunner()
    runner.run(suite)
