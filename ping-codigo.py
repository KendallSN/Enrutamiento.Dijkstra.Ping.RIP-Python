from scapy.all import *

def ping(host):
    pkt = IP(dst=host)/ICMP()
    reply = sr1(pkt, timeout=2, verbose=False)
    if reply:
        print(f"Respuesta de {host}: {reply.src}")
    else:
        print("Tiempo de espera agotado.")

host = input("Ingresa la IP o dominio a hacer ping: ")
ping(host)
