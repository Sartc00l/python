import sys
import mysql.connector
from mysql.connector import Error
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QTableView, QLabel, QLineEdit, QDateEdit, QComboBox, 
    QMessageBox, QStatusBar, QHeaderView
)
from PyQt6.QtCore import Qt, QAbstractTableModel
from PyQt6.QtGui import QAction

class DatabaseManager:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="sqlPASSWORD123",
                password="123",
                database="generaltourdatabaseCOPY",
                port=8889
            )
            self.cursor = self.connection.cursor(dictionary=True)
            print("Успешное подключение к базе данных")
        except Error as e:
            print(f"Ошибка подключения к MySQL: {e}")
            raise

    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params or ())
            if query.strip().lower().startswith("select"):
                return self.cursor.fetchall()
            self.connection.commit()
            return True
        except Error as err:
            print(f"Ошибка базы данных: {err}")
            return False

    def close(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()

class TableModel(QAbstractTableModel):
    def __init__(self, data, headers):
        super().__init__()
        self._data = data
        self._headers = headers
    
    def rowCount(self, parent=None):
        return len(self._data)
    
    def columnCount(self, parent=None):
        return len(self._headers)
    
    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            return str(self._data[index.row()][self._headers[index.column()]])
        return None
    
    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            return self._headers[section]
        return None

class TourManagementApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        try:
            self.db = DatabaseManager()
            self.setWindowTitle("Система управления турами")
            self.setGeometry(100, 100, 1200, 800)
            
            self.statusBar().showMessage("Готово")
            self.init_ui()
            self.load_data()
        
        except Exception as e:
            QMessageBox.critical(None, "Ошибка базы данных", 
                f"Не удалось инициализировать приложение:\n{str(e)}")
            sys.exit(1)

    def init_ui(self):
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        
        # Создаем все вкладки
        self.create_tours_tab()
        self.create_customers_tab()
        self.create_cars_tab()
        self.create_drivers_tab()
        self.create_orders_tab()
        self.create_transfers_tab()
        self.uiDELETE()
        
        self.create_menu_bar()

    def create_menu_bar(self):
        menubar = self.menuBar()
        
        # Меню Файл
        file_menu = menubar.addMenu("Файл")
        exit_action = QAction("Выход", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Меню Справка
        help_menu = menubar.addMenu("Справка")
        about_action = QAction("О программе", self)
        about_action.triggered.connect(lambda: QMessageBox.about(self, "О программе", "Система управления турами v1.0"))
        help_menu.addAction(about_action)
        
        calcuate_menu  = menubar.addMenu("Бухгалтерия")
        calc_action = QAction("Бухгалтерия",self)
        calc_action.triggered.connect(lambda: QMessageBox.about(self,"Абаюднда","Абаюндаv228"))
        calcuate_menu.addAction(calc_action)

    def create_tours_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        
        # Таблица
        self.tour_table = QTableView()
        self.tour_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.tour_table)
        
        # Форма
        form_layout = QHBoxLayout()
        
        self.tour_name_input = QLineEdit(placeholderText="Название тура")
        self.tour_price_input = QLineEdit(placeholderText="Цена")
        self.fly_out_input = QDateEdit()
        self.fly_in_input = QDateEdit()
        self.operator_input = QLineEdit(placeholderText="Туроператор")
        self.destination_input = QLineEdit(placeholderText="Страна назначения")
        self.airport_input = QLineEdit(placeholderText="Аэропорт")
        
        add_btn = QPushButton("Добавить тур")
        add_btn.clicked.connect(self.add_tour)
        
        form_layout.addWidget(QLabel("Название:"))
        form_layout.addWidget(self.tour_name_input)
        form_layout.addWidget(QLabel("Цена:"))
        form_layout.addWidget(self.tour_price_input)
        form_layout.addWidget(QLabel("Вылет:"))
        form_layout.addWidget(self.fly_out_input)
        form_layout.addWidget(QLabel("Прилет:"))
        form_layout.addWidget(self.fly_in_input)
        form_layout.addWidget(QLabel("Оператор:"))
        form_layout.addWidget(self.operator_input)
        form_layout.addWidget(QLabel("Страна:"))
        form_layout.addWidget(self.destination_input)
        form_layout.addWidget(QLabel("Аэропорт:"))
        form_layout.addWidget(self.airport_input)
        form_layout.addWidget(add_btn)
        
        layout.addLayout(form_layout)
        tab.setLayout(layout)
        self.tabs.addTab(tab, "Туры")

    def create_customers_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        
        self.customer_table = QTableView()
        self.customer_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.customer_table)
        
        form_layout = QHBoxLayout()
        
        self.customer_name_input = QLineEdit(placeholderText="Имя клиента")
        self.customer_phone_input = QLineEdit(placeholderText="Телефон")
        self.customer_passport_input = QLineEdit(placeholderText="Паспорт")
        
        add_btn = QPushButton("Добавить клиента")
        add_btn.clicked.connect(self.add_customer)
        
        form_layout.addWidget(QLabel("Имя:"))
        form_layout.addWidget(self.customer_name_input)
        form_layout.addWidget(QLabel("Телефон:"))
        form_layout.addWidget(self.customer_phone_input)
        form_layout.addWidget(QLabel("Паспорт:"))
        form_layout.addWidget(self.customer_passport_input)
        form_layout.addWidget(add_btn)
        
        layout.addLayout(form_layout)
        tab.setLayout(layout)
        self.tabs.addTab(tab, "Клиенты")

    def create_cars_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        
        self.car_table = QTableView()
        self.car_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.car_table)
        
        form_layout = QHBoxLayout()
        
        self.car_brand_input = QLineEdit(placeholderText="Марка")
        self.car_number_input = QLineEdit(placeholderText="Номер")
        self.car_color_input = QLineEdit(placeholderText="Цвет")
        
        add_btn = QPushButton("Добавить авто")
        add_btn.clicked.connect(self.add_car)
        
        form_layout.addWidget(QLabel("Марка:"))
        form_layout.addWidget(self.car_brand_input)
        form_layout.addWidget(QLabel("Номер:"))
        form_layout.addWidget(self.car_number_input)
        form_layout.addWidget(QLabel("Цвет:"))
        form_layout.addWidget(self.car_color_input)
        form_layout.addWidget(add_btn)
        
        layout.addLayout(form_layout)
        tab.setLayout(layout)
        self.tabs.addTab(tab, "Автомобили")

    def uiDELETE(self):
        tab = QWidget()
        layout = QVBoxLayout()
        self.table = QTableView()
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.table)
        
        btn = QPushButton("Press")
        layout.addWidget(btn)
        
        tab.setLayout(layout)
        self.tabs.addTab(tab,"huinya")
   
        
        


    def create_drivers_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        
        self.driver_table = QTableView()
        self.driver_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.driver_table)
        
        form_layout = QHBoxLayout()
        
        self.driver_name_input = QLineEdit(placeholderText="Имя водителя")
        self.driver_phone_input = QLineEdit(placeholderText="Телефон")
        
        add_btn = QPushButton("Добавить водителя")
        add_btn.clicked.connect(self.add_driver)
        
        form_layout.addWidget(QLabel("Имя:"))
        form_layout.addWidget(self.driver_name_input)
        form_layout.addWidget(QLabel("Телефон:"))
        form_layout.addWidget(self.driver_phone_input)
        form_layout.addWidget(add_btn)
        
        layout.addLayout(form_layout)
        tab.setLayout(layout)
        self.tabs.addTab(tab, "Водители")

    def create_orders_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        
        self.order_table = QTableView()
        self.order_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.order_table)
        
        form_layout = QHBoxLayout()
        
        self.order_customer_combo = QComboBox()
        self.order_tour_combo = QComboBox()
        
        add_btn = QPushButton("Создать заказ")
        add_btn.clicked.connect(self.add_order)
        
        form_layout.addWidget(QLabel("Клиент:"))
        form_layout.addWidget(self.order_customer_combo)
        form_layout.addWidget(QLabel("Тур:"))
        form_layout.addWidget(self.order_tour_combo)
        form_layout.addWidget(add_btn)
        
        layout.addLayout(form_layout)
        tab.setLayout(layout)
        self.tabs.addTab(tab, "Заказы")

    def create_transfers_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        
        self.transfer_table = QTableView()
        self.transfer_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.transfer_table)
        
        form_layout = QHBoxLayout()
        
        self.transfer_tour_combo = QComboBox()
        self.transfer_driver_combo = QComboBox()
        self.transfer_car_combo = QComboBox()
        
        add_btn = QPushButton("Назначить трансфер")
        add_btn.clicked.connect(self.add_transfer)
        
        form_layout.addWidget(QLabel("Тур:"))
        form_layout.addWidget(self.transfer_tour_combo)
        form_layout.addWidget(QLabel("Водитель:"))
        form_layout.addWidget(self.transfer_driver_combo)
        form_layout.addWidget(QLabel("Авто:"))
        form_layout.addWidget(self.transfer_car_combo)
        form_layout.addWidget(add_btn)
        
        layout.addLayout(form_layout)
        tab.setLayout(layout)
        self.tabs.addTab(tab, "Трансферы")

    def load_data(self):
        # Загрузка туров
        tours = self.db.execute_query("SELECT * FROM tourtable")
        if tours:
            self.tour_table.setModel(TableModel(tours, [
                "idTour", "TourName", "Price", "FlyOutDate", "FlyInDate", 
                "Touroperator", "Destination_country", "Airport"
            ]))
        
        # Загрузка клиентов
        customers = self.db.execute_query("SELECT * FROM customerinfo")
        if customers:
            self.customer_table.setModel(TableModel(customers, [
                "IdCustomer", "CustomerName", "CustomerPhone", "CustomerPassport"
            ]))
            self.order_customer_combo.clear()
            for customer in customers:
                self.order_customer_combo.addItem(
                    f"{customer['CustomerName']} ({customer['CustomerPhone']})", 
                    customer['IdCustomer']
                )
        
        # Загрузка автомобилей
        cars = self.db.execute_query("SELECT * FROM carinfo")
        if cars:
            self.car_table.setModel(TableModel(cars, [
                "CarID", "CarBrand", "CarNumber", "CarColor"
            ]))
            self.transfer_car_combo.clear()
            for car in cars:
                self.transfer_car_combo.addItem(
                    f"{car['CarBrand']} ({car['CarNumber']})", 
                    car['CarID']
                )
        
        # Загрузка водителей
        drivers = self.db.execute_query("SELECT * FROM drivertransferinfo")
        if drivers:
            self.driver_table.setModel(TableModel(drivers, [
                "idDriver", "DriverName", "DriverPhoneNumber"
            ]))
            self.transfer_driver_combo.clear()
            for driver in drivers:
                self.transfer_driver_combo.addItem(
                    f"{driver['DriverName']} ({driver['DriverPhoneNumber']})", 
                    driver['idDriver']
                )
        
        # Загрузка заказов
        orders = self.db.execute_query("""
            SELECT o.Order_Number, c.CustomerName, t.TourName 
            FROM orderid o
            JOIN customerinfo c ON o.customerID = c.IdCustomer
            JOIN tourtable t ON o.Tour_ID = t.idTour
        """)
        if orders:
            self.order_table.setModel(TableModel(orders, [
                "Order_Number", "CustomerName", "TourName"
            ]))
        
        # Загрузка трансферов
        transfers = self.db.execute_query("""
            SELECT tf.Transfer_ID, t.TourName, d.DriverName, c.CarBrand 
            FROM transferinfo tf
            JOIN tourtable t ON tf.tourID = t.idTour
            JOIN drivertransferinfo d ON tf.driverID = d.idDriver
            JOIN carinfo c ON tf.CarID = c.CarID
        """)
        if transfers:
            self.transfer_table.setModel(TableModel(transfers, [
                "Transfer_ID", "TourName", "DriverName", "CarBrand"
            ]))
        
        # Загрузка комбобоксов
        if tours:
            self.order_tour_combo.clear()
            self.transfer_tour_combo.clear()
            for tour in tours:
                self.order_tour_combo.addItem(tour["TourName"], tour["idTour"])
                self.transfer_tour_combo.addItem(tour["TourName"], tour["idTour"])

    def add_tour(self):
        try:
            query = """
            INSERT INTO tourtable 
            (TourName, Price, FlyOutDate, FlyInDate, Touroperator, Destination_country, Airport) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            params = (
                self.tour_name_input.text(),
                self.tour_price_input.text(),
                self.fly_out_input.date().toString("yyyy-MM-dd"),
                self.fly_in_input.date().toString("yyyy-MM-dd"),
                self.operator_input.text(),
                self.destination_input.text(),
                self.airport_input.text()
            )
            
            if not all(params):
                QMessageBox.warning(self, "Предупреждение", "Все поля обязательны для заполнения!")
                return
            
            if self.db.execute_query(query, params):
                QMessageBox.information(self, "Успех", "Тур успешно добавлен!")
                self.load_data()
                self.tour_name_input.clear()
                self.tour_price_input.clear()
                self.operator_input.clear()
                self.destination_input.clear()
                self.airport_input.clear()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось добавить тур:\n{str(e)}")

    def add_customer(self):
        try:
            query = """
            INSERT INTO customerinfo 
            (CustomerName, CustomerPhone, CustomerPassport) 
            VALUES (%s, %s, %s)
            """
            params = (
                self.customer_name_input.text(),
                self.customer_phone_input.text(),
                self.customer_passport_input.text()
            )
            
            if not all(params):
                QMessageBox.warning(self, "Предупреждение", "Все поля обязательны для заполнения!")
                return
            
            if self.db.execute_query(query, params):
                QMessageBox.information(self, "Успех", "Клиент успешно добавлен!")
                self.load_data()
                self.customer_name_input.clear()
                self.customer_phone_input.clear()
                self.customer_passport_input.clear()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось добавить клиента:\n{str(e)}")

    def add_car(self):
        try:
            query = """
            INSERT INTO carinfo 
            (CarBrand, CarNumber, CarColor) 
            VALUES (%s, %s, %s)
            """
            params = (
                self.car_brand_input.text(),
                self.car_number_input.text(),
                self.car_color_input.text()
            )
            
            if not all(params):
                QMessageBox.warning(self, "Предупреждение", "Все поля обязательны для заполнения!")
                return
            
            if self.db.execute_query(query, params):
                QMessageBox.information(self, "Успех", "Автомобиль успешно добавлен!")
                self.load_data()
                self.car_brand_input.clear()
                self.car_number_input.clear()
                self.car_color_input.clear()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось добавить автомобиль:\n{str(e)}")

    def add_driver(self):
        try:
            query = """
            INSERT INTO drivertransferinfo 
            (DriverName, DriverPhoneNumber) 
            VALUES (%s, %s)
            """
            params = (
                self.driver_name_input.text(),
                self.driver_phone_input.text()
            )
            
            if not all(params):
                QMessageBox.warning(self, "Предупреждение", "Все поля обязательны для заполнения!")
                return
            
            if self.db.execute_query(query, params):
                QMessageBox.information(self, "Успех", "Водитель успешно добавлен!")
                self.load_data()
                self.driver_name_input.clear()
                self.driver_phone_input.clear()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось добавить водителя:\n{str(e)}")

    def add_order(self):
        try:
            customer_id = self.order_customer_combo.currentData()
            tour_id = self.order_tour_combo.currentData()
            
            if not customer_id or not tour_id:
                QMessageBox.warning(self, "Предупреждение", "Пожалуйста, выберите клиента и тур!")
                return
            
            # Сначала вставляем в orderinfo
            orderinfo_query = "INSERT INTO orderinfo (Order_Number_Monthly, Order_Number_Yearly, Order_Number_All) VALUES (0, 0, 0)"
            if self.db.execute_query(orderinfo_query):
                # Получаем последний вставленный ID
                self.db.cursor.execute("SELECT LAST_INSERT_ID() as id")
                order_id = self.db.cursor.fetchone()["id"]
                
                # Теперь вставляем в orderid
                orderid_query = """
                INSERT INTO orderid 
                (Order_Number, idOrder, customerID, Tour_ID) 
                VALUES (%s, %s, %s, %s)
                """
                if self.db.execute_query(orderid_query, (order_id, order_id, customer_id, tour_id)):
                    QMessageBox.information(self, "Успех", "Заказ успешно создан!")
                    self.load_data()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось создать заказ:\n{str(e)}")
    
    def add_transfer(self):
        try:
            tour_id = self.transfer_tour_combo.currentData()
            driver_id = self.transfer_driver_combo.currentData()
            car_id = self.transfer_car_combo.currentData()
            
            if not all([tour_id, driver_id, car_id]):
                QMessageBox.warning(self, "Предупреждение", "Пожалуйста, выберите тур, водителя и автомобиль!")
                return
            
            query = """
            INSERT INTO transferinfo 
            (tourID, driverID, CarID) 
            VALUES (%s, %s, %s)
            """
            if self.db.execute_query(query, (tour_id, driver_id, car_id)):
                QMessageBox.information(self, "Успех", "Трансфер успешно назначен!")
                self.load_data()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось назначить трансфер:\n{str(e)}")

    def closeEvent(self, event):
        self.db.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    try:
        window = TourManagementApp()
        window.show()
        sys.exit(app.exec())
    except Exception as e:
        QMessageBox.critical(None, "Критическая ошибка", f"Приложение не смогло запуститься:\n{str(e)}")
        sys.exit(1)