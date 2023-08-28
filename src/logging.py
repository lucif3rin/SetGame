from os import devnull

class Colors:
    """
    reset all colors with colors.reset; two
    sub classes fg for foreground
    and bg for background; use as colors.subclass.colorname.
    i.e. colors.fg.red or colors.bg.greenalso, the generic bold, disable,
    underline, reverse, strike through,
    and invisible work with the main class i.e. colors.bold
    """
    RESET = '\033[0m'
    BOLD = '\033[01m'
    DISABLE = '\033[02m'
    UNDERLINE = '\033[04m'
    REVERSE = '\033[07m'
    STRIKE_THROUGH = '\033[09m'
    INVISIBLE = '\033[08m'
    class Fg:
        BLACK = '\033[30m'
        RED = '\033[31m'
        GREEN = '\033[32m'
        ORANGE = '\033[33m'
        BLUE = '\033[34m'
        PURPLE = '\033[35m'
        CYAN = '\033[36m'
        LIGHT_GREY = '\033[37m'
        DARK_GREY = '\033[90m'
        LIGHT_RED = '\033[91m'
        LIGHT_GREEN = '\033[92m'
        YELLOW = '\033[93m'
        LIGHT_BLUE = '\033[94m'
        PINK = '\033[95m'
        LIGHT_CYAN = '\033[96m'
    
    class Bg:
        BLACK = '\033[40m'
        RED = '\033[41m'
        GREEN = '\034[42m'
        ORANGE = '\033[43m'
        BLUE = '\033[44m'
        PURPLE = '\033[45m'
        CYAN = '\033[46m'
        LIGHT_GREY = '\033[47m'

class Log:
    def __init__(self, log_path: str, output_to_console: bool):
        """
        Creates a new log file or writes to an existing one.
        Selects whether or not to print to the console.
        :param log_path: Path of the log file.
        :param output_to_console: Whether or not to output to console.
        """
        try:
            self.log_file = open(log_path, "+a")
            self.output_to_console = output_to_console
            self.write_event(f"Successfuly opened log, print to console: {output_to_console}")
        except FileNotFoundError:
            print(f"{Colors.Bg.RED}FATAL: Could not open log file, discarding logs and writing to console instead.{Colors.RESET}")
            continue_operation = input(f"{Colors.Fg.ORANGE}Please enter \"confirm\" to continue, else the program will stop running.{Colors.RESET}\n")
            if continue_operation.lower() != "confirm":
                exit(-1)
            self.log_file = open(devnull, "+a")
            self.output_to_console = True
            self.write_warning("Continuing operation, logs discarded.")
                

    def write_to_log(self, msg: str):
        """
        Receives a message to write to the log, checks whether to print or not, and logs the message.
        :param msg: The message to write to the log.
        :return:    True if successful, false otherwise.
        """
        log_msg = msg + Colors.RESET
        if self.output_to_console:
            print(log_msg)
        self.log_file.write(log_msg)

    def write_event(self, msg: str):
        """
        Writes an event with color formating.
        """
        event_msg = f"{Colors.Bg.GREEN}EVENT:{Colors.RESET} {Colors.Fg.GREEN}{msg}"
        self.write_to_log(event_msg)

    def write_warning(self, msg: str):
        """
        Writes a warning with color formatting
        """
        warning_msg = f"{Colors.Bg.ORANGE}WARNING: {Colors.RESET} {Colors.Fg.ORANGE}{msg}"
        self.write_to_log(warning_msg)
    
    def write_error(self, msg: str):
        """
        Writes an error with formatting
        """
        error_msg = f"{Colors.Bg.RED}ERROR:{Colors.RESET} {Colors.Fg.RED}{msg}"
        self.write_to_log(error_msg)

    def write_fatal(self, msg):
        """
        Writes a fatal error with formatting
        """
        fatal_msg = f"{Colors.Bg.RED}FATAL:{msg}"
        self.write_to_log(fatal_msg)
