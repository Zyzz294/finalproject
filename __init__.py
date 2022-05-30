# from PyQt5.QtWidgets import QMessageBox
# from PyQt5.QtGui import QBrush,QPixmap
# import Rename,WaterMark # 导入模块
#
# palette = QtGui.QPalette()
# # 设置窗体背景自适应
# palette.setBrush(MainWindow.backgroundRole(), QBrush(QPixmap("image/back.png").scaled(MainWindow.size(), QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation)))
# MainWindow.setPalette(palette)
# MainWindow.setAutoFillBackground(True)  # 设置自动填充背景
#
#         #水印界面
#         self.pushButton.clicked.connect(self.openMark)
#         #重命名界面
#         self.pushButton_2.clicked.connect(self.openRename)
#         #软件介绍
#         self.pushButton_3.clicked.connect(self.about)
#
#     # 打开水印窗体
#     def openMark(self):
#         self.another = WaterMark.Ui_MainWindow()  # 创建水印窗体对象
#         self.another.show()  # 显示窗体
#
#     # 打开重命名窗体
#     def openRename(self):
#         self.another = Rename.Ui_MainWindow()  # 创建重命名窗体对象
#         self.another.show()  # 显示窗体
#
#     # 关于本软件
#     def about(self):
#         QMessageBox.information(None, '关于本软件', '图片批量处理器是一款提供日常工作的工具软件，'
#                                                    '通过该软件，您可以方便的为图片添加文字水印和图片水印，'
#                                                    '而且可以自定义添加位置，以及透明度；另外，您还可以通过'
#                                                    '该软件对图片文件进行重命名，支持文件名大写、小写，以及'
#                                                    '根据自定义模板对图片文件进行编号。', QMessageBox.Ok)
#
#  # 主方法
# if __name__ == '__main__':
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()  # 创建窗体对象
#     ui = Ui_MainWindow()  # 创建PyQt5设计的窗体对象
#     ui.setupUi(MainWindow)  # 调用PyQt5窗体的方法对窗体对象进行初始化设置
#     MainWindow.show()  # 显示窗体
#     sys.exit(app.exec_())  # 程序关闭时退出进程
#
#
#
#
# import os
# import os.path
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QMessageBox, QFileDialog, QFontDialog, QMainWindow
# from PyQt5.QtGui import QFontMetrics, QFontInfo
# from PyQt5.QtGui import QBrush,QPixmap
# from PIL import Image, ImageDraw, ImageFont, ImageEnhance
#
# class Ui_MainWindow(QMainWindow):
#     def __init__(self):
#         super(Ui_MainWindow, self).__init__()
#
#         self.setupUi(self)
#
#
#
#
#         self.statusbar.showMessage('准备就绪…… ')  # 设置状态栏默认值
#
#
#
#         # 关联添加图片
#         self.b.clicked.connect(self.getFiles)
#         # 关联字体设置
#         self.b1.clicked.connect(self.setFont)
#         # 关联存储位置浏览
#         self.b2.clicked.connect(self.msg)
#         # 关联保存水印图片
#         self.bc.clicked.connect(self.addMark)
#         # 关联列表图片预览
#         self.listWidget.itemClicked.connect(self.itemClick)
#
#     # 判断是否为图片
#     def isImg(self, file):
#         file = file.lower()
#         if file == '.jpg':
#             return True
#         elif file == '.png':
#             return True
#         elif file == '.jpeg':
#             return True
#         elif file == '.bmp':
#             return True
#         else:
#             return False
#
#         # 获取图片路径
#     def getFiles(self):
#         try:
#             # 选择图片文件夹路径
#             self.img_path = QFileDialog.getExistingDirectory(None, "选择图片文件夹路径", os.getcwd())
#             self.list = os.listdir(self.img_path)  # 遍历选择的文件夹
#             num = 0  # 记录图片数量
#             self.listWidget.clear()  # 清空列表项
#             for i in range(0, len(self.list)):
#                     # 遍历图片列表
#                 filepath = os.path.join(self.img_path, self.list[i])  # 记录遍历到的文件名
#                 if os.path.isfile(filepath):  # 判断是否是文件
#                     imgType = os.path.splitext(filepath)[1]  # 获取扩展名
#                     if self.isImg(imgType):  # 判断是否为图片
#                         num += 1  # 图片数量加1
#                         self.item = QtWidgets.QListWidgetItem(self.listWidget)  # 创建列表项
#                         self.item.setText(self.list[i])  # 显示图片列表
#             self.statusbar.showMessage('共有图片' + str(num) + '张')  # 状态栏显示图片总数
#         except Exception:
#             QMessageBox.warning(None, '警告', '请选择一个有效路径...')
#
#     # 预览图片
#     def itemClick(self, item):
#         os.startfile(self.img_path + '\\' + item.text())
#
#     # 设置字体
#     def setFont(self):
#         self.waterfont, ok = QFontDialog.getFont()  # 显示字体对话框
#         if ok:  # 判断是否选择了字体
#             self.t1.setFont(self.waterfont)  # 设置水印文字的字体
#             self.fontSize = QFontMetrics(self.waterfont)  # 获取字体尺寸
#             self.fontInfo = QFontInfo(self.waterfont)  # 获取字体信息
#
#     # 设置存储路径
#     def msg(self):
#         try:
#             # dir_path即为选择的文件夹的绝对路径，第二个参数为对话框标题，第三个为对话框打开后默认的路径
#             self.dir_path = QFileDialog.getExistingDirectory(None, "选择路径", os.getcwd())
#             self.t2.setText(self.dir_path)  # 显示选择的的保存路径
#         except Exception as e:
#             print(e)
#
#     # 添加文字水印
#     def textMark(self, img, newImgPath):
#         try:
#             im = Image.open(img).convert('RGBA')  # 打开原始图片，并转换为RGBA
#             newImg = Image.new('RGBA', im.size, (255, 255, 255, 0))  # 存储添加水印后的图片
#             fonttype = 'C:\\Users\\kezhipeng\\Desktop\\set\\python\\课程代码\\Fonts\\' + self.fontInfo.family() + '.ttf'  # 'simkai.ttf'
#             font = ImageFont.truetype(fonttype, self.fontInfo.pointSize(), encoding="utf-8")
#             #print("通过")
#             imagedraw = ImageDraw.Draw(newImg)  # 创建绘制对象
#                 #       imagewidth,imageheight = im.size    #记载图片大小
#                 #      txtwidth = self.fontSize.maxWidth()*len(self.t1.text())     #获取字体宽度
#                 #     txtheight = self.fontSize.height()  #获取字体高度
#
#                 # 设置水印文字位置
#             X = eval(self.x.text())
#             Y = eval(self.y.text())
#             position = (X, Y)
#
#             imagedraw.text(xy=position, text=self.t1.text(), font=font, fill=(255, 255, 255, 60))
#
#             # 设置透明度
#             alpha = newImg.split()[3]
#             alpha = ImageEnhance.Brightness(alpha).enhance(int(self.horizontalSlider.value()) / 10.0)
#             newImg.putalpha(alpha)
#             # 保存图片
#             out = Image.alpha_composite(im, newImg)
#             out = out.convert('RGB')
#             out.save(newImgPath)
#
#
#         except Exception as e1:
#             print(e1)
#             QMessageBox.warning(None, '错误', '图片格式有误，请重新选择...', QMessageBox.Ok)
#
#     # 添加水印
#     def addMark(self):
#         if self.t2.text() == '':  # 判断是否选择了保存路径
#             QMessageBox.warning(None, '警告', '请选择保存路径', QMessageBox.Ok)
#             return
#         else:
#             num = 0  # 记录图片数量
#             for i in range(0, self.listWidget.count()):  # 遍历图片列表
#                    # 设置原图片路径（包括文件名）
#                 filepath = os.path.join(self.img_path, self.listWidget.item(i).text())
#                     # 设置水印图片保存路径（包括文件名）
#                 newfilepath = os.path.join(self.t2.text(), self.listWidget.item(i).text())
#                 if self.t1.text() == '':  # 判断是否输入了水印文字
#                     QMessageBox.warning(None, '警告', '请输入水印文字', QMessageBox.Ok)
#                     return
#                 else:
#                     self.textMark(filepath, newfilepath)  # 调用textMark方法添加文字水印
#                     num += 1  # 处理图片数量加一
#             self.statusbar.showMessage('任务完成，此次共处理 ' + str(num) + ' 张图片')  # 显示处理图片总数