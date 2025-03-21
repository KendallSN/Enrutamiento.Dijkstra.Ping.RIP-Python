class Router:
    def __init__(self, name):
        self.name = name
        self.table = {}
    
    def add_route(self, dest, cost):
        self.table[dest] = cost
    
    def update_table(self, other_router):
        for dest, cost in other_router.table.items():
            if dest not in self.table or self.table[dest] > cost + 1:
                self.table[dest] = cost + 1
    
    def show_table(self):
        print(f"Tabla de rutas de {self.name}: {self.table}")

r1 = Router("R1")
r2 = Router("R2")
r3 = Router("R3")

r1.add_route("R2", 1)
r2.add_route("R3", 1)

r2.update_table(r1)
r3.update_table(r2)

r1.show_table()
r2.show_table()
r3.show_table()
