# Multiplication Table with NumPy

A Python program that generates a multiplication table from 1 to 10 using NumPy broadcasting.

## How It Works

The program:
1. Creates an array of numbers from 1 to 10
2. Uses NumPy broadcasting to multiply the array with its transpose
3. Creates a complete 10x10 multiplication table in one operation

## What is Broadcasting?

Broadcasting allows NumPy to perform operations on arrays of different shapes. Here, `x[:, None]` creates a column vector and `x` is a row vector, so multiplying them together creates the entire multiplication table.

## Requirements
```
numpy>=1.15.0
```
