![Project Banner](assets/atm-banner.png)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Python Version](https://img.shields.io/badge/python-3.10-blue)
![License](https://img.shields.io/badge/license-MIT-green)

# ATM Simulator in Python (CLI + GUI)

## Description

This project is a modular ATM simulator implemented in Python. It showcases a clean separation between domain logic (accounts, cards) and a Tkinter-based graphical interface that simulates an ATM workflow. The GUI provides Spanish-language screens and an on‑screen numeric keypad for PIN and amount entry. Security UX includes a three-attempt PIN limit before session lockout.

## Architectural Highlights

- Modular, decoupled design: domain logic lives in `accounts/` and `cards/`; the GUI resides in `ui/`.
- Clear responsibilities by component:
  - `accounts/*`: Concrete account types (Checking, Savings, Credit).
  - `cards/*`: Card abstractions (Debit, Credit) linked to accounts.
  - `ui/app.py`: Tkinter GUI screens and navigation.
- Simple seeding via `AccountFactory` to provide demo accounts/cards for quick testing.

## Security & User Experience Features

- PIN attempt limit: authentication allows 3 attempts; after 3 failures, the session resets and returns to the welcome screen.
- Clear feedback on incorrect PIN and operation results (receipt view after actions).
- On‑screen numeric keypad for PIN and amount entry to mimic ATM experience.

## Technologies Used

- Python 3.10+
- Tkinter for GUI (ships with Python on most platforms)

## Project Structure

ATM/
├── accounts/
│ ├── checking_account.py
│ ├── savings_account.py
│ ├── credit_account.py
│ ├── account_manager.py
│ └── factory.py
├── cards/
│ ├── card.py
│ ├── debit_card.py
│ └── credit_card.py
├── ui/
│ └── app.py
└── README.md

- `ui/app.py`: GUI entry point and screens (Welcome, Card Insert, PIN, Menu, Amount, Receipt).
- `accounts/`: Account domain logic and factory for creating concrete accounts.
- `cards/`: Card abstractions linking to accounts.

## Installation

1. Clone this repository to your local machine.
2. Ensure you have Python 3.10 or newer installed (with Tkinter available).
3. No external dependencies are required for the GUI.

## Usage

Run the GUI from the project root:

```
python -m ui.app
```

Demo Cards (enter last 4 digits on the Card screen):

- `4444` → PIN `1234` → Checking `CHK-001` (Alice, 1000.00)
- `8888` → PIN `4321` → Savings `SAV-001` (Bob, 2500.00)
- `2222` → PIN `2468` → Credit `CRD-001` (Carlos, limit 1500, 20% APR)

Features available in the GUI:

- View balance, Deposit, Withdraw, Exit.
- 3-attempt PIN lockout with session reset.

## Contributing

Contributions, issues, and feature requests are welcome. Please use feature branches and open pull requests against `main`. Suggested follow-ups: transfers between accounts, improved styling/themes, and additional error handling.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

Created by superTay. Feel free to connect for collaboration or feedback!
