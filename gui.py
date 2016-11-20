from PyQt4 import uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import converter

import os
import sys

current_dir = os.path.dirname(__file__)

Ui_FormClass, UiFormBase = \
    uic.loadUiType(os.path.join(current_dir, "mainwindow.ui"))


class Window(Ui_FormClass, UiFormBase):
    """
    Main program window.
    """

    def __init__(self, app):
        super(Window, self).__init__()
        self.setupUi(self)
        self.app = app

    @pyqtSlot()
    def on_select_button_clicked(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.AnyFile)
        file_dialog.setFilter("Avi file (*.avi)")

        if file_dialog.exec_():
            filename = str(file_dialog.selectedFiles()[0])
            self.line_open_path.setText(filename)
            file_dialog.close()

    @pyqtSlot()
    def on_output_button_clicked(self):
        name = QFileDialog.getSaveFileName(parent=self, caption='Save File')
        self.line_save_path.setText(name)

        return

    @pyqtSlot()
    def on_convert_button_clicked(self):
        input = "%s" % self.line_open_path.text()
        output = "%s" % self.line_save_path.text()

        type = ""
        if self.mpeg_radio_button.isChecked():
            type = "MPEG"
        elif self.mjpeg_radio_button.isChecked():
            type = "MJPEG"

        # delete if exists
        if os.path.exists(output):
            os.remove(output)

        conv = converter.Converter(input, output, type)
        conv.start()

        # alert
        QMessageBox.about(self, "Result", "Successful converted")


def main():
    app = QApplication(sys.argv)
    win = Window(app)
    win.show()
    app.exec_()


if __name__ == '__main__':
    main()
