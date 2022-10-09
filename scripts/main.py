from csv import excel
from constants import *
from MyMessage import MyMessage

from designer.Ui_MainWindow import Ui_MainWindow


import sys
import os
import shutil,ctypes

from loguru import logger

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog, QSizePolicy, QPushButton, QComboBox
from PyQt5.QtGui import QImage, QIcon, QCloseEvent
from PyQt5.QtCore import QPoint

from HBLibCustomiser import HBLibCustomiser


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

class DirExistException(Exception):
    ...

class Application(Ui_MainWindow, QMainWindow):
    """ 主程序 """

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.initSettings()
        self.initWindow()
        self.initWidget()

    def initSettings(self):
        """ 初始化设置参数 """
        self.hasChange = False  # 提示有更改未保存
        self.lastTabIndex = -1  # 上一个标签页下标
        self.confirmFiles()  # 确认依赖文件

    def initWindow(self):
        """ 初始化主窗口 """
        self.setWindowTitle(AppInfo.NAME+' - '+AppInfo.VERSION)
        #self.setFixedSize(self.width(),self.height())
        self.setWindowIcon(QIcon(AppInfo.ICO_PATH))
        #self.setGeometry(609, 70, 718, 898)

    def initWidget(self):
        """ 初始化部件 """

        self.btn_selectPath.clicked.connect(self.clickedSelectPath)
        self.btn_addData.clicked.connect(self.clickedAddData)

    def confirmFiles(self):
        for filePath in (AppInfo.EXCEL_PATH,):
            if not os.path.exists(filePath):
                MyMessage.critical(self, '缺少必要的文件！', '未发现文件：{}'.format(filePath), Btn.Cancel)
                sys.exit(0)

    def clickedSelectPath(self):
        """ 选择Standard目录 """
        defaultPath = r"C:\Program Files\ladybug_tools\resources\standards"
        initPath = defaultPath if os.path.exists(defaultPath) else "/"
        dir = QFileDialog.getExistingDirectory(self, '选择HB库路径', initPath, QFileDialog.Option.ShowDirsOnly)
        if dir:
            self.le_folderPath.setText(dir)

    def createCustomPath(self,path) -> bool:
        """ 创建自定义目录，返回目录 """
        customPath = os.path.join(path, "honeybee_energy_custom_standards")
        
        if os.path.exists(customPath):
            btn = MyMessage.question(self, "是否覆盖", "存在之前的自定义库，是否覆盖？")
            if btn == Btn.Yes:
                shutil.rmtree(customPath)
            else:
                raise DirExistException()
            
        os.mkdir(customPath)
        constructionPath = os.path.join(customPath, "constructions")
        os.mkdir(constructionPath)
        os.mkdir(os.path.join(customPath, "constructionsets"))
        os.mkdir(os.path.join(customPath, "programtypes"))
        os.mkdir(os.path.join(customPath, "programtypes_registry"))
        os.mkdir(os.path.join(customPath, "schedules"))
        opaqueMaterialPath = os.path.join(constructionPath, "opaque_material.json")
        return opaqueMaterialPath

    def clickedAddData(self):
        path = self.le_folderPath.text()
        if (path is None) or (path.isspace()) or (len(path) == 0):
            MyMessage.warning(self, "输入路径", "请先输入路径", Btn.Ok, Btn.Ok)
            return
        if not os.path.isdir(path):
            MyMessage.critical(self, "路径错误", "输入路径不合法：{path}", Btn.Ok, Btn.Ok)
            return

        # 创建文件夹
        
        try:
            opaqueMaterialPath = self.createCustomPath(path)
        except DirExistException as e:
            return
        except PermissionError as e:
            workPath = os.getcwd()
            MyMessage.question(self,"权限不足",f"操作该目录需要管理员权限: {path}\n库文件夹 honeybee_energy_custom_standards 将生成在: \n{workPath}",Btn.Ok,Btn.Ok)
            try:
                opaqueMaterialPath = self.createCustomPath(workPath)
            except DirExistException as e:
                return
        

        # 读取Excel
        excelPath = AppInfo.EXCEL_PATH
        d = HBLibCustomiser.loadExcel(excelPath)

        # 制作Json
        HBLibCustomiser.createJson(opaqueMaterialPath, d)

        # 显示完成
        MyMessage.information(self, "完成", f"完成{len(d)}项添加")


@logger.catch
def main():
    try:
        logger.info('程序开始启动')
        app = QApplication(sys.argv)
        myWindow = Application()
        logger.info('程序开始运行')
        myWindow.show()
        sys.exit(app.exec())

    except SystemExit as back:
        if str(back) == '0':
            logger.info('程序成功退出，返回值为：{back}', back=back)
            sys.exit(0)
        else:
            logger.error('程序未成功退出，返回值为：{back}', back=back)
            sys.exit(0)


if __name__ == '__main__':
    logger.remove()
    # 控制台输出
    logger.add(
        sink=sys.stderr,
        format="<green>{time:HH:mm:ss.SSS}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        level='DEBUG')
    # 文件输出
    logger.add(sink=AppInfo.LOG_FILE_DIR, rotation="00:00", level='INFO', retention='30 days')

    main()
    showError = QApplication(sys.argv[:1])
    MyMessage.critical(None, '程序炸了', '所以就是炸了呗。。。')
    logger.error('炸了')
    sys.exit(0)
