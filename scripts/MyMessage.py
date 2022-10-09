from constants import AppInfo, Btn, Icon

from PyQt5.QtWidgets import QDialog, QDesktopWidget, QWidget, QMessageBox
from PyQt5.QtCore import QRect, QDate

class MyMessage():
    """ 自定义的QmessageBox类 """
    TRANSLATE_DICT = {
        '&Ok': '懂了',
        '&Yes': '好吧',
        '&No': '拒绝',
        'Cancel': '取消',
        'Open': '打开文件夹',
        'Ignore': '不用了',
    }

    @staticmethod
    def translateButton(messageBox: QMessageBox):
        for button in messageBox.buttons():
            text = button.text()
            if text in MyMessage.TRANSLATE_DICT.keys():
                button.setText(MyMessage.TRANSLATE_DICT[text])

    @staticmethod
    def information(parent=None, title: str = '消息', text: str = '一个啥也没写的消息', standardButtons: Btn = Btn.Ok, defaultButton: 'Btn' = Btn.Ok):
        """ 中文消息 """
        messageBox = QMessageBox(Icon.INFORMATION, title, text, standardButtons, parent)
        messageBox.setDefaultButton(defaultButton)
        MyMessage.translateButton(messageBox)
        messageBox.exec()
        return messageBox.standardButton(messageBox.clickedButton())

    @staticmethod
    def question(parent=None, title: str = '询问', text: str = '一个啥也没问的问题', standardButtons: Btn = Btn.YesNo, defaultButton: 'Btn' = Btn.Yes):
        """ 中文询问 """
        messageBox = QMessageBox(Icon.QUESTION, title, text, standardButtons, parent)
        messageBox.setDefaultButton(defaultButton)
        MyMessage.translateButton(messageBox)
        messageBox.exec()
        return messageBox.standardButton(messageBox.clickedButton())

    @staticmethod
    def warning(parent=None, title: str = '警告', text: str = '一个啥也没写的警告', standardButtons: Btn = Btn.YesNo, defaultButton: 'Btn' = Btn.Yes):
        """ 中文警告 """
        messageBox = QMessageBox(Icon.WARNING, title, text, standardButtons, parent)
        messageBox.setDefaultButton(defaultButton)
        MyMessage.translateButton(messageBox)
        messageBox.exec()
        return messageBox.standardButton(messageBox.clickedButton())

    @staticmethod
    def critical(parent=None, title: str = '错误', text: str = '一个啥也没写的错误', standardButtons: Btn = Btn.YesNo, defaultButton: 'Btn' = Btn.Yes):
        """ 中文错误 """
        messageBox = QMessageBox(Icon.CRITICAL, title, text, standardButtons, parent)
        messageBox.setDefaultButton(defaultButton)
        MyMessage.translateButton(messageBox)
        messageBox.exec()
        return messageBox.standardButton(messageBox.clickedButton())

    @staticmethod
    def about(parent=None, title: str = '关于', text: str = '一个啥也没写的关于', standardButtons: Btn = Btn.Ok, defaultButton: 'Btn' = Btn.Ok):
        """ 中文关于 """
        messageBox = QMessageBox(None, title, text, standardButtons, parent)
        messageBox.setDefaultButton(defaultButton)
        MyMessage.translateButton(messageBox)
        messageBox.exec()
        return messageBox.standardButton(messageBox.clickedButton())

    @staticmethod
    def finishAndOpen(parent=None, title: str = '完成', text: str = '是否打开文件？', standardButtons: Btn = Btn.YesOpenIgnore, defaultButton: 'Btn' = Btn.Ignore):
        """ 好的|打开文件夹|不用了 """
        messageBox = QMessageBox(Icon.INFORMATION, title, text, standardButtons, parent)
        messageBox.setDefaultButton(defaultButton)
        MyMessage.translateButton(messageBox)
        messageBox.exec()
        return messageBox.standardButton(messageBox.clickedButton())
