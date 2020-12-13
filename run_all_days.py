import os
import subprocess

if __name__ == '__main__':
    for day_module in sorted([e for e in os.listdir(os.path.dirname(__file__))
                              if os.path.isdir(e) and e.startswith('day')]):
        print(f"\n**** Day {int(day_module[-2:])} ****\n")
        subprocess.run(['python3', '-m', f'{day_module}.solution'])
