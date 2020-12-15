import os
import subprocess

from solutions.python.common.files import PYTHON_SOLUTIONS_DIRECTORY

if __name__ == '__main__':
    for day_module in sorted([f[:-3] for f in os.listdir(PYTHON_SOLUTIONS_DIRECTORY)
                              if f.startswith('day_') and f.endswith('.py')]):
        day_number: int = int(day_module[-2:])
        print(f"\n******* Day {day_number} *******\n")
        subprocess.run(['python3', '-m', f'solutions.python.{day_module}'])
