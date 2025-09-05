# Nama : Hikmal Maulana Ramadhan
# NIM  : G1D021024

from math import lcm, gcd, sqrt as math_sqrt
from sympy import exp, I, pi, minimal_polynomial, simplify, symbols, solve, QQ, Poly, discriminant, N

x = symbols("x")

#------------------------------------------------------------------------------------------------------------

def cek_prima(num):
    if num < 2:
        return False
    for i in range(2, int(math_sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True

def input_sigma():
    sigma = []
    num_cycles = int(input("Masukkan jumlah siklus = "))
    for i in range(num_cycles):
        cycle = input(f"Masukkan elemen ke-{i + 1} (pisah dengan koma) = ")
        cycle_elements = list(map(int, cycle.split(',')))
        sigma.append(cycle_elements)
    return sigma

def order_permutasi(cycles):
    panjang = [len(cycle) for cycle in cycles]
    return lcm(*panjang)
c 
def grup_perkalian(p):
    return [i for i in range(1, p) if gcd(i, p) == 1]

def subgrup_H(p, order):
    subgrup_order = (p - 1) // order
    elements = grup_perkalian(p)
    H = [x for x in elements if pow(x, subgrup_order, p) == 1]
    return H, subgrup_order

def Mpoly(p, H, x):
    zeta = exp(2 * pi * I / p)
    alpha = sum(zeta**i for i in H)
    alpha = simplify(alpha)
    return minimal_polynomial(alpha, x)

def diskriminan_polynomial(poly_expr, var):
    poly = Poly(poly_expr, var)
    D = discriminant(poly)
    print(f"\nDiskriminan = {D}")
    return D

def konstruksi_kode_grs(roots, k):
    n = len(roots)
    alpha_bar = [simplify(r) for r in roots]
    b = [1] * n

    print("\nAkar-akarnya (eksak dan aproksimasi):")
    for i, r in enumerate(roots, 1):
        print(f"r_{i} = {simplify(r)}  ≈  {N(r, 8)}")

    print("\nVektor evaluasi ᾱ = (r₁, r₂, ..., rₙ):")
    print(alpha_bar)
    print("\nVektor bobot b =", b)

    # Hitung vektor Cauchy c
    c = []
    for i in range(n):
        prod = 1
        if i < k:
            for j in range(k):
                if j != i:
                    prod *= (roots[i] - roots[j])
        else:
            for j in range(k):
                prod *= (roots[i] - roots[j])
        c_val = simplify(b[i] * prod)
        c.append(c_val)

    print("\nVektor Cauchy c (eksak):")
    print(c)

    print("\nVektor c dalam bentuk desimal:")
    for i, val in enumerate(c, 1):
        print(f"c{i} ≈ {N(val, 8)}")

    # Matriks B(a, c)
    print("\nMatriks Cauchy B(a, c):")
    B = []
    for i in range(k):
        row = []
        for j in range(n - k):
            denom = c[i] * (roots[j + k] - roots[i])
            Bij = simplify(c[j + k] / denom)
            row.append(Bij)
        B.append(row)

    for i, row in enumerate(B, 1):
        print(f"Baris {i}:", [N(val, 6) for val in row])

    # Matriks Generator GRS: (I_k | B)
    print("\nMatriks Generator GRS (I_k | B):")
    for i in range(k):
        identitas = [1 if j == i else 0 for j in range(k)]
        gabung = identitas + [N(val, 6) for val in B[i]]
        print(f"Baris {i+1}:", gabung)

#-------------------------------------------------------------------------------------------------------------

def main():
    sigma = input_sigma()
    order = order_permutasi(sigma)
    modulus = 2 * order

    # Input p yang sesuai syarat
    while True:
        p = int(input(f"Input bilangan prima p yang kongruen dengan 1 mod {modulus}: "))
        if cek_prima(p) and p % modulus == 1:
            break
        else:
            print(f"{p} bukan bilangan prima yang kongruen dengan 1 mod {modulus}. Input ulang!.")

    print("\nSigma:", sigma)
    print("Order permutasi:", order)

    group_Zp = grup_perkalian(p)
    print(f"Grup perkalian (Z/{p}Z)*:", group_Zp)

    H, subgrup_order = subgrup_H(p, order)
    print(f"Subgrup H dari (Z/{p}Z)* dengan orde {subgrup_order}:", H)

    poly_expr = Mpoly(p, H, x)
    print("\nPolinomial Minimal:")
    print(poly_expr)

    D = diskriminan_polynomial(poly_expr, x)

    # GRS Construction
    print("\n=== Konstruksi Kode GRS ===")
    roots = solve(poly_expr, x)
    n = len(roots)

    if n < 2:
        print("Polinomial tidak cukup akar untuk membentuk GRS.")
    else:
        while True:
            k = int(input(f"\nMasukkan dimensi k (k < {n}): "))
            if 1 <= k < n:
                break
            print(f"k harus di antara 1 dan {n-1}")
        konstruksi_kode_grs(roots, k)

# Eksekusi program
if __name__ == "__main__":
    main()
