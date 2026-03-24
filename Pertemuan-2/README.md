### Regula Falsi dengan Python

```
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    """Mendefinisikan fungsi f(x)"""
    return x**3 - 2*x - 5

def regula_falsi(x1, x2, toleransi, max_iter):
    if f(x1) * f(x2) >= 0:
        print("ERROR: Batas x1 dan x2 tidak mengapit akar (tanda sama).")
        return None

    print("-" * 75)
    print(f"{'Iter':<5} | {'X1':<10} | {'X2':<10} | {'X3':<10} | {'f(X3)':<12} | {'Error':<10}")
    print("-" * 75)

    akar_ditemukan = False
    x3 = 0

    for i in range(1, max_iter + 1):
        x3 = x2 - (f(x2) * (x2 - x1)) / (f(x2) - f(x1))
        fx3 = f(x3)

        print(f"{i:<5} | {x1:<10.5f} | {x2:<10.5f} | {x3:<10.5f} | {fx3:<12.5f} | {abs(fx3):<10.5f}")

        if abs(fx3) < toleransi:
            print("-" * 75)
            print(f"AKAR DITEMUKAN: x = {x3:.5f} pada iterasi ke-{i}")
            akar_ditemukan = True
            break

        if f(x1) * fx3 < 0:
            x2 = x3
        else:
            x1 = x3

    if not akar_ditemukan:
        print("-" * 75)
        print("Batas iterasi tercapai tanpa mencapai toleransi yang diinginkan.")
        
    return x3

def plot_grafik(x_bawah, x_atas, akar):
    """Fungsi untuk menampilkan grafik f(x) dan titik akar"""
    x_vals = np.linspace(x_bawah - 1, x_atas + 1, 400)
    y_vals = f(x_vals)

    plt.figure(figsize=(8, 6))
    
    plt.plot(x_vals, y_vals, label='f(x) = x^3 - 2x - 5', color='blue')
    
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    
    if akar is not None:
        plt.plot(akar, f(akar), 'ro', label=f'Akar (x={akar:.5f})')
        plt.vlines(x=akar, ymin=0, ymax=f(akar), colors='red', linestyles='dashed')

    plt.title("Metode Regula Falsi")
    plt.xlabel("Sumbu X")
    plt.ylabel("Sumbu Y")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    
    plt.show()


x_awal = 2.0
x_akhir = 3.0
toleransi_error = 0.00001
maksimal_iterasi = 20

akar_hasil = regula_falsi(x_awal, x_akhir, toleransi_error, maksimal_iterasi)

if akar_hasil is not None:
    plot_grafik(x_awal, x_akhir, akar_hasil)
```
