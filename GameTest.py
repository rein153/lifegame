import unittest
from unittest import mock
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

    def test_getneighbor(self):
        mainframe=MainFrame(100,100)
        mainframe.GameMap[0][0]=1
        self.assertEqual(mainframe.get_neighbor(0,0),0,"error")
        self.assertEqual(mainframe.get_neighbor(0,1),1,"error")

    def test_change_status(self):
        mainframe = MainFrame(100, 100)
        mainframe.GameMap[0][0] = 1
        mainframe.change_status(0,0)
        self.assertEqual(mainframe.NextMap[0][0],0,"error")
        self.assertEqual(mainframe.NextMap[0][1],0,"error")

    def test_next_phrase(self):
        mainframe = MainFrame(100,100)
        mainframe.GameMap[0][0] = 1
        mainframe.next_phrase()
        self.assertEqual(mainframe.GameMap[0][0], 0, "error")
        self.assertEqual(mainframe.GameMap[0][1], 0, "error")

    def test_reset(self):
        mainframe = MainFrame(100, 100)
        mainframe.GameMap[0][0] = 1
        mainframe.reset()
        self.assertEqual(mainframe.GameMap[0][0], 0, "error")
        self.assertEqual(mainframe.GameMap[0][1], 0, "error")



    def tearDown(self):
        print("tear down")

if __name__ == '__main__':
    suite=unittest.TestSuite()
    suite.addTest(GameTest("test_getneighbor"))
    suite.addTest(GameTest("test_change_status"))
    suite.addTest(GameTest("test_next_phrase"))
    suite.addTest(GameTest("test_reset"))


    runner=unittest.TextTestRunner()
    runner.run(suite)