import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Criador de Janelas")
        self.setGeometry(100, 100, 400, 200)

        self.width_label = QLabel("Largura:", self)
        self.width_label.setGeometry(50, 50, 100, 30)

        self.height_label = QLabel("Altura:", self)
        self.height_label.setGeometry(50, 90, 100, 30)

        self.width_input = QLineEdit(self)
        self.width_input.setGeometry(150, 50, 100, 30)

        self.height_input = QLineEdit(self)
        self.height_input.setGeometry(150, 90, 100, 30)

        self.create_button = QPushButton("Criar Janela", self)
        self.create_button.setGeometry(50, 130, 100, 30)
        self.create_button.clicked.connect(self.create_new_window)

        self.open_windows = []  # Lista para manter referências das janelas abertas

    def create_new_window(self):
        try:
            width = int(self.width_input.text())
            height = int(self.height_input.text())
            new_window = NewWindow(width, height)
            self.open_windows.append(new_window)  # Adicionar a nova janela à lista
            new_window.show()
        except ValueError:
            pass


class NewWindow(QWidget):
    def __init__(self, width, height):
        super().__init__()

        self.setWindowTitle("Nova Janela")
        self.setGeometry(200, 200, width, height)

        label = QLabel(f"Esta é uma nova janela com dimensões {width}x{height} pixels.", self)
        label.setGeometry(50, 50, width, 30)

        close_button = QPushButton("Fechar", self)
        close_button.setGeometry(50, 100, 100, 30)
        close_button.clicked.connect(self.close_window)

    def close_window(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
