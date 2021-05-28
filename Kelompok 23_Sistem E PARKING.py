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
