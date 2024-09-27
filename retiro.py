import time
import random
from abc import ABC, abstractmethod

class Colors:
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
        return random.randint(10, 300)

class BBVACodeGenerator(CodeGenerator):

    @staticmethod
    def generate_code() -> str:
        return '1' + ''.join(random.choices('0123456789', k=11))

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
    def loading_animation(text: str, duration: float = 1.0) -> None:
        print(f"{text} ", end="", flush=True)
        for _ in range(int(duration * 2)):  # Ajustamos el tiempo para que sea más rápido
            for symbol in "|/-\\":
                print(f"\033[94m{symbol}\033[0m", end="\r", flush=True)
                time.sleep(0.25)

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
    def simulate_processing(stage: str, time_seconds: float, success_chance: float = 1.0) -> bool:
        UserInterface.loading_animation(f"{stage} en progreso", duration=time_seconds)
        success = random.random() < success_chance
        if success:
            print(f"\n{Colors.OKGREEN}✔ {stage} completado.{Colors.RESET}\n")
        else:
            print(f"\n{Colors.FAIL}✘ {stage} fallido. Intentando de nuevo...{Colors.RESET}\n")
        return success

    @staticmethod
    def main() -> None:
        UserInterface.print_line(char='=', length=60, color=Colors.HEADER)
        UserInterface.slow_print(f"{Colors.OKCYAN}{Colors.BOLD}    Bienvenido a BBVA México - Generador de Códigos de Retiro{Colors.RESET}", delay=0.03)
        UserInterface.print_line(char='=', length=60, color=Colors.HEADER)
        UserInterface.loading_animation("  Cargando sistema", duration=2)
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
            # Simular varias etapas del proceso en 30 segundos total
            if CodeGeneratorApp.simulate_processing(" Verificación de autenticidad", time_seconds=3.5, success_chance=0.98):
                if CodeGeneratorApp.simulate_processing(" Validación del monto", time_seconds=3.5, success_chance=0.95):
                    if CodeGeneratorApp.simulate_processing(" Generación del código de seguridad", time_seconds=3.5, success_chance=0.99):
                        # Generar código si todas las etapas son exitosas
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
                    else:
                        UserInterface.display_message(
                            header="Error",
                            message="No se pudo generar el código de seguridad. Reintentando...",
                            color_message=Colors.FAIL
                        )
                else:
                    UserInterface.display_message(
                        header="Error",
                        message="Validación de monto fallida. Reintentando...",
                        color_message=Colors.FAIL
                    )
            else:
                UserInterface.display_message(
                    header="Error",
                    message="Autenticación fallida. Reintentando...",
                    color_message=Colors.FAIL
                )

        FileManager.save_to_file(codes, filename)

        UserInterface.display_message(
            header="Proceso Completo",
            message="Todos los códigos se generaron y guardaron correctamente.",
            color_header=Colors.BOLD_GREEN
        )

if __name__ == "__main__":
    CodeGeneratorApp.main()
