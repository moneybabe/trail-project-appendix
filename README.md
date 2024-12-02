# trail-project-appendix

Random Turn Games: Numerical Verification of \(\min_{1 \leq i \leq N} \mathcal{M}^\downarrow_{5,4}(t_{i-1}, t_i)\)

This repository contains the code and resources used for the numerical verification of the lower bound of \(\min_{1 \leq i \leq N} \mathcal{M}^\downarrow_{5,4}(t_{i-1}, t_i)\) in the context of random turn games, as discussed in our paper.

Table of Contents
	- [Introduction](#introduction)
	- [Repository Structure](#repository-structure)
	- [Getting Started](#getting-started)
	- [Prerequisites](#prerequisites)
	- [Installation](#installation)
		- [Coq Installation](#coq-installation)
		- [Python Installation](#python-installation)
	- [Coq Implementation](#coq-implementation)
		- [Description](#description)
		- [Setup and Usage](#setup-and-usage)
	- [Python Implementations](#python-implementations)
		- [Common Setup](#common-setup)
		- [Implementation 1: Interval Arithmetic with mpmath](#implementation-1-interval-arithmetic-with-mpmath)
			- [Description](#description-1)
			- [Usage](#usage)
		- [Implementation 2: Custom Rounding](#implementation-2-custom-rounding)
			- [Description](#description-2)
			- [Usage](#usage-1)
	- [Results](#results)
	- [Contributing](#contributing)
	- [License](#license)

# Introduction

In our study of random turn games, we aim to establish a rigorous lower bound for the value of \(\min_{1 \leq i \leq N} \mathcal{M}^\downarrow_{5,4}(t_{i-1}, t_i)\). Due to the computational complexity and the need for rigorous error control, we provide both a formal verification using Coq and two numerical implementations in Python.

This repository allows readers and researchers to reproduce our results and verify the computations independently.

# Repository Structure

	•	coq/: Contains the Coq scripts for formal verification.
	•	python/: Contains two subfolders:
		•	interval_arithmetic/: Python implementation using the mpmath library for interval arithmetic.
		•	custom_rounding/: Python implementation with custom floating-point rounding strategies.
	•	README.md: This file.
	•	LICENSE: License information for the repository.

# Getting Started

# Prerequisites

To run the code in this repository, you need the following software installed:

	•	For Coq:
		•	Coq Proof Assistant (version 8.13 or later recommended)
	•	For Python implementations:
		•	Python 3.7 or later
		•	Required Python packages:
			•	mpmath (for interval arithmetic implementation)
			•	numpy

# Installation

## Coq Installation

	•	Windows and macOS: Download installers from the Coq official website.
	•	Linux: Install via your package manager or use opam.

## Python Installation

	•	Install Python from the official website or via a package manager.
	•	Install required packages using pip:

```
pip install mpmath numpy
```



Coq Implementation

Description

The Coq implementation provides a formal verification of the lower bound for \(\mathcal{M}^\downarrow_{5,4}(t_{i-1}, t_i)\) for a specific interval \([t_{i-1}, t_i]\). Due to computational limitations, verifying all intervals is impractical in Coq. However, the scripts allow for rigorous verification on selected intervals.

Setup and Usage

	1.	Navigate to the Coq Folder:

cd coq


	2.	Open the Coq File:
Open the verification.v file using your preferred Coq IDE (CoqIDE, Proof General, or VSCode with Coq extension).
	3.	Compile and Step Through the Proof:
	•	Load the file in the IDE.
	•	Step through the proof to see the verification of the lower bound on the specified interval.
	•	You can modify the interval endpoints in the script to verify other intervals.
	4.	Understanding the Script:
	•	The script defines the function \(\mathcal{M}^\downarrow_{5,4}(a, b)\) and computes the lower bound.
	•	It uses Coq’s real number definitions and tactics for rigorous proof development.

Python Implementations

Common Setup

	1.	Navigate to the Python Folder:

cd python


	2.	Install Dependencies (if not already installed):

pip install -r requirements.txt

The requirements.txt file should contain:

mpmath
numpy



Implementation 1: Interval Arithmetic with mpmath

Description

This implementation uses the mpmath library to perform interval arithmetic, providing rigorous bounds by accounting for all possible values within each interval, including floating-point errors.

Usage

	1.	Navigate to the Interval Arithmetic Folder:

cd interval_arithmetic


	2.	Run the Script:

python compute_lower_bound.py


	3.	Script Overview:

	•	The script compute_lower_bound.py performs the following steps:
	•	Divides the interval \([\tfrac{1}{3}, 3]\) into  subintervals.
	•	Computes \(\M_{5,4}(x)\) over each subinterval using interval arithmetic.
	•	Records the lower bound from each subinterval.
	•	Determines the minimum lower bound across all intervals.
	4.	Output:
	•	The script outputs the computed global lower bound, confirming that \(\M_{5,4}(x) \geq 0.9999030108006773\).
	5.	Adjusting Precision:
	•	You can adjust the decimal precision by modifying the mp.dps parameter at the beginning of the script.

from mpmath import mp
mp.dps = 30  # Set decimal places of precision


	6.	Understanding the Code:
	•	The function M54(x) computes \(\M_{5,4}(x)\) using mpmath functions.
	•	Interval arithmetic is achieved by creating intervals for x and performing computations with these intervals.

Implementation 2: Custom Rounding

Description

This implementation manually controls the floating-point rounding direction to ensure conservative estimates. By strategically rounding computations up or down, it accounts for floating-point errors and ensures the computed lower bound is rigorous.

Usage

	1.	Navigate to the Custom Rounding Folder:

cd custom_rounding


	2.	Run the Script:

python compute_lower_bound.py


	3.	Script Overview:
	•	The script compute_lower_bound.py performs the following steps:
	•	Divides the interval \([\tfrac{1}{3}, 3]\) into ￼ subintervals.
	•	For each subinterval:
	•	Computes \(\M_{5,4}(x)\) at the endpoints with controlled rounding.
	•	Determines the minimum value, ensuring it is a rigorous lower bound.
	•	Records the minimum lower bound across all intervals.
	4.	Output:
	•	The script outputs the computed global lower bound, confirming that \(\M_{5,4}(x) \geq 0.9999030108006773\).
	5.	Understanding the Code:
	•	The script uses the decimal module to control rounding direction.
	•	Functions are defined to perform arithmetic operations with specified rounding modes.
	•	The computations ensure that any rounding errors decrease the overall result, maintaining a valid lower bound.
	6.	Adjusting Precision:
	•	You can adjust the decimal precision by setting the prec parameter in the decimal context.

from decimal import localcontext, Decimal, ROUND_DOWN, ROUND_UP
localcontext().prec = 30  # Set decimal places of precision



Results

Both implementations confirm the rigorous lower bound:

\[
\M_{5,4}(x) \geq 0.9999030108006773 \quad \text{for all } x \in \left[\tfrac{1}{3}, 3\right].
\]

This result supports the proof of the lower bound for ￼ as detailed in our paper.

Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

License

This project is licensed under the MIT License - see the LICENSE file for details.

Note: This repository and the code within are provided for educational and research purposes. Ensure you have the appropriate software and understand the computations before running the scripts.