# Advent Of Code 2020
[![Python 3.9.1](https://img.shields.io/badge/python-3.9.1-blue.svg)](https://www.python.org/downloads/release/python-391/)

### Learnings

- `value = dict.get(key, f())`: `f()` is evaluated by default before the lookup in `dict`. 
  - For a lazy evaluation, use: `value = dict[key] if key in dict else f()`.
  
- Product of a list of numbers : `math.prod`
- Greatest common divisor : `math.gcd`, Least common multiple : `math.lcm`
