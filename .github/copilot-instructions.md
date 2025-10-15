# Copilot Instructions

## Project Overview

This project is an ATM simulator that demonstrates the use of SOLID principles and design patterns, specifically the Factory pattern for creating different types of bank accounts and cards.

## Architecture

The application is divided into two main components: `accounts` and `cards`. Both components follow a similar structure, using a factory to create instances of different types.

- **`accounts/`**: This directory contains all the logic related to bank accounts.
- **`cards/`**: This directory contains the logic for different types of cards (e.g., Debit, Credit).

The project uses a Factory design pattern to decouple the client code from the concrete implementations of accounts and cards. This makes it easy to add new types of accounts or cards without modifying the client code.

### Accounts

- **`accounts/account_manager.py`**: Defines the `AccountManager` abstract base class, which serves as an interface for all account types. All new account types should inherit from this class and implement its abstract methods.
- **`accounts/factory.py`**: The `AccountFactory` is responsible for creating instances of different account types. To add a new account type, you need to update the `create_account` method in this factory.

### Cards

- **`cards/card.py`**: Defines the `Card` abstract base class, which serves as an interface for all card types.
- **`cards/factory.py`**: The `CardFactory` is responsible for creating instances of different card types.

## Development Workflow

### Adding a new Account Type

1.  Create a new file in the `accounts/` directory (e.g., `new_account_type.py`).
2.  Implement the new account class, inheriting from `AccountManager` and implementing all its abstract methods.
3.  Update the `AccountFactory` in `accounts/factory.py` to include the new account type.

### Adding a new Card Type

1.  Create a new file in the `cards/` directory (e.g., `new_card_type.py`).
2.  Implement the new card class, inheriting from `Card` and implementing all its abstract methods.
3.  Update the `CardFactory` in `cards/factory.py` to include the new card type.

## Conventions

- Use abstract base classes (`ABC`) to define interfaces for components.
- Use factories to create instances of objects.
- Follow SOLID principles in your code.
