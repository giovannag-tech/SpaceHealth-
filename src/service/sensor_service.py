import random
import time
from datetime import datetime

from src.repository.clima_repository import inserir_leitura

CIDADES = {
    1: "Sao Paulo",
    2: "Campinas",
    3: "Santos",
    4: "Sorocaba"
}

INTERVALO_SEGUNDOS = 5

TEMP_MIN, TEMP_MAX = 22.0, 36.0
CHUVA_MAX = 35.0


def ler_temperatura():
    """Simula leitura de temperatura (sensor DHT22)."""
    return round(random.uniform(TEMP_MIN, TEMP_MAX), 1)


def ler_pluviometro():
    """Simula leitura de pluviometro. 70% de chance de sem chuva."""
    if random.random() < 0.70:
        return 0.0
    return round(random.uniform(1.0, CHUVA_MAX), 1)


def executar():
    print("=" * 50)
    print("  SpaceHealth — Simulador ESP32")
    print("  Sensores: DHT22 + Pluviometro")
    print("=" * 50)
    print(f"  Intervalo de leitura: {INTERVALO_SEGUNDOS}s")
    print(f"  Cidades monitoradas: {len(CIDADES)}")
    print("  Pressione Ctrl+C para encerrar")
    print("=" * 50)

    leituras = 0

    while True:
        for cidade_id, nome in CIDADES.items():
            temperatura = ler_temperatura()
            chuva = ler_pluviometro()

            inserir_leitura(cidade_id, temperatura, chuva)

            agora = datetime.now().strftime("%H:%M:%S")
            print(
                f"[{agora}] {nome:<12} "
                f"| Temp: {temperatura:5.1f}C "
                f"| Chuva: {chuva:5.1f}mm"
            )

        leituras += 1
        print(f"  >> Lote #{leituras} salvo no banco\n")

        time.sleep(INTERVALO_SEGUNDOS)


if __name__ == "__main__":
    try:
        executar()
    except KeyboardInterrupt:
        print("\n[INFO] Simulador encerrado pelo usuario.")
