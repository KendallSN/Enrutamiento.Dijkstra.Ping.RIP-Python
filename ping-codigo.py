from scapy.all import *
from scapy.layers.inet import ICMP, IP

def ping(host):
    pkt = IP(dst=host)/ICMP()
    reply = sr1(pkt, timeout=2, verbose=False)
    if reply:
        print(f"Respuesta de {host}: {reply.src}")
    else:
        print("Tiempo de espera agotado.")

def traceroute_simulation(host, max_hops=30):
    print(f"Iniciando traceroute a {host}...")
    for ttl in range(1, max_hops + 1):
        pkt = IP(dst=host, ttl=ttl)/ICMP()
        reply = sr1(pkt, timeout=2, verbose=False)
        if reply is None:
            print(f"{ttl}: * * * Tiempo de espera agotado.")
        elif reply.type == 0:
            print(f"{ttl}: {reply.src} (Destino alcanzado)")
            break
        else:
            print(f"{ttl}: {reply.src}")
    else:
        print("No se pudo alcanzar el destino.")

host = input("Ingresa la IP o dominio a analizar (ping/traceroute): ")
print("\n--- Simulación de Ping ---")
ping(host)
print("\n--- Simulación de Traceroute ---")
traceroute_simulation(host)