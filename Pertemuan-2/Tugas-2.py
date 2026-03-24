def f(x):
    """Mendefinisikan fungsi f(x)"""
    return (1 - 0.6 * x) / x

def bolzano(x1, x2, toleransi, max_iter):
    if f(x1) * f(x2) >= 0:
        print("ERROR: Batas X1 dan X2 tidak mengapit akar (tanda sama).")
        print(f"f(x1) = {f(x1):.5f}, f(x2) = {f(x2):.5f}")
        return

    print("-" * 65)
    print(f"{'Iter':<5} | {'X1':<10} | {'X2':<10} | {'X3':<10} | {'f(X3)':<10}")
    print("-" * 65)

    for i in range(1, max_iter + 1):
        x3 = (x1 + x2) / 2
        fx3 = f(x3)

        print(f"{i:<5} | {x1:<10.5f} | {x2:<10.5f} | {x3:<10.5f} | {fx3:<10.5f}")

        if abs(fx3) < toleransi:
            print("-" * 65)
            print(f"AKAR DITEMUKAN: x = {x3:.5f} pada iterasi ke-{i}")
            return x3

        if f(x1) * fx3 < 0:
            x2 = x3
        else:
            x1 = x3

    print("-" * 65)
    print("Batas iterasi tercapai.")
    return x3

x_bawah = 1.6
x_atas = 1.7
toleransi_error = 0.00001
maksimal_iterasi = 20

bolzano(x_bawah, x_atas, toleransi_error, maksimal_iterasi)
