import sqlite3
import random

class ProductDB:
    def __init__(self, db_path="c:/work/electronics.db"):
        self.con = sqlite3.connect(db_path)
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS Product (
                id INTEGER PRIMARY KEY,
                name TEXT,
                price INTEGER
            );
        """)
        self.con.commit()

    def insert_product(self, product_id, name, price):
        self.cur.execute(
            "INSERT INTO Product (id, name, price) VALUES (?, ?, ?);",
            (product_id, name, price)
        )
        self.con.commit()

    def update_product(self, product_id, name=None, price=None):
        if name is not None and price is not None:
            self.cur.execute(
                "UPDATE Product SET name=?, price=? WHERE id=?;",
                (name, price, product_id)
            )
        elif name is not None:
            self.cur.execute(
                "UPDATE Product SET name=? WHERE id=?;",
                (name, product_id)
            )
        elif price is not None:
            self.cur.execute(
                "UPDATE Product SET price=? WHERE id=?;",
                (price, product_id)
            )
        self.con.commit()

    def delete_product(self, product_id):
        self.cur.execute(
            "DELETE FROM Product WHERE id=?;",
            (product_id,)
        )
        self.con.commit()

    def select_all(self):
        self.cur.execute("SELECT * FROM Product;")
        return self.cur.fetchall()

    def select_by_id(self, product_id):
        self.cur.execute("SELECT * FROM Product WHERE id=?;", (product_id,))
        return self.cur.fetchone()

    def close(self):
        self.con.close()

# 샘플 데이터 100개 생성 및 삽입
if __name__ == "__main__":
    db = ProductDB()
    # 이미 데이터가 있다면 중복 방지
    db.cur.execute("DELETE FROM Product;")
    db.con.commit()
    for i in range(1, 101):
        name = f"전자제품{i}"
        price = random.randint(10000, 1000000)
        db.insert_product(i, name, price)
    # 전체 데이터 출력
    for row in db.select_all():
        print(row)
    db.close()