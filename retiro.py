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
    BOLD_RED = "\033[1;31m"

class CodeGenerator(ABC):

    @abstractmethod
    def generate_code(self) -> str:
        pass

    @staticmethod
    def generate_verification_code() -> str:
        return ''.join(random.choices('0123456789', k=4))

    @staticmethod
    def generate_amount() -> int:
        return random.randint(100, 10000)

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
        for _ in range(int(duration * 2)):
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

    def show_reflection_message() -> None:
        UserInterface.print_line(char='=', length=60, color=Colors.BOLD_RED)
        UserInterface.slow_print(f"{Colors.BOLD_RED}{Colors.BOLD}😔 A veces, las cosas no salen como esperamos... ¿Verdad? 😔{Colors.RESET}", delay=0.08)
        UserInterface.print_line(char='=', length=60, color=Colors.BOLD_RED)
        time.sleep(1)
        UserInterface.slow_print(f"{Colors.BOLD_YELLOW}🌧️ Has recorrido este camino con la esperanza de encontrar una solución fácil, un atajo. Todos hemos pasado por ese deseo de que, de alguna manera, las cosas cambien de la noche a la mañana. 🌧️{Colors.RESET}", delay=0.07)
        time.sleep(1)
        UserInterface.slow_print(f"{Colors.BOLD_YELLOW}💔 Pero la vida no funciona así. A veces buscamos respuestas en los lugares equivocados, esperando que la suerte o algún truco nos salve. 💔{Colors.RESET}", delay=0.07)
        time.sleep(1)
        UserInterface.slow_print(f"{Colors.BOLD_YELLOW}💭 Y no es tu culpa por pensar que esta podría haber sido la solución... a veces la desesperación nos hace seguir caminos que, en el fondo, sabemos que no llevan a ningún lugar. 💭{Colors.RESET}", delay=0.08)
        time.sleep(1)
        UserInterface.slow_print(f"{Colors.BOLD_YELLOW}⚠️ Pero esta no es una estafa, ni una burla. Es solo una lección, una que duele pero que en el futuro te hará más fuerte. ⚠️{Colors.RESET}", delay=0.07)
        time.sleep(1)
        UserInterface.slow_print(f"{Colors.BOLD_YELLOW}💡 Hoy no has perdido dinero, sino una oportunidad de abrir los ojos. Este momento, aunque difícil, es un recordatorio de que las cosas valiosas no se consiguen sin esfuerzo. 💡{Colors.RESET}", delay=0.08)
        time.sleep(1)
        UserInterface.slow_print(f"{Colors.BOLD_YELLOW}🌱 El verdadero cambio no viene de lo fácil o rápido. Viene de las veces que te caes y te vuelves a levantar. 🌱{Colors.RESET}", delay=0.07)
        time.sleep(1)
        UserInterface.slow_print(f"{Colors.BOLD_YELLOW}😔 Es normal sentirse derrotado a veces... Pero cada derrota es solo una parte del camino hacia algo más grande. 😔{Colors.RESET}", delay=0.07)
        time.sleep(1)
        UserInterface.slow_print(f"{Colors.BOLD_YELLOW}💪 Hoy tal vez no lograste lo que querías, pero mañana, con esfuerzo y dedicación, lograrás mucho más de lo que jamás imaginaste. 💪{Colors.RESET}", delay=0.07)
        time.sleep(1)
        UserInterface.print_line(char='-', length=60, color=Colors.BOLD_CYAN)
        UserInterface.slow_print(f"{Colors.BOLD_GREEN}✨ Este no es el final, es solo el principio de un nuevo camino. Un camino que, aunque más difícil, te llevará a verdaderos logros. ✨{Colors.RESET}", delay=0.07)
        UserInterface.slow_print(f"{Colors.BOLD_GREEN}🌟 Sigue adelante, levántate y construye algo real, algo tuyo. 🌟{Colors.RESET}", delay=0.07)
        UserInterface.print_line(char='-', length=60, color=Colors.BOLD_CYAN)

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
            # Simulación de autenticación
            if CodeGeneratorApp.simulate_processing("Autenticación", time_seconds=2, success_chance=0.8):
                # Simulación de validación de monto
                if CodeGeneratorApp.simulate_processing("Validación de monto", time_seconds=1, success_chance=0.9):
                    # Simulación de generación de código de seguridad
                    if CodeGeneratorApp.simulate_processing("Generación de código de seguridad", time_seconds=1, success_chance=1.0):
                        code = BBVACodeGenerator.generate_code()
                        codes.append(code)
                        UserInterface.slow_print(f"{Colors.OKGREEN}Código {i+1}: {code}{Colors.RESET}")
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
            header="Proceso FALLIDO",
            message="Todos los códigos no se generaron correctamente :(",
            color_header=Colors.BOLD_GREEN
        )

        CodeGeneratorApp.show_reflection_message()

# Ejecutar la aplicación
if __name__ == "__main__":
    CodeGeneratorApp.main()
