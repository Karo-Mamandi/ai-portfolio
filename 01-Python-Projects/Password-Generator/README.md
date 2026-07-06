# Secure Password Generator

A powerful, cryptographically secure password generator with customizable options and entropy strength estimation.

## Description

This password generator creates strong, secure passwords using Python's `secrets` module, which provides cryptographically secure random numbers. Unlike regular random generators, this is suitable for production applications, user accounts, and security-sensitive contexts.

## Features

- **Cryptographically Secure** - Uses `secrets` module for unpredictable passwords
- **Customizable Character Sets** - Choose from lowercase, uppercase, digits, and special characters
- **Guaranteed Character Types** - Ensures at least one character from each selected category
- **Password Shuffling** - Prevents predictable patterns in output
- **Entropy Estimation** - Displays password strength in bits
- **Command-line Interface** - Simple and easy to use

## Requirements

- Python 3.6+ (for `secrets` module)
- No external dependencies
