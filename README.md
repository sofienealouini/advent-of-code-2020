# Advent Of Code 2020
[![Python 3.9.1](https://img.shields.io/badge/Python-3.9.1-3572a5.svg)](https://www.python.org/downloads/release/python-391/)
[![Julia 1.5.3](https://img.shields.io/badge/Julia-1.5.3-a270ba.svg)](https://julialang.org/downloads/)

## Getting started

To run the Julia solution for a specific day :
```
julia solutions/julia/day_15.jl
```

To run the Python solution for a specific day :
```
python3 -m solutions.python.day_15
```

To run the Python solutions for all days :
```
python3 -m solutions.python.all_days
```



## Learnings

### Julia

- Any function `f` can be used in a vectorized way on a collection with `f.`
- Functions can be composed using `∘` : `g ∘ f = x -> g(f(x))`
- Composite types can be defined using `struct`:
```
struct Rule
    password::String
    control_letter::Char
    low_position::Int
    high_position::Int
end
```
- Variables of this type can be created as follows: `Rule("vptrwwwnwwn", ':', 8, 10)`

### Python
- `value = dict.get(key, f())`: `f()` is evaluated by default before the lookup in `dict`. 
  - For a lazy evaluation, use: `value = dict[key] if key in dict else f()`.
  
- Product of a list of numbers : `math.prod`
- Greatest common divisor : `math.gcd`, Least common multiple : `math.lcm`

- `for key in dict` is more efficient than `for key in dict.keys()`
