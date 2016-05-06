import sys
from scipy.misc import *
from PySide.QtGui import *
from PySide.QtCore import *
from SteganographyGUI import *
from Steganography import *


class SteganographyApp(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(SteganographyApp, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Steganography - Alex Dunker")
        self.chkApplyCompression.clicked.connect(self.comp_check)
        self.slideCompression.valueChanged.connect(self.level_change)
        self.btnSave.clicked.connect(self.save_new)
        self.btnClean.clicked.connect(self.clean_img)
        self.btnExtract.clicked.connect(self.extract_img)

        self.comp_level = -1
        self.valid_p1 = False
        self.valid_c1 = False

        self.carrier = None
        self.payload = None
        self.carrier1 = None
        self.payload1 = None

        self.g_payload1 = Graphics(self.grpPayload1)
        self.g_payload1.setObjectName("g_payload1")
        self.g_payload1.setGeometry(QtCore.QRect(10, 40, 361, 281))
        p1_lambda = lambda: self.update_payload(self.g_payload1.img_array)
        self.g_payload1.scene1.changed.connect(p1_lambda)

        self.g_carrier1 = Graphics(self.grpCarrier1)
        self.g_carrier1.setObjectName("g_carrier1")
        self.g_carrier1.setGeometry(QtCore.QRect(10, 40, 361, 281))
        c1_lambda = lambda: self.update_carrier(self.g_carrier1.img_array)
        self.g_carrier1.scene1.changed.connect(c1_lambda)

        self.g_carrier2 = Graphics(self.grpCarrier2)
        self.g_carrier2.setObjectName("g_carrier2")
        self.g_carrier2.setGeometry(QtCore.QRect(10, 40, 361, 281))
        c2_lambda = lambda: self.update_carrier1(self.g_carrier2.img_array)
        self.g_carrier2.scene1.changed.connect(c2_lambda)

        self.scene_p = QGraphicsScene()


    def comp_check(self):
        if self.chkApplyCompression.isChecked():
            self.slideCompression.setEnabled(True)
            self.txtCompression.setEnabled(True)
            self.lblLevel.setEnabled(True)
            self.comp_level = self.slideCompression.value()
            self.update_payload(self.g_payload1.img_array)
        if not self.chkApplyCompression.isChecked():
            self.slideCompression.setEnabled(False)
            self.slideCompression.setValue(0)
            self.txtCompression.setEnabled(False)
            self.lblLevel.setEnabled(False)
            self.comp_level = -1
            self.update_payload(self.g_payload1.img_array)
        self.check_save()

    def level_change(self):
        self.txtCompression.setText(str(self.slideCompression.value()))
        self.comp_level = self.slideCompression.value()
        self.update_payload(self.g_payload1.img_array)
        self.check_save()

    def update_payload(self, img):
        try:
            self.payload = Payload(img, self.comp_level, None)
            self.txtPayloadSize.setText(str(len(self.payload.xml.encode("utf-8"))))
            self.valid_p1 = True
        except:
            self.txtPayloadSize.setText("0")
            self.valid_p1 = False
            self.btnSave.setEnabled(False)
        self.check_save()

    def update_carrier(self, img):
        try:
            self.carrier = Carrier(img)
        except:
            self.lblPayloadFound.setText("")
            self.chkOverride.setEnabled(False)
            self.txtCarrierSize.setText("0")
            self.valid_c1 = False
            self.btnSave.setEnabled(False)
        else:
            if self.carrier.payloadExists():
                self.lblPayloadFound.setText(">>>> Payload Found <<<<")
                self.chkOverride.setEnabled(True)
                self.txtCarrierSize.setText(str(int(self.carrier.img.size / 8)))
            else:
                self.lblPayloadFound.setText("")
                self.chkOverride.setEnabled(False)
                self.chkOverride.setChecked(False)
                self.txtCarrierSize.setText(str(int(self.carrier.img.size / 8)))
            self.valid_c1 = True
            self.check_save()

    def update_carrier1(self, img):
        try:
            self.carrier1 = Carrier(img)
        except:
            pass
        else:
            self.scene_p.clear()
            if self.carrier1.payloadExists():
                self.btnClean.setEnabled(True)
                self.btnExtract.setEnabled(True)
                self.lblCarrierEmpty.setText("")
            else:
                self.btnClean.setEnabled(False)
                self.btnExtract.setEnabled(False)
                self.lblCarrierEmpty.setText(">>>>Carrier Empty<<<<")

    def save_new(self):
        filePath, _ = QFileDialog.getSaveFileName(self, caption='Save img file ...', filter="PNG files (*.png)")
        if not filePath:
            return
        try:
            img = self.carrier.embedPayload(self.payload, self.chkOverride.isChecked())
        except ValueError:
            return
        imsave(filePath, img)

    def clean_img(self):
        self.carrier1 = Carrier(self.g_carrier2.img_array)
        self.carrier1.img = self.carrier1.clean()
        imsave(self.g_carrier2.path, self.carrier1.img)
        self.btnClean.setEnabled(False)
        self.btnExtract.setEnabled(False)
        self.lblCarrierEmpty.setText(">>>>Carrier Empty<<<<")

    def extract_img(self):
        self.carrier1 = Carrier(self.g_carrier2.img_array)
        self.payload1 = self.carrier1.extractPayload()
        imsave('temp.png', self.payload1.img)
        image = QPixmap('temp.png')
        self.scene_p.addPixmap(image)
        self.viewPayload2.setScene(self.scene_p)
        self.viewPayload2.fitInView(self.scene_p.itemsBoundingRect(), Qt.KeepAspectRatio)
        try:
            self.viewPayload2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.viewPayload2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        except:
            pass

    def check_save(self):
        if self.carrier is None or self.payload is None:
            self.btnSave.setEnabled(False)
        else:
            if self.carrier.payloadExists():
                if self.chkOverride.isEnabled():
                    if self.valid_p1 and self.valid_c1 and float(self.txtCarrierSize.text()) > float(self.txtPayloadSize.text()):
                        self.btnSave.setEnabled(True)
                    else:
                        self.btnSave.setEnabled(False)
            else:
                if self.valid_p1 and self.valid_c1 and float(self.txtCarrierSize.text()) > float(self.txtPayloadSize.text()):
                    self.btnSave.setEnabled(True)
                else:
                    self.btnSave.setEnabled(False)

class Graphics(QtGui.QGraphicsView):
    def __init__(self, parent):
        super(Graphics, self).__init__(parent)
        self.setAcceptDrops(True)
        self.img_array = None
        self.path = None
        self.scene1 = QGraphicsScene()

    def disp_img(self, path):
        try:
            img = imread(path)
            self.img_array = img
            self.path = path
        except:
            error = QtGui.QErrorMessage()
            error.showMessage('''File was not an image. Please use a valid image.''')
            error.exec_()
        else:
            if img is not None:
                image = QPixmap(path)
                self.scene1.clear()
                self.scene1.addPixmap(image)
                self.setScene(self.scene1)
                self.fitInView(self.scene1.itemsBoundingRect(), Qt.KeepAspectRatio)
                self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        self.disp_img(event.mimeData().urls()[0].toLocalFile())
        event.accept()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()


def main():
    currentApp = QApplication(sys.argv)
    currentForm = SteganographyApp()
    currentForm.show()
    currentApp.exec_()

if __name__ == "__main__":
    main()
