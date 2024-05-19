def hitung_biaya_bahan_bakar(jarak, liter_per_km, biaya_per_liter):
    total_liter = jarak * liter_per_km
    total_biaya = total_liter * biaya_per_liter
    return total_liter, total_biaya


jarak = 50  
liter_per_km = 1  
biaya_per_liter = 10000  
total_liter, total_biaya = hitung_biaya_bahan_bakar(jarak, liter_per_km, biaya_per_liter)

print(f"Total liter bahan bakar yang dibutuhkan: {total_liter} liter")
print(f"Total biaya yang dikeluarkan: Rp{total_biaya}")
