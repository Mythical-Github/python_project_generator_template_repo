import sys
from pathlib import Path

from default_project_name import cli_py
from default_project_name.cli import OPTIONS
from default_project_name import log_py as log
from default_project_name.log_colors import COLORS


if getattr(sys, 'frozen', False):
    script_dir = Path(sys.executable).parent
else:
    script_dir = Path(__file__).resolve().parent

def main():
    try:
        log.set_log_base_dir(script_dir)
        log.configure_logging(COLORS)
        cli_py.cli_logic(OPTIONS)
    except Exception as error_message:
        log.log_message(str(error_message))

if __name__ == "__main__":
    main()
