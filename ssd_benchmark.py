import time
import os

# Configuramos el test: vamos a escribir un archivo de 1GB
file_name = "test_bench.bin"
file_size_gb = 1
file_size_bytes = file_size_gb * 1024 * 1024 * 1024

print(f"--- Iniciando Benchmark de Disco (Escribiendo {file_size_gb}GB) ---")

data = os.urandom(1024 * 1024) # 1MB de datos aleatorios en RAM
start_time = time.time()

with open(file_name, "wb") as f:
    for _ in range(file_size_gb * 1024):
        f.write(data)
with open(file_name, "wb") as f:
    for _ in range(file_size_gb * 1024):
        f.write(data)
    
    f.flush()            # Limpia el buffer interno de Python
    os.fsync(f.fileno()) # OBLIGA a Windows a escribir en el disco físico antes de seguir
end_time = time.time()
total_time = end_time - start_time
write_speed = file_size_gb * 1024 / total_time

print(f"Tiempo total: {round(total_time, 2)} segundos")
print(f"Velocidad de escritura real: {round(write_speed, 2)} MB/s")

# Limpieza
os.remove(file_name)