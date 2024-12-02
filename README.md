# Trail of Lost Pennies: Numerical Verification of $\min_{1 \leq i \leq N} \mathcal{M}^\downarrow_{5,4}(t_{i-1}, t_i)$

This repository contains the code and resources used for the numerical verification of the lower bound of $\min_{1 \leq i \leq N} \mathcal{M}^\downarrow_{5,4}(t_{i-1}, t_i)$ in the Trail of Lost Pennies, as discussed in our paper.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
## Table of Contents

- [Introduction](#introduction)
- [Repository Structure](#repository-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Coq Installation](#coq-installation)
  - [Python Installation](#python-installation)
- [Coq Implementation](#coq-implementation)
  - [Setup and Usage](#setup-and-usage)
- [Python Implementations](#python-implementations)
  - [Implementation 1: Interval Arithmetic with mpmath](#implementation-1-interval-arithmetic-with-mpmath)
    - [Setup and Usage](#setup-and-usage-1)
  - [Implementation 2: Custom Rounding](#implementation-2-custom-rounding)
    - [Setup and Usage](#setup-and-usage-2)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Introduction

In our study of random turn games, we aim to establish a rigorous lower bound for the value of $\min_{1 \leq i \leq N} \mathcal{M}^\downarrow_{5,4}(t_{i-1}, t_i)$. Due to the computational complexity and the need for rigorous error control, we provide both a formal verification using Coq and two numerical implementations in Python.

This repository allows readers and researchers to reproduce our results and verify the computations independently.

## Repository Structure

- coq: Contains the Coq scripts for formal verification.
- python: Contains two subfolders:
  - interval_arithmetic: Python implementation using the mpmath library for interval arithmetic.
  - custom_rounding: Python implementation with custom floating-point rounding strategies.
  - requirements.txt: Required Python packages for the implementations.
- README.md: This file.
- LICENSE: License information for the repository.

## Prerequisites

To run the code in this repository, you need the following software installed:

- For Coq:
  - Coq Proof Assistant (version 8.18 or later recommended)
- For Python implementations:
  - Python 3.9 or later

## Installation

### Coq Installation

- Windows and macOS: Download installers from the [Coq official website](https://coq.inria.fr/download).
- Linux: Install via your package manager or use opam.

### Python Installation

- Install Python from the official website or via a package manager.
- Install required packages using pip:

```bash
pip install -r python/requirements.txt
```

## Coq Implementation

The Coq implementation provides a formal verification of the lower bound for $\mathcal{M}^\downarrow_{5,4}(t_{i-1}, t_i)$ for a specific interval $[t_{i-1}, t_i]$. Due to computational limitations, verifying all intervals is impractical in Coq. However, the scripts allow for rigorous verification on selected intervals.

### Setup and Usage

1. Navigate to the Coq Folder:

```bash
cd coq
```

2. Open the Coq File:

Open the Main.v file using your preferred Coq IDE (CoqIDE, Proof General, or VSCode with Coq extension).

3. Compile and Step Through the Proof:

- Load the file in the IDE.
- Step through the proof to see the verification of the lower bound on the specified interval.
- You can modify the interval endpoints in the script to verify other intervals.

4. Understanding the Script:

- The script defines the function $\mathcal{M}^\downarrow_{5,4}(a, b)$ and computes the lower bound.
- It uses Coq's real number definitions and interval arithmetic tactic for rigorous proof development.

## Python Implementations

### Implementation 1: Interval Arithmetic with mpmath

This implementation uses the `mpmath` library to perform interval arithmetic, providing rigorous bounds by accounting for all possible values within each interval, including floating-point errors.

#### Setup and Usage

1. Navigate to the Interval Arithmetic Folder:

```bash
cd python/interval_arithmetic
```

2. Run the Script:

```bash
python main.py
```

3. Script Overview:

- The script compute_lower_bound.py performs the following steps:
  - Divides the interval $[\tfrac{1}{3}, 3]$ into subintervals.
  - Computes $\mathcal{M}^\downarrow_{5,4}(a, b)$ over each subinterval using interval arithmetic.
  - Records the lower bound from each subinterval.
  - Determines the minimum lower bound across all intervals.

4. Output:

- The script outputs the computed global lower bound, confirming that $\min_{1 \leq i \leq N} \mathcal{M}^\downarrow_{5,4}(t_{i-1}, t_i) \geq 0.9999030108006773$.
- The script also saves a `results.csv` file with the computed lower bounds for each subinterval.

5. Understanding the Code:

- The function `M54_down` computes $\mathcal{M}^\downarrow_{5,4}(a, b)$ using mpmath functions.
- Interval arithmetic is achieved by creating intervals for each real number and performing computations with these intervals.

### Implementation 2: Custom Rounding

This implementation manually controls the floating-point rounding direction to ensure conservative estimates. By strategically rounding computations up or down, it accounts for floating-point errors and ensures the computed lower bound is rigorous.

#### Setup and Usage

1. Navigate to the Custom Rounding Folder:

```bash
cd python/custom_rounding
```

2. Run the Script:

```bash
python main.py
```

3. Script Overview:

- The script compute_lower_bound.py performs the following steps:
  - Divides the interval $[\tfrac{1}{3}, 3]$ into subintervals.
  - For each subinterval:
    - Computes $\mathcal{M}^\downarrow_{5,4}(t_{i-1}, t_i)$ at the endpoints with controlled rounding.
  - Determines the minimum value, ensuring it is a rigorous lower bound.
    - Records the minimum lower bound across all intervals.

4. Output:

- The script outputs the computed global lower bound, confirming that $\min_{1 \leq i \leq N} \mathcal{M}^\downarrow_{5,4}(t_{i-1}, t_i) \geq 0.9999030108006773$.

## Results

Both implementations confirm the rigorous lower bound:

$$
	\min_{1 \leq i \leq N} \mathcal{M}^\downarrow_{5,4}(t_{i-1}, t_i) \geq 0.9999030108006773.
$$

This result supports the proof of the lower bound for $\inf\{\mathcal{M}^\downarrow_{5,4}(x): x\in[\tfrac{1}{3}, 3]\}$ as detailed in our paper.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request. Please also feel free to contact the authors for any questions or collaborations through the emails provided in the paper.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

Note: This repository and the code within are provided for educational and research purposes. Ensure you have the appropriate software and understand the computations before running the scripts.
