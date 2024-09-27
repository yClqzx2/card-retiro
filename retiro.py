import time
import random
import os
from abc import ABC, abstractmethod

class Colors:
    """Clase para definir colores ANSI utilizados en la terminal."""
    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    BOLD_GREEN = "\033[1;32m"
    BOLD_YELLOW = "\033[1;33m"
    BOLD_CYAN = "\033[1;36m"

class CodeGenerator(ABC):

    @abstractmethod
    def generate_code(self) -> str:
        pass

    @staticmethod
    def generate_verification_code() -> str:
        return ''.join(random.choices('0123456789', k=4))

    @staticmethod
    def generate_amount() -> int:
        return random.randint(1, 10000)

class BBVACodeGenerator(CodeGenerator):

    @staticmethod
    def generate_code() -> str:
        return '112' + ''.join(random.choices('0123456789', k=16))

class UserInterface:

    @staticmethod
    def slow_print(text: str, delay: float = 0.05) -> None:
        for char in text:
            print(char, end="", flush=True)
            time.sleep(delay)
        print()

    @staticmethod
    def print_line(char: str = '-', length: int = 60, color: str = Colors.OKBLUE) -> None:
        print(f"{color}{char * length}{Colors.RESET}")

    @staticmethod
    def loading_animation(text: str, duration: int = 5) -> None:
        print(f"{text} ", end="", flush=True)
        for _ in range(duration):
            for symbol in "|/-\\":
                print(f"\033[94m{symbol}\033[0m", end="\r", flush=True)
                time.sleep(0.1)

    @staticmethod
    def display_message(header: str, message: str, color_header: str = Colors.BOLD_CYAN, color_message: str = Colors.OKGREEN) -> None:
        UserInterface.print_line(char='-', length=60, color=color_header)
        UserInterface.slow_print(f"{color_header}{header}{Colors.RESET}")
        UserInterface.print_line(char='-', length=60, color=color_header)
        UserInterface.slow_print(f"{color_message}{message}{Colors.RESET}")
        UserInterface.print_line(char='-', length=60, color=color_header)

    @staticmethod
    def get_valid_filename() -> str:
        while True:
            filename = input(f"{Colors.OKCYAN}Introduce el nombre del archivo donde guardar los códigos (debe terminar en .txt): {Colors.RESET}")
            if filename.endswith(".txt"):
                return filename
            else:
                UserInterface.display_message(
                    header="Error",
                    message="El nombre del archivo debe terminar en '.txt'. Intenta nuevamente.",
                    color_message=Colors.FAIL
                )

    @staticmethod
    def get_valid_number(prompt: str) -> int:
        """Solicita al usuario un número válido."""
        while True:
            try:
                num = int(input(prompt))
                if num > 0:
                    return num
                else:
                    UserInterface.display_message(
                        header="Error",
                        message="El número debe ser positivo.",
                        color_message=Colors.FAIL
                    )
            except ValueError:
                UserInterface.display_message(
                    header="Error",
                    message="Entrada inválida. Por favor, ingresa un número entero.",
                    color_message=Colors.FAIL
                )

class FileManager:

    @staticmethod
    def save_to_file(codes: list, filename: str) -> None:
        try:
            with open(filename, 'a', encoding='utf-8') as file:
                for code in codes:
                    file.write(code + "\n")
            UserInterface.display_message(
                header="Éxito",
                message=f"Códigos guardados exitosamente en {filename}",
                color_message=Colors.OKGREEN
            )
        except Exception as e:
            UserInterface.display_message(
                header="Error",
                message=f"Error al guardar los códigos: {e}",
                color_message=Colors.FAIL
            )

class CodeGeneratorApp:

    @staticmethod
    def main() -> None:
        """Método principal para ejecutar la aplicación."""
        UserInterface.print_line(char='=', length=60, color=Colors.HEADER)
        UserInterface.slow_print(f"{Colors.OKCYAN}{Colors.BOLD}    Bienvenido a BBVA México - Generador de Códigos de Retiro{Colors.RESET}", delay=0.03)
        UserInterface.print_line(char='=', length=60, color=Colors.HEADER)
        UserInterface.loading_animation("  Cargando sistema", duration=5)
        print("\n")

        filename = UserInterface.get_valid_filename()
        num_codes = UserInterface.get_valid_number(f"{Colors.OKCYAN}Introduce la cantidad de códigos a generar: {Colors.RESET}")

        UserInterface.display_message(
            header="Generación de Códigos",
            message="Generando códigos, por favor espere...",
            color_header=Colors.BOLD_YELLOW
        )

        codes = []
        for i in range(num_codes):
            code = BBVACodeGenerator.generate_code()
            verification = CodeGenerator.generate_verification_code()
            amount = CodeGenerator.generate_amount()

            # Crear una entrada de código decorada
            code_entry = (
                f"Banco: BBVA México\n"
                f"Código de Retiro: {code}\n"
                f"Código de Verificación: {verification}\n"
                f"Monto disponible: ${amount} MXN"
            )
            codes.append(code_entry)

            # Imprimir código decorado
            UserInterface.display_message(
                header=f"Código {i + 1}",
                message=code_entry,
                color_message=Colors.OKGREEN
            )

        FileManager.save_to_file(codes, filename)

        UserInterface.display_message(
            header="Proceso Completo",
            message="Todos los códigos se generaron y guardaron correctamente.",
            color_header=Colors.BOLD_GREEN
        )

if __name__ == "__main__":
    CodeGeneratorApp.main()
