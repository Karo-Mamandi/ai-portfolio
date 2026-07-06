# Fibonacci Series Generator

A Python program that generates the Fibonacci sequence using NumPy arrays.

## Features

- Generates the first 10 numbers in the Fibonacci sequence
- Uses NumPy arrays for efficient storage
- Demonstrates iterative algorithm implementation

## How It Works

The program:
1. Creates a NumPy array of size 10 (all zeros)
2. Sets the first two values to 1 (starting point)
3. Calculates each subsequent number as the sum of the two previous numbers
4. Displays the complete Fibonacci sequence

## Fibonacci Sequence Explained

#### The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones:
* 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...


**Formula:** `F(n) = F(n-1) + F(n-2)` where `F(0) = 0` and `F(1) = 1`

## Requirement
```
numpy>=1.15.0
```
