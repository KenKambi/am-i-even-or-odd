# Am I Even Or Odd 

[![PyPI version](https://img.shields.io/pypi/v/am-i-even-or-odd.svg)](https://pypi.org/project/am-i-even-or-odd/)
[![CI](https://github.com/KenKambi/am-i-even-or-odd/actions/workflows/ci.yml/badge.svg)](https://github.com/KenKambi/am-i-even-or-odd/actions/workflows/ci.yml)
[![Python versions](https://img.shields.io/pypi/pyversions/am-i-even-or-odd.svg)](https://pypi.org/project/am-i-even-or-odd/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/KenKambi/am-i-even-or-odd/blob/main/LICENSE)

A tiny Python package that answers one simple question:
is your number even, or odd tho?

Yes, `n % 2 == 0` does the same thing :)

## Installation

```bash
pip install am-i-even-or-odd
```

## Usage

```python
from am_i_even_or_odd import is_it_even_tho, is_it_odd_tho

print(is_it_even_tho(4))
print(is_it_odd_tho(5))
```

Output

```
True
True
```

### Error handling

Only `int` values are accepted. Anything else — floats, strings,
`None`, booleans — raises a `TypeError` with a message explaining
why, rather than silently returning a possibly-wrong answer:

```python
>>> is_it_even_tho(4.0)
TypeError: expected an int, got 'float' (4.0). Floats and other
numeric types aren't supported to avoid ambiguity around what
counts as 'even' or 'odd'.
```

## Development

```bash
git clone https://github.com/KenKambi/am-i-even-or-odd.git
cd am-i-even-or-odd
pip install -e ".[dev]"
pytest -v
```

Contributions and issues are welcome — see the
[issue tracker](https://github.com/KenKambi/am-i-even-or-odd/issues).

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## License

MIT — see [LICENSE](LICENSE).