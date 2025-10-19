# ATM Simulator (CLI + GUI)

## Overview
- Python ATM simulator with account and card abstractions.
- GUI built with Tkinter: Spanish screens and on‑screen numeric keypad.
- Supports: card insert, PIN auth (3 attempts), balance, deposit, withdrawal.

## Requirements
- Python 3.9+ with Tkinter available.
- No external dependencies.

## Run
- GUI: `python -m ui.app`
- CLI: Use your existing CLI entry points if applicable.

## Demo Data
- Cards (enter last 4 digits on Card screen):
  - `4444` → PIN `1234` → Checking `CHK-001` (Alice, 1000.00)
  - `8888` → PIN `4321` → Savings `SAV-001` (Bob, 2500.00)
  - `2222` → PIN `2468` → Credit `CRD-001` (Carlos, limit 1500, 20% APR)

## Features
- Welcome → Card insert → PIN keypad → Menu.
- Menu: View balance, Deposit, Withdraw, Exit.
- PIN lockout: 3 failed attempts lock session and return to Welcome.

## Project Structure
- `accounts/`: account implementations (checking, savings, credit)
- `cards/`: card types (debit, credit)
- `ui/app.py`: Tkinter GUI entrypoint

## Development
- Create a feature branch for changes.
- Run tests (if present), then open a PR to `main`.

## License
- Add your license info if applicable.

