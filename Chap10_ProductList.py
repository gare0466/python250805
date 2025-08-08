import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import uic
import sqlite3
import os.path

# DB파일이 없으면 만들고 있다면 접속한다.
db_path = "ProductList.db"
con = sqlite3.connect(db_path)
cur = con.cursor()
cur.execute(
    "CREATE TABLE IF NOT EXISTS Products (id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Price INTEGER);"
)

# 디자인 파일을 로딩
form_class = uic.loadUiType("Chap10_ProductList.ui")[0]

class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # QTableWidget의 컬럼폭 셋팅하기
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setHorizontalHeaderLabels(["제품ID", "제품명", "가격"])
        self.tableWidget.setTabKeyNavigation(False)

        # 엔터키를 클릭하면 다음 컨트롤로 이동
        self.prodID.returnPressed.connect(lambda: self.focusNextChild())
        self.prodName.returnPressed.connect(lambda: self.focusNextChild())
        self.prodPrice.returnPressed.connect(lambda: self.focusNextChild())

        # 더블클릭 시그널 처리
        self.tableWidget.doubleClicked.connect(self.doubleClick)

        # 버튼 연결 (추가, 수정, 삭제, 검색)
        self.pushButton.clicked.connect(self.addProduct)
        self.pushButton_2.clicked.connect(self.updateProduct)
        self.pushButton_3.clicked.connect(self.removeProduct)
        self.pushButton_4.clicked.connect(self.getProduct)

        # 초기 데이터 로딩
        self.getProduct()

    def addProduct(self):
        name = self.prodName.text()
        price = self.prodPrice.text()
        if not name or not price.isdigit():
            QMessageBox.warning(self, "입력 오류", "제품명과 가격을 올바르게 입력하세요.")
            return
        cur.execute("INSERT INTO Products (Name, Price) VALUES (?, ?);", (name, int(price)))
        con.commit()
        self.getProduct()

    def updateProduct(self):
        id_ = self.prodID.text()
        name = self.prodName.text()
        price = self.prodPrice.text()
        if not id_.isdigit() or not name or not price.isdigit():
            QMessageBox.warning(self, "입력 오류", "제품ID, 제품명, 가격을 올바르게 입력하세요.")
            return
        cur.execute("UPDATE Products SET Name=?, Price=? WHERE id=?;", (name, int(price), int(id_)))
        con.commit()
        self.getProduct()

    def removeProduct(self):
        id_ = self.prodID.text()
        if not id_.isdigit():
            QMessageBox.warning(self, "입력 오류", "제품ID를 올바르게 입력하세요.")
            return
        cur.execute("DELETE FROM Products WHERE id=?;", (int(id_),))
        con.commit()
        self.getProduct()

    def getProduct(self):
        cur.execute("SELECT * FROM Products;")
        rows = cur.fetchall()
        self.tableWidget.setRowCount(len(rows))
        for row_idx, item in enumerate(rows):
            itemID = QTableWidgetItem(str(item[0]))
            itemID.setTextAlignment(Qt.AlignRight)
            self.tableWidget.setItem(row_idx, 0, itemID)
            self.tableWidget.setItem(row_idx, 1, QTableWidgetItem(item[1]))
            itemPrice = QTableWidgetItem(str(item[2]))
            itemPrice.setTextAlignment(Qt.AlignRight)
            self.tableWidget.setItem(row_idx, 2, itemPrice)

    def doubleClick(self):
        row = self.tableWidget.currentRow()
        self.prodID.setText(self.tableWidget.item(row, 0).text())
        self.prodName.setText(self.tableWidget.item(row, 1).text())
        self.prodPrice.setText(self.tableWidget.item(row, 2).text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    sys.exit(app.exec_())




