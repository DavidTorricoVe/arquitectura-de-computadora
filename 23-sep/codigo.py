import subprocess
import time

def mostrar_memoria(etapa):
    """Ejecuta 'free -h' para registrar la evidencia en consola."""
    print(f"\n[{etapa}] Estado de RAM y Swap:")
    subprocess.run(["free", "-h"])
    print("-" * 50)

def saturar():
    bloques = []
    tamano_bloque = 100 * 1024 * 1024  
    total_mb = 0

    mostrar_memoria("ANTES DE INICIAR EL BUCLE")
    print("Iniciando asignación continua...\n")

    try:
        while True:
            bloques.append(bytearray(tamano_bloque))
            total_mb += 100
            print(f"Memoria asignada a Python: {total_mb} MB")
            
            time.sleep(0.1) 
            
    except MemoryError:
        print("\n[!] Python se quedó sin memoria (MemoryError).")
    except KeyboardInterrupt:
        print("\n[i] Interrumpido con Ctrl+C.")
    finally:
        mostrar_memoria("DESPUÉS DEL BUCLE / MÁXIMO CONSUMO")

        del bloques
        print("Memoria liberada.")
        mostrar_memoria("POST-LIBERACIÓN")

if __name__ == "__main__":
    saturar()