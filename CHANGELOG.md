# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased] - 1.1.0-SNAPSHOT

### Added

- Comprehensive unit test suite with `test_main.py`
- Test coverage for all main functions (ring_laptop, wait_for_keypress, get_interval, main)
- Testing dependencies: pytest, pytest-cov, pytest-mock
- `requirements.txt` for production dependencies
- `requirements-dev.txt` for development dependencies
- Testing section in README.md
- Version number in main.py (`__version__`)
- `--version` and `-v` command-line flags to display version

### Changed

- Refactored overall code

## [1.0.0] - 2024-07-12

### Added

- Command-line argument support for interval sleep time
- Comprehensive README with usage examples and build instructions
- Keybinding table documentation
- Requirements section in README

### Changed

- Replaced module-level mutable globals with local variables and return values
- Fixed race condition in keyboard listener using `threading.Event` objects
- Replaced `os.system` with `subprocess.run` for safer subprocess execution
- Replaced `time.sleep` with `threading.Event().wait` for better threading
- Improved error handling for `EOFError` in input handling
- Sound thread now properly joined to prevent overlapping audio

### Fixed

- Thread synchronization issues between listener and main threads
- Clean exit on `KeyboardInterrupt` (Ctrl+C) with proper exception handling
- Prevented sound overlap when user advances quickly through intervals

## [0.1.0] - 2024-07-12

### Added

- Initial release
- Basic timer functionality with configurable intervals
- Sound notification using macOS `afplay`
- Keyboard controls (Space to continue, Esc to exit)
- Interactive prompt for setting time intervals
