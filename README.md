Hikmal Maulana Ramadhan
Mathematics Study Program, Faculty of Mathematics and Natural Sciences
University of Mataram

# GRS Code over Number Fields

This repository contains a Python implementation of **Generalized Reed–Solomon (GRS) codes over number fields** using algebraic number theory and Galois theory.

## Features
- Compute permutation order and select primes with specific congruence conditions.  
- Construct subgroup \(H \subseteq (\mathbb{Z}/p\mathbb{Z})^*\).  
- Generate minimal polynomial of \(\alpha = \sum_{h \in H} \zeta_p^h\).  
- Calculate polynomial discriminant and roots (exact & approximate).  
- Build evaluation vectors, Cauchy vectors, and construct the GRS generator matrix \((I_k | B)\).  

## Requirements
- Python 3.9+  
- [SymPy](https://www.sympy.org/en/index.html)  

Install SymPy with:
```bash
pip install sympy
