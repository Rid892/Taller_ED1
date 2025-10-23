class Cliente:
    def __init__(self, nombre, apellido, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.activo = True  # eliminación lógica

    def __str__(self):
        estado = "Activo" if self.activo else "Inactivo"
        return f"{self.nombre} {self.apellido} | Tel: {self.telefono} | Estado: {estado}"


class NodoCliente:
    def __init__(self, cliente):
        self.cliente = cliente
        self.siguiente = None
        self.anterior = None


class ListaClientes:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def registrar_cliente(self, nombre, apellido, telefono):
        nuevo_cliente = Cliente(nombre, apellido, telefono)
        nuevo_nodo = NodoCliente(nuevo_cliente)

        if self.cabeza is None:
            self.cabeza = self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo
        print(f"\n✅ Cliente '{nombre} {apellido}' registrado correctamente.\n")

    def listar_clientes(self):
        if self.cabeza is None:
            print("\n⚠️ No hay clientes registrados.\n")
            return

        print("\n📋 LISTADO DE CLIENTES:")
        actual = self.cabeza
        while actual:
            print(actual.cliente)
            actual = actual.siguiente
        print()

    def eliminar_cliente(self, telefono):
        actual = self.cabeza
        while actual:
            if actual.cliente.telefono == telefono:
                if not actual.cliente.activo:
                    print("\n⚠️ El cliente ya está inactivo.\n")
                    return
                actual.cliente.activo = False
                print(f"\n🗑️ Cliente con teléfono {telefono} marcado como inactivo.\n")
                return
            actual = actual.siguiente
        print("\n❌ Cliente no encontrado.\n")


# --------- MENÚ PRINCIPAL ---------
def menu():
    lista = ListaClientes()

    while True:
        print("========== MENÚ PRINCIPAL ==========")
        print("1. Registrar un cliente")
        print("2. Listar clientes")
        print("3. Eliminar un cliente (lógico)")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            telefono = input("Teléfono: ")
            lista.registrar_cliente(nombre, apellido, telefono)

        elif opcion == "2":
            lista.listar_clientes()

        elif opcion == "3":
            telefono = input("Ingrese el teléfono del cliente a eliminar: ")
            lista.eliminar_cliente(telefono)

        elif opcion == "4":
            print("\n👋 Saliendo del sistema...")
            break
        else:
            print("\n❌ Opción inválida. Intente de nuevo.\n")


# Ejecución del programa
if __name__ == "__main__":
    menu()
