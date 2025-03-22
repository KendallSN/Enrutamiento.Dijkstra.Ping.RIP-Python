class Router:
    def __init__(self, name):
        self.name = name
        self.table = {}
    
    def add_route(self, dest, cost):
        """Agrega una ruta directa al router."""
        self.table[dest] = cost
    
    def update_table(self, other_router):
        """Actualiza la tabla de rutas basándose en la tabla de otro router."""
        updated = False
        for dest, cost in other_router.table.items():
            if dest not in self.table or self.table[dest] > cost + 1:
                self.table[dest] = cost + 1 
                updated = True 
        return updated 
    
    def show_table(self):
        """Muestra la tabla de rutas del router."""
        print(f"Tabla de rutas de {self.name}:")
        for dest, cost in self.table.items():
            print(f"  Destino: {dest}, Costo: {cost}")
        print()

# Crear routers
r1 = Router("R1")
r2 = Router("R2")
r3 = Router("R3")
r4 = Router("R4")

# Configurar rutas iniciales
r1.add_route("R2", 1)
r2.add_route("R3", 1)
r3.add_route("R4", 1)

# Simular actualizaciones periódicas de tablas
def simulate_rip(routers, iterations=1):
    """Simula el protocolo RIP actualizando tablas entre routers."""
    for i in range(iterations):
        print(f"--- Iteración {i + 1} ---")
        for router in routers:
            for other_router in routers:
                if router != other_router:
                    router.update_table(other_router)
        for router in routers:
            router.show_table()

# Lista de routers
routers = [r1, r2, r3, r4]

# Ejecutar simulación
simulate_rip(routers)
