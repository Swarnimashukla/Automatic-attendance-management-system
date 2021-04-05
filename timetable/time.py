import sys
import os
import csv
from PyQt5.QtWidgets import QTableWidget, QApplication, QMainWindow, QTableWidgetItem, QFileDialog
from PyQt5.QtWidgets import qApp, QAction


class MyTable(QTableWidget):
    def __init__(self, r, c):
        super().__init__(r, c)
        self.check_change = True
        self.init_ui()

    def init_ui(self):
        self.cellChanged.connect(self.c_current)
        self.show()

    def c_current(self):
        if self.check_change:
            row = self.currentRow()
            col = self.currentColumn()
            value = self.item(row, col)
            value = value.text()
            print("The current cell is ", row, ", ", col)
            print("In this cell we have: ", value)

    def open_sheet(self):
        self.check_change = False
        path = '/home/suyash/PycharmProjects/guitutorials/final_gui_demo/time_table.csv'
        if path != '':
            with open(path, newline='') as csv_file:
                self.setRowCount(0)
                self.setColumnCount(10)
                my_file = csv.reader(csv_file, dialect='excel')
                for row_data in my_file:
                    row = self.rowCount()
                    self.insertRow(row)
                    if len(row_data) > 10:
                        self.setColumnCount(len(row_data))
                    for column, stuff in enumerate(row_data):
                        item = QTableWidgetItem(stuff)
                        self.setItem(row, column, item)
        self.check_change = True

    def save_sheet(self):
        path = '/home/suyash/PycharmProjects/guitutorials/final_gui_demo/time_table.csv'
        if path != '':
            with open(path, 'w') as csv_file:
                writer = csv.writer(csv_file, dialect='excel')
                for row in range(self.rowCount()):
                    row_data = []
                    for column in range(self.columnCount()):
                        item = self.item(row, column)
                        if item is not None:
                            row_data.append(item.text())
                        else:
                            row_data.append('')
                    writer.writerow(row_data)


class Sheet(QMainWindow):
    def __init__(self):
        super().__init__()

        self.form_widget = MyTable(10, 10)
        self.setCentralWidget(self.form_widget)
        col_headers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        self.form_widget.setHorizontalHeaderLabels(col_headers)

        # Set up menu
        bar = self.menuBar()
        file = bar.addMenu('File')

        save_action = QAction('&Save', self)
        save_action.setShortcut('Ctrl+S')

        open_action = QAction('&Open', self)

        quit_action = QAction('&Quit', self)

        file.addAction(save_action)
        file.addAction(open_action)
        file.addAction(quit_action)

        quit_action.triggered.connect(self.quit_app)
        save_action.triggered.connect(self.form_widget.save_sheet)
        open_action.triggered.connect(self.form_widget.open_sheet)
        self.show()

    def quit_app(self):
        qApp.quit()

app = QApplication(sys.argv)
sheet = Sheet()
sys.exit(app.exec_())
