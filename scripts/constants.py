# coding=utf-8
from enum import Enum
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMessageBox

class AppInfo:
    NAME = "HB Lib Customiser"
    VERSION = "Ver 0.10"
    LOG_FILE_DIR = './log/program.log'
    EXCEL_PATH = "./添加数据.xlsx"
    
class Color():
    GREEN = QColor('#00a388')
    YELLOW = QColor('#ffff9d')


class Btn():
    YesNo = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No  # type:Btn
    YesOpenIgnore = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Open | QMessageBox.StandardButton.Ignore  # type:Btn
    Yes = QMessageBox.StandardButton.Yes  # type:Btn
    No = QMessageBox.StandardButton.No  # type:Btn
    Ok = QMessageBox.StandardButton.Ok  # type:Btn
    Cancel = QMessageBox.StandardButton.Cancel  # type:Btn
    Open = QMessageBox.StandardButton.Open  # type:Btn
    Ignore = QMessageBox.StandardButton.Ignore  # type:Btn


class Icon():
    INFORMATION = QMessageBox.Icon.Information  # type:Icon
    QUESTION = QMessageBox.Icon.Question  # type:Icon
    WARNING = QMessageBox.Icon.Warning  # type:Icon
    CRITICAL = QMessageBox.Icon.Critical  # type:Icon
