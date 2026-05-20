import sys
import os

# Adiciona o diretório atual ao path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from controllers.main_controller import MainController

if __name__ == "__main__":
    app = MainController()
    app.run()