import wx
import sqlite3
from SearchRoomorder import *
from OrderRoom import *
from SubmitQuestion import *

class  UsersFunction(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title = "酒店管理系统", size =(300, 260))
        panel = wx.Panel(self)
        self.bt1 = wx.Button(panel, label = "Roomorder", pos = (100, 20))
        self.bt2 = wx.Button(panel, label = "Orderroom", pos = (100, 60))
        self.bt3 = wx.Button(panel, label = "Question", pos = (100, 100))
        self.bt4 = wx.Button(panel, label = "Exit", pos = (100, 140))
        self.bt1.Bind(wx.EVT_BUTTON, self.SearchRoomorder)
        self.bt2.Bind(wx.EVT_BUTTON, self.Orderroom)
        self.bt3.Bind(wx.EVT_BUTTON, self.Question)
        self.bt4.Bind(wx.EVT_BUTTON, self.Exit)
    
    def SearchRoomorder(self, event):
        searchRoomorder()
    def Orderroom(self, event):
        orderRoom()
    def Question(self, event):
        submitQuestion()
    def Exit(self, event):
        self.Destroy()
        exit()

def usersFunction():
    app = wx.App()
    frame = UsersFunction(None, -1)
    frame.Centre()
    frame.Show()
    app.MainLoop()

if __name__ == "__main__":
    usersFunction()