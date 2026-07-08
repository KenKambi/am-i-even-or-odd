# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [0.2.0] - 2026-07-08

### Added
- Input validation: `is_it_even_tho` and `is_it_odd_tho` now raise a
  `TypeError` with a clear message for non-`int` input (floats,
  strings, `None`, `bool`, etc.) instead of silently returning a
  possibly-misleading result.
- Type hints and docstrings on the public functions.
- `py.typed` marker so type checkers (mypy, pyright) recognize this
  package as typed.
- Tests covering zero, negative numbers, and invalid input.
- CI workflow running the test suite on Python 3.8–3.12.
- Automated PyPI publish workflow triggered on GitHub Release.

### Changed
- **Potentially breaking:** previously, non-int numeric input (e.g.
  `4.0`) was silently accepted via Python's `%` operator. It's now
  rejected with a `TypeError`. If you were relying on float input,
  pin to `<0.2.0` or cast to `int` before calling.

## [0.1.0] - Initial release

### Added
- `is_it_even_tho(number)` and `is_it_odd_tho(number)`.
- MIT license, README, and PyPI packaging metadata.
