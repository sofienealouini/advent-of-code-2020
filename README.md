# Advent Of Code 2020
[![Python 3.9.1](https://img.shields.io/badge/Python-3.9.1-3572a5.svg)](https://www.python.org/downloads/release/python-391/)
[![Julia 1.5.3](https://img.shields.io/badge/Julia-1.5.3-a270ba.svg)](https://julialang.org/downloads/)

### Learnings

- `value = dict.get(key, f())`: `f()` is evaluated by default before the lookup in `dict`. 
  - For a lazy evaluation, use: `value = dict[key] if key in dict else f()`.
  
- Product of a list of numbers : `math.prod`
- Greatest common divisor : `math.gcd`, Least common multiple : `math.lcm`

- `for key in dict` is more efficient than `for key in dict.keys()`
