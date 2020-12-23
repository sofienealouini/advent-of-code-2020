# Advent Of Code 2020
[![Python 3.9.1](https://img.shields.io/badge/Python-3.9.1-3572a5.svg)](https://www.python.org/downloads/release/python-391/)
[![Julia 1.5.3](https://img.shields.io/badge/Julia-1.5.3-a270ba.svg)](https://julialang.org/downloads/)

## Getting started

### Julia

- To run the Julia solution for a specific day :
```
julia solutions/julia/day_15.jl
```

- To run the Julia solutions for all days :
```
julia solutions/julia/all_days.jl
```

### Python

- To run the Python solution for a specific day :
```
python3 -m solutions.python.day_15
```

- To run the Python solutions for all days :
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
- Julia accepts a list of [symbols](https://github.com/JuliaLang/julia/blob/master/src/julia-parser.scm) that can be used to define infix operators. Based on their symbol, some user-defined operators (like `∨`) will automatically have the same precedence as `+`, and others (like `∧`) will automatically have the same precedence as `*`.

### Python
- `value = dict.get(key, f())`: `f()` is evaluated by default before the lookup in `dict`. 
  - For a lazy evaluation, use: `value = dict[key] if key in dict else f()`.
  
- Product of a list of numbers : `math.prod`
- Greatest common divisor : `math.gcd`, Least common multiple : `math.lcm`

- `for key in dict` is more efficient than `for key in dict.keys()`

- Calling `.extendleft()` on a `deque` extends the `deque` from right to left starting from index 0 :
```
>>> q = deque([3, 4, 5])
>>> q.extendleft([1, 2])
>>> q
deque([2, 1, 3, 4, 5])
```
