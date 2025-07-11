import sys
import mysql.connector
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QTableView, QLabel, QLineEdit, QDateEdit, QComboBox, 
    QMessageBox, QStatusBar, QHeaderView, QGroupBox, QFormLayout
)
from PyQt6.QtCore import Qt, QAbstractTableModel, QDate
from PyQt6.QtGui import QAction, QIcon, QFont

class DatabaseManager:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="sqlPASSWORD123",
                password="sqlPASSWORD123",
                database="generaltourdatabaseCOPY",
                port=8888
            )
            self.cursor = self.connection.cursor(dictionary=True)
        except mysql.connector.Error as e:
            raise Exception(f"Ошибка подключения к MySQL: {e}")

    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params or ())
            if query.strip().lower().startswith("select"):
                return self.cursor.fetchall()
            self.connection.commit()
            return True
        except mysql.connector.Error as err:
            raise Exception(f"Ошибка запроса: {err}")

    def close(self):
        if hasattr(self, 'cursor'):
            self.cursor.close()
        if hasattr(self, 'connection') and self.connection.is_connected():
            self.connection.close()

class TableModel(QAbstractTableModel):
    def __init__(self, data, headers):
        super().__init__()
        self._data = data or []
        self._headers = headers or []

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._headers) if self._data else 0

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole and self._data:
            row = index.row()
            col = index.column()
            if row < len(self._data) and col < len(self._headers):
                return str(self._data[row].get(self._headers[col], ""))
        return None

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            return self._headers[section] if section < len(self._headers) else ""
        return None

class TourManagementApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.setup_database()
        self.load_data()

    def setup_ui(self):
        self.setWindowTitle("ТурМенеджер Pro")
        self.setGeometry(100, 100, 1000, 700)
        
        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Главный лейаут
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(10, 10, 10, 10)
        
        # Создаем табы
        self.tabs = QTabWidget()
        main_layout.addWidget(self.tabs)
        
        # Создаем вкладки
        self.create_tabs()
        
        # Статус бар
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        
        # Меню
        self.create_menu()
        
        # Применяем стили
        self.apply_styles()

    def setup_database(self):
        try:
            self.db = DatabaseManager()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось подключиться к базе данных:\n{str(e)}")
            self.close()

    def create_menu(self):
        menubar = self.menuBar()
        
        # Меню Файл
        file_menu = menubar.addMenu("Файл")
        refresh_action = QAction("Обновить данные", self)
        refresh_action.triggered.connect(self.load_data)
        file_menu.addAction(refresh_action)
        
        exit_action = QAction("Выход", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Меню Справка
        help_menu = menubar.addMenu("Справка")
        about_action = QAction("О программе", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)

    def create_tabs(self):
        self.create_tours_tab()
        self.create_customers_tab()
        self.create_cars_tab()
        self.create_drivers_tab()
        self.create_orders_tab()
        self.create_transfers_tab()

    def create_tours_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Таблица
        self.tour_table = QTableView()
        self.tour_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.tour_table)
        
        # Форма добавления
        form_group = QGroupBox("Добавить тур")
        form_layout = QFormLayout()
        
        self.tour_name_input = QLineEdit()
        self.tour_price_input = QLineEdit()
        self.fly_out_input = QDateEdit()
        self.fly_out_input.setDate(QDate.currentDate())
        self.fly_in_input = QDateEdit()
        self.fly_in_input.setDate(QDate.currentDate().addDays(7))
        self.operator_input = QLineEdit()
        self.destination_input = QLineEdit()
        self.airport_input = QLineEdit()
        
        form_layout.addRow("Название:", self.tour_name_input)
        form_layout.addRow("Цена:", self.tour_price_input)
        form_layout.addRow("Вылет:", self.fly_out_input)
        form_layout.addRow("Прилет:", self.fly_in_input)
        form_layout.addRow("Оператор:", self.operator_input)
        form_layout.addRow("Страна:", self.destination_input)
        form_layout.addRow("Аэропорт:", self.airport_input)
        
        add_btn = QPushButton("Добавить")
        add_btn.clicked.connect(self.add_tour)
        form_layout.addRow(add_btn)
        
        form_group.setLayout(form_layout)
        layout.addWidget(form_group)
        
        self.tabs.addTab(tab, "Туры")

    def create_customers_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        self.customer_table = QTableView()
        self.customer_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.customer_table)
        
        form_group = QGroupBox("Добавить клиента")
        form_layout = QFormLayout()
        
        self.customer_name_input = QLineEdit()
        self.customer_phone_input = QLineEdit()
        self.customer_passport_input = QLineEdit()
        
        form_layout.addRow("Имя:", self.customer_name_input)
        form_layout.addRow("Телефон:", self.customer_phone_input)
        form_layout.addRow("Паспорт:", self.customer_passport_input)
        
        add_btn = QPushButton("Добавить")
        add_btn.clicked.connect(self.add_customer)
        form_layout.addRow(add_btn)
        
        form_group.setLayout(form_layout)
        layout.addWidget(form_group)
        
        self.tabs.addTab(tab, "Клиенты")

    def create_cars_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        self.car_table = QTableView()
        self.car_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.car_table)
        
        form_group = QGroupBox("Добавить автомобиль")
        form_layout = QFormLayout()
        
        self.car_brand_input = QLineEdit()
        self.car_number_input = QLineEdit()
        self.car_color_input = QLineEdit()
        
        form_layout.addRow("Марка:", self.car_brand_input)
        form_layout.addRow("Номер:", self.car_number_input)
        form_layout.addRow("Цвет:", self.car_color_input)
        
        add_btn = QPushButton("Добавить")
        add_btn.clicked.connect(self.add_car)
        form_layout.addRow(add_btn)
        
        form_group.setLayout(form_layout)
        layout.addWidget(form_group)
        
        self.tabs.addTab(tab, "Автомобили")

    def create_drivers_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        self.driver_table = QTableView()
        self.driver_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.driver_table)
        
        form_group = QGroupBox("Добавить водителя")
        form_layout = QFormLayout()
        
        self.driver_name_input = QLineEdit()
        self.driver_phone_input = QLineEdit()
        
        form_layout.addRow("Имя:", self.driver_name_input)
        form_layout.addRow("Телефон:", self.driver_phone_input)
        
        add_btn = QPushButton("Добавить")
        add_btn.clicked.connect(self.add_driver)
        form_layout.addRow(add_btn)
        
        form_group.setLayout(form_layout)
        layout.addWidget(form_group)
        
        self.tabs.addTab(tab, "Водители")

    def create_orders_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        self.order_table = QTableView()
        self.order_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.order_table)
        
        form_group = QGroupBox("Создать заказ")
        form_layout = QFormLayout()
        
        self.order_customer_combo = QComboBox()
        self.order_tour_combo = QComboBox()
        
        form_layout.addRow("Клиент:", self.order_customer_combo)
        form_layout.addRow("Тур:", self.order_tour_combo)
        
        add_btn = QPushButton("Создать")
        add_btn.clicked.connect(self.add_order)
        form_layout.addRow(add_btn)
        
        form_group.setLayout(form_layout)
        layout.addWidget(form_group)
        
        self.tabs.addTab(tab, "Заказы")

    def create_transfers_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        self.transfer_table = QTableView()
        self.transfer_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.transfer_table)
        
        form_group = QGroupBox("Назначить трансфер")
        form_layout = QFormLayout()
        
        self.transfer_tour_combo = QComboBox()
        self.transfer_driver_combo = QComboBox()
        self.transfer_car_combo = QComboBox()
        
        form_layout.addRow("Тур:", self.transfer_tour_combo)
        form_layout.addRow("Водитель:", self.transfer_driver_combo)
        form_layout.addRow("Автомобиль:", self.transfer_car_combo)
        
        add_btn = QPushButton("Назначить")
        add_btn.clicked.connect(self.add_transfer)
        form_layout.addRow(add_btn)
        
        form_group.setLayout(form_layout)
        layout.addWidget(form_group)
        
        self.tabs.addTab(tab, "Трансферы")

    def apply_styles(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
            QGroupBox {
                border: 1px solid #ddd;
                border-radius: 5px;
                margin-top: 10px;
                padding-top: 15px;
                font-weight: bold;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 8px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QTableView {
                border: 1px solid #ddd;
                border-radius: 5px;
            }
            QHeaderView::section {
                background-color: #4CAF50;
                color: white;
                padding: 5px;
            }
        """)

    def load_data(self):
        try:
            # Загрузка туров
            tours = self.db.execute_query("SELECT * FROM tourtable")
            self.tour_table.setModel(TableModel(tours, [
                "idTour", "TourName", "Price", "FlyOutDate", "FlyInDate", 
                "Touroperator", "Destination_country", "Airport"
            ]))
            
            # Загрузка клиентов
            customers = self.db.execute_query("SELECT * FROM customerinfo")
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
            self.transfer_table.setModel(TableModel(transfers, [
                "Transfer_ID", "TourName", "DriverName", "CarBrand"
            ]))
            
            # Обновление комбобоксов
            self.order_tour_combo.clear()
            self.transfer_tour_combo.clear()
            for tour in tours:
                self.order_tour_combo.addItem(tour["TourName"], tour["idTour"])
                self.transfer_tour_combo.addItem(tour["TourName"], tour["idTour"])
            
            self.status_bar.showMessage("Данные успешно загружены", 3000)
            
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить данные:\n{str(e)}")
            self.status_bar.showMessage("Ошибка загрузки данных", 3000)

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
                QMessageBox.warning(self, "Ошибка", "Все поля должны быть заполнены")
                return
            
            if self.db.execute_query(query, params):
                QMessageBox.information(self, "Успех", "Тур успешно добавлен")
                self.load_data()
                self.clear_tour_form()
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
                QMessageBox.warning(self, "Ошибка", "Все поля должны быть заполнены")
                return
            
            if self.db.execute_query(query, params):
                QMessageBox.information(self, "Успех", "Клиент успешно добавлен")
                self.load_data()
                self.clear_customer_form()
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
                QMessageBox.warning(self, "Ошибка", "Все поля должны быть заполнены")
                return
            
            if self.db.execute_query(query, params):
                QMessageBox.information(self, "Успех", "Автомобиль успешно добавлен")
                self.load_data()
                self.clear_car_form()
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
                QMessageBox.warning(self, "Ошибка", "Все поля должны быть заполнены")
                return
            
            if self.db.execute_query(query, params):
                QMessageBox.information(self, "Успех", "Водитель успешно добавлен")
                self.load_data()
                self.clear_driver_form()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось добавить водителя:\n{str(e)}")

    def add_order(self):
        try:
            customer_id = self.order_customer_combo.currentData()
            tour_id = self.order_tour_combo.currentData()
            
            if not customer_id or not tour_id:
                QMessageBox.warning(self, "Ошибка", "Выберите клиента и тур")
                return
            
            # Сначала вставляем в orderinfo
            if self.db.execute_query("INSERT INTO orderinfo (Order_Number_Monthly, Order_Number_Yearly, Order_Number_All) VALUES (0, 0, 0)"):
                # Получаем последний вставленный ID
                self.db.cursor.execute("SELECT LAST_INSERT_ID() as id")
                order_id = self.db.cursor.fetchone()["id"]
                
                # Теперь вставляем в orderid
                query = """
                INSERT INTO orderid 
                (Order_Number, idOrder, customerID, Tour_ID) 
                VALUES (%s, %s, %s, %s)
                """
                if self.db.execute_query(query, (order_id, order_id, customer_id, tour_id)):
                    QMessageBox.information(self, "Успех", "Заказ успешно создан")
                    self.load_data()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось создать заказ:\n{str(e)}")

    def add_transfer(self):
        try:
            tour_id = self.transfer_tour_combo.currentData()
            driver_id = self.transfer_driver_combo.currentData()
            car_id = self.transfer_car_combo.currentData()
            
            if not all([tour_id, driver_id, car_id]):
                QMessageBox.warning(self, "Ошибка", "Выберите тур, водителя и автомобиль")
                return
            
            query = """
            INSERT INTO transferinfo 
            (tourID, driverID, CarID) 
            VALUES (%s, %s, %s)
            """
            if self.db.execute_query(query, (tour_id, driver_id, car_id)):
                QMessageBox.information(self, "Успех", "Трансфер успешно назначен")
                self.load_data()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось назначить трансфер:\n{str(e)}")

    def clear_tour_form(self):
        self.tour_name_input.clear()
        self.tour_price_input.clear()
        self.operator_input.clear()
        self.destination_input.clear()
        self.airport_input.clear()

    def clear_customer_form(self):
        self.customer_name_input.clear()
        self.customer_phone_input.clear()
        self.customer_passport_input.clear()

    def clear_car_form(self):
        self.car_brand_input.clear()
        self.car_number_input.clear()
        self.car_color_input.clear()

    def clear_driver_form(self):
        self.driver_name_input.clear()
        self.driver_phone_input.clear()

    def show_about(self):
        QMessageBox.about(self, "О программе", 
            "ТурМенеджер Pro\nВерсия 1.0\n\nПрограмма для управления туристическим бизнесом")

    def closeEvent(self, event):
        if hasattr(self, 'db'):
            self.db.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    try:
        window = TourManagementApp()
        window.show()
        sys.exit(app.exec())
    except Exception as e:
        QMessageBox.critical(None, "Ошибка", f"Не удалось запустить приложение:\n{str(e)}")
        sys.exit(1)