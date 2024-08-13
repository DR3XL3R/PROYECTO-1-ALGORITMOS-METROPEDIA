from Menu import Menu
import asyncio

class Main:

    def run(self) -> None:
        # Crea una instancia del menú y ejecuta el menú principal de forma asíncrona
        menu: Menu = Menu()
        asyncio.run(menu.runMenu())

main: Main = Main()
main.run()
