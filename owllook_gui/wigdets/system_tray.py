#!/usr/bin/env python
"""
 Created by howie.hu at 2018/6/5.
"""
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QMenu, QSystemTrayIcon


class SystemTray(QSystemTrayIcon):

    def __init__(self, icon_path, parent=None):
        super(SystemTray, self).__init__(parent)
        self.parent = parent
        self.icon = self.MessageIcon()

        # 在系统托盘处显示图标
        self.setIcon(QIcon(icon_path))
        # 设置图标
        self.set_default_menu()
        # 设置点击事件
        self.set_active_event()

    def set_default_menu(self):
        # 设置系统托盘图标的菜单
        action_show = QAction('&显示', self, triggered=self.parent.show)
        action_show.setShortcut('Ctrl+O')
        # 直接退出可用qApp.quit
        action_quit = QAction('&退出', self, triggered=self.quit_main_window)
        action_quit.setShortcut('Ctrl+Q')

        sys_tray_icon_menu = QMenu()
        sys_tray_icon_menu.addAction(action_show)
        sys_tray_icon_menu.addAction(action_quit)
        self.setContextMenu(sys_tray_icon_menu)

    def set_active_event(self):
        self.activated.connect(self.click_sys_tray_icon)

    def click_sys_tray_icon(self, reason):
        reason = int(reason)
        if reason == 2 or reason == 3:
            pass

        if reason == 4:
            # 中键点击
            pass

    def quit_main_window(self):
        QCoreApplication.instance().quit()
