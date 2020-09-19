import unittest
from MainFrame import MainFrame
from GUI import GUI


class GameTest(unittest.TestCase):

    def setUp(self):
        print("start test")


    def test_start(self):
        gui = GUI(10,10)
        self.assertEqual(gui.start(),1,"error")

    def test_pause(self):
        gui = GUI(10,10)
        self.assertEqual(gui.pause(),0,"error")

    def test_resetgui(self):
        gui = GUI(10,10)
        for i in range(10):
            for j in range(10):
                gui.frame.GameMap[i][j] = 1
        gui.reset()
        for i in range(10):
            for j in range(10):
                self.assertEqual(gui.frame.GameMap[i][j],0,"error")

    def test_drawText(self):
        gui = GUI(10,10)
        self.assertNotEqual(gui.drawText(""),0,"error")


    def test_getneighbor(self):
        mainframe=MainFrame(100,100)
        mainframe.GameMap[0][0] = 1
        mainframe.GameMap[0][1] = 1
        mainframe.GameMap[0][2] = 1
        mainframe.GameMap[1][0] = 1
        mainframe.GameMap[1][1] = 1
        mainframe.GameMap[1][2] = 1
        mainframe.GameMap[2][0] = 1
        mainframe.GameMap[2][1] = 1
        mainframe.GameMap[2][2] = 1
        #本格子以及周围格子设置为1
        self.assertEqual(mainframe.get_neighbor(1,1),8,"error")
        #检测周围或者数量是否为8

        mainframe.GameMap[0][0] = 0
        self.assertEqual(mainframe.get_neighbor(1, 1), 7, "error")
        #逐渐递减
        mainframe.GameMap[0][1] = 0
        self.assertEqual(mainframe.get_neighbor(1, 1), 6, "error")
        mainframe.GameMap[0][2] = 0
        self.assertEqual(mainframe.get_neighbor(1, 1), 5, "error")
        mainframe.GameMap[1][0] = 0
        self.assertEqual(mainframe.get_neighbor(1, 1), 4, "error")
        mainframe.GameMap[1][1] = 0
        self.assertEqual(mainframe.get_neighbor(1, 1), 4, "error") #本格子设置为0.没有影响
        mainframe.GameMap[1][2] = 0
        self.assertEqual(mainframe.get_neighbor(1, 1), 3, "error")
        mainframe.GameMap[2][0] = 0
        self.assertEqual(mainframe.get_neighbor(1, 1), 2, "error")
        mainframe.GameMap[2][1] = 0
        self.assertEqual(mainframe.get_neighbor(1, 1), 1, "error")
        mainframe.GameMap[2][2] = 0
        self.assertEqual(mainframe.get_neighbor(1, 1), 0, "error")

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
        self.assertEqual(mainframe.NextMap[1][1], 0, "error")#死亡

        mainframe.GameMap[0][0] = 1
        mainframe.GameMap[0][1] = 1
        mainframe.GameMap[0][2] = 0
        mainframe.GameMap[1][0] = 1
        mainframe.GameMap[1][2] = 0
        mainframe.GameMap[2][0] = 0
        mainframe.GameMap[2][1] = 0
        mainframe.GameMap[2][2] = 0
        mainframe.change_status(1, 1)
        self.assertEqual(mainframe.NextMap[1][1], 1, "error")#一定活

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
        self.assertEqual(mainframe.NextMap[1][1], 1, "error")#不变

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

    def test_next_phrase(self):
        mainframe = MainFrame(100,100)
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

    def test_reset(self):
        mainframe = MainFrame(100, 100)
        for i in range(50):
            for j in range(50):
                mainframe.GameMap[0][0] = 1
        mainframe.reset()
        for i in range(50):
            for j in range(50):
                self.assertEqual(mainframe.GameMap[i][j], 0, "error")



    def tearDown(self):
        print("tear down")

if __name__ == '__main__':
    suite=unittest.TestSuite()

    suite.addTest(GameTest("test_start"))
    suite.addTest(GameTest("test_pause"))
    suite.addTest(GameTest("test_getneighbor"))
    suite.addTest(GameTest("test_change_status"))
    suite.addTest(GameTest("test_next_phrase"))
    suite.addTest(GameTest("test_reset"))
    suite.addTest(GameTest("test_resetgui"))
    suite.addTest(GameTest("test_drawText"))

    runner=unittest.TextTestRunner()
    runner.run(suite)