import winsound
import time
from time import sleep


print("==========================================================")
print()
print('E-PARKING')


# FUNGSI PEMBATAS
def space():
    print()
    print("==========================================================");
    sleep(1)
    print()

    
# LOADING
def wait():
    print("[MOHON TUNGGU SEBENTAR]");
    sleep(0.25)
    print(".", end=" ");
    sleep(0.25)
    print(".", end=" ");
    sleep(0.25)
    print(".");
    sleep(0.25)
    print()

    
# PENGATURAN AWAL PARKING SYSTEM
slot_motor = 20
slot_mobil = 30
jam1_motor = 3600
biaya1_motor = 2000
jam2_motor = 3600
biaya2_motor = 3000
jam1_mobil = 3600
biaya1_mobil = 5000
jam2_mobil = 3600
biaya2_mobil = 7000
space()


# MENUNJUKKAN KETERSEDIAAN SLOT PARKIR
def slot_parkir(motor_count, mobil_count):
    print("[SLOT PARKIR TERSEDIA]")
    print("Mobil =", mobil_count)
    print("Motor =", motor_count)

# MENGHITUNG JUMLAH SLOT PARKIR YANG KOSONG
def count_motor(x):
    motor_count = 0
    for i in range(slot_motor):
        motor_count = motor_count + x[i]
    return motor_count


def count_mobil(y):
    mobil_count = 0
    for i in range(slot_mobil):
        mobil_count = mobil_count + y[i]
    return mobil_count


# KALKULASI HARGA
def perhitungan_motor(durasi):
    harga = 0
    harga1 = 0
    total = 0
    if durasi >= jam1_motor:
        harga1 = harga + biaya1_motor
        durasi = durasi - jam1_motor
        if durasi < 0:
            durasi = 0
        if durasi % jam2_motor > 0:
            durasi = durasi + jam2_motor
        harga = (durasi // jam2_motor) * biaya2_motor
        total = harga1 + harga
    elif durasi < jam1_motor:
        total = biaya1_motor
    return total




def perhitungan_mobil(durasi):
    harga = 0
    harga1 = 0
    if durasi >= jam1_mobil:
        harga1 = harga + biaya1_mobil
        durasi = durasi - jam1_mobil
        if durasi < 0:
            durasi = 0
        elif durasi % jam2_mobil > 0:
            durasi = durasi + jam2_mobil
        harga = (durasi // jam2_mobil) * biaya1_mobil
        total = harga1 + harga
    elif durasi < jam1_mobil:
        total = biaya1_mobil
    return total
