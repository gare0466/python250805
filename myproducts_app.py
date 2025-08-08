import sys
import sqlite3
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QMessageBox
)
from PyQt5.QtCore import Qt

DB_PATH = "myproducts.db"

class ProductApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("전자제품 관리 프로그램")
        self.setGeometry(100, 100, 600, 500)
        self.conn = sqlite3.connect(DB_PATH)
        self.cur = self.conn.cursor()
        self.create_table()
        self.initUI()
        self.load_products()

    def create_table(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS myproducts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price INTEGER NOT NULL
            );
        """)
        self.conn.commit()

    def initUI(self):
        # 입력 폼
        lbl_id = QLabel("ID:")
        self.le_id = QLineEdit()
        self.le_id.setReadOnly(True)
        lbl_name = QLabel("제품명:")
        self.le_name = QLineEdit()
        lbl_price = QLabel("가격:")
        self.le_price = QLineEdit()

        # 버튼
        btn_add = QPushButton("입력")
        btn_update = QPushButton("수정")
        btn_delete = QPushButton("삭제")
        btn_search = QPushButton("검색")

        btn_add.clicked.connect(self.add_product)
        btn_update.clicked.connect(self.update_product)
        btn_delete.clicked.connect(self.delete_product)
        btn_search.clicked.connect(self.search_product)

        # 입력 레이아웃
        form_layout = QHBoxLayout()
        form_layout.addWidget(lbl_id)
        form_layout.addWidget(self.le_id)
        form_layout.addWidget(lbl_name)
        form_layout.addWidget(self.le_name)
        form_layout.addWidget(lbl_price)
        form_layout.addWidget(self.le_price)
        form_layout.addWidget(btn_add)
        form_layout.addWidget(btn_update)
        form_layout.addWidget(btn_delete)
        form_layout.addWidget(btn_search)

        # 테이블
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID", "제품명", "가격"])
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.cellClicked.connect(self.table_cell_clicked)

        # 전체 레이아웃
        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.table)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def add_product(self):
        name = self.le_name.text().strip()
        price = self.le_price.text().strip()
        if not name or not price.isdigit():
            QMessageBox.warning(self, "입력 오류", "제품명과 가격을 올바르게 입력하세요.")
            return
        self.cur.execute("INSERT INTO myproducts (name, price) VALUES (?, ?)", (name, int(price)))
        self.conn.commit()
        self.le_name.clear()
        self.le_price.clear()
        self.load_products()

    def update_product(self):
        id_ = self.le_id.text().strip()
        name = self.le_name.text().strip()
        price = self.le_price.text().strip()
        if not id_ or not name or not price.isdigit():
            QMessageBox.warning(self, "입력 오류", "ID, 제품명, 가격을 올바르게 입력하세요.")
            return
        self.cur.execute("UPDATE myproducts SET name=?, price=? WHERE id=?", (name, int(price), int(id_)))
        self.conn.commit()
        self.le_id.clear()
        self.le_name.clear()
        self.le_price.clear()
        self.load_products()

    def delete_product(self):
        id_ = self.le_id.text().strip()
        if not id_:
            QMessageBox.warning(self, "입력 오류", "삭제할 ID를 선택하세요.")
            return
        self.cur.execute("DELETE FROM myproducts WHERE id=?", (int(id_),))
        self.conn.commit()
        self.le_id.clear()
        self.le_name.clear()
        self.le_price.clear()
        self.load_products()

    def search_product(self):
        name = self.le_name.text().strip()
        if not name:
            self.load_products()
            return
        self.cur.execute("SELECT * FROM myproducts WHERE name LIKE ?", ('%' + name + '%',))
        rows = self.cur.fetchall()
        self.show_products(rows)

    def load_products(self):
        self.cur.execute("SELECT * FROM myproducts")
        rows = self.cur.fetchall()
        self.show_products(rows)

    def show_products(self, rows):
        self.table.setRowCount(len(rows))
        for row_idx, row in enumerate(rows):
            self.table.setItem(row_idx, 0, QTableWidgetItem(str(row[0])))
            self.table.setItem(row_idx, 1, QTableWidgetItem(row[1]))
            self.table.setItem(row_idx, 2, QTableWidgetItem(str(row[2])))

    def table_cell_clicked(self, row, col):
        self.le_id.setText(self.table.item(row, 0).text())
        self.le_name.setText(self.table.item(row, 1).text())
        self.le_price.setText(self.table.item(row, 2).text())

    def closeEvent(self, event):
        self.conn.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ProductApp()
    win.show()
    sys.exit(app.exec_())