from datetime import datetime


class Ticket:
    def __init__(self,
                 copia=0,
                 fecha=datetime.now().strftime("%d/%m/%Y"),
                 hora=datetime.now().strftime("%H:%M"),
                 posicion=0,
                 consecutivo=0,
                 producto="",
                 ppu=0,
                 volumen=0,
                 dinero=0.0,
                 placa="",
                 vendedor="",
                 line="*******************************"):

        self.time = None
        self.copia = copia
        self.vendedor = vendedor
        self.placa = placa
        self.producto = producto
        self.consecutivo = consecutivo
        self.posicion = posicion
        self.ppu = "$/G " + str(ppu)
        self.volumen = "G " + str(volumen)
        self.dinero = "$ " + str(dinero)
        self.line = line
        self.fecha = fecha
        self.hora = hora

    def modificar(self, opcion):
        opcion = int(opcion)
        if opcion == 1:
            self.copia = int(input("Introduce el nuevo numero de copia: "))
        elif opcion == 2:
            self.fecha = input("Introduce la fecha en formato dia/mes/año: ")
        elif opcion == 3:
            self.hora = input("Introduce la hora en formato HH:MM ")
        elif opcion == 4:
            self.posicion = input("Introduce la nueva posición: ")
        elif opcion == 5:
            self.consecutivo = input("Introduce el nuevo consecutivo: ")
        elif opcion == 6:
            self.producto = input("Introduce el nuevo producto: ")
        elif opcion == 7:
            self.ppu = input("Introduce el nuevo Ppu: ")
        elif opcion == 8:
            self.volumen = input("Introduce el nuevo volumen: ")
        elif opcion == 9:
            self.dinero = input("Introduce el nuevo dinero: ")
        elif opcion == 10:
            self.placa = input("Introduce la nueva placa: ")
        elif opcion == 11:
            self.vendedor = input("Introduce el nuevo vendedor: ")

    def reset(self):
        self.copia = 0
        self.vendedor = 0
        self.placa = 0
        self.producto = 0
        self.consecutivo = 0
        self.posicion = 0
        self.ppu = "$/G "
        self.volumen = "G "
        self.dinero = "$ "
        self.time = datetime.now()
        self.fecha = self.time.strftime("%d/%m/%Y")
        self.hora = self.time.strftime("%H:%M")

    def load_mott(self, file_name):
        with open(file_name, "r") as file:
            data = file.readlines()
        return [line.strip() for line in data]

    def print_mott(self):
        for line in self.load_mott("mott.txt"):
            print(line.center(40, " "))

    def print_ticket(self):
        print("\n\n\n\n")
        print("El ticket que usted ha creado es el siguiente")
        print("")
        self.print_mott()
        print(self.line)
        print("Copia", self.copia)
        print(self.line)
        print(f"{'Fecha': <8}", self.fecha)
        print(f"{'Hora': <8}", self.hora)
        print(self.line)
        print(f'{"Posición": <11}:', self.posicion)
        print(f'{"Consecutivo": <11}:', self.consecutivo)
        print(f"{'Producto': <11}:", self.producto)
        print(f"{'Ppu': <11}:", self.ppu)
        print(f"{'Volumen': <11}:", self.volumen)
        print(f"{'Dinero': <11}:", self.dinero)
        print(f"{'Placa': <11}:", self.placa)
        print(self.line)
        print("Vendedor", self.vendedor, self.vendedor)
        print(self.line)
        print("GRACIAS POR SU COMPRA".center(39, " "))
        print(f"{'': <13}VUELVA PRONTO")

    def save_ticket(self):
        nombre = input("Introduce el nombre del ticket: ") + ".txt"
        try:
            with open("tickets/" + nombre, "w") as file:
                for line in self.load_mott("mott.txt"):
                    file.write(line.center(40, " "))
                    file.write("\n")
                file.write(self.line)
                file.write("\n")
                file.write(f"Copia {self.copia}")
                file.write("\n")
                file.write(self.line)
                file.write("\n")
                file.write(f"{'Fecha': <8} {self.fecha}")
                file.write("\n")
                file.write(f"{'Hora': <8} {self.hora}")
                file.write("\n")
                file.write(self.line)
                file.write("\n")
                file.write(f'{"Posición": <11}: {self.posicion}')
                file.write("\n")
                file.write(f'{"Consecutivo": <11}: {self.consecutivo}')
                file.write("\n")
                file.write(f"{'Producto': <11}: {self.producto}")
                file.write("\n")
                file.write(f"{'Ppu': <11}: {self.ppu}")
                file.write("\n")
                file.write(f"{'Volumen': <11}: {self.volumen}")
                file.write("\n")
                file.write(f"{'Dinero': <11}: {self.dinero}")
                file.write("\n")
                file.write(f"{'Placa': <11}: {self.placa}")
                file.write("\n")
                file.write(self.line)
                file.write("\n")
                file.write(f"Vendedor {self.vendedor} {self.vendedor}")
                file.write("\n")
                file.write(self.line)
                file.write("\n")
                file.write("GRACIAS POR SU COMPRA".center(39, " "))
                file.write("\n")
                file.write(f"{'': <13}VUELVA PRONTO")
        except FileNotFoundError as error:
            print(error.strerror)


def cargar_copia(file_name):
    with open(file_name) as file:
        return file.readline(0)


des = "0"
while des != "4":
    fecha, hora = "", ""
    print("Usted va a generar un nuevo ticket")
    copia = int(input("Introduce el numero de copia: "))
    mf = input("¿Desea modificar la fecha o utilizar la de hoy? \n\t1.- Actual \n\t2.- Modificar \n")
    if mf != "1":
        fecha = input("Introduce la fecha en formato dia/mes/año: ")
    hf = input("¿Desea modificar la hora o utilizar la actual? \n\t1.- Actual \n\t2.- Modificar \n")
    if hf != "1":
        hora = input("Introduce la hora en formato HH:MM: ")
    posicion = input("Introduce la  posición: ")
    consecutivo = input("Introduce el  consecutivo: ")
    producto = input("Introduce el  producto: ")
    ppu = input("Introduce el  Ppu: ")
    volumen = input("Introduce el  volumen: ")
    dinero = input("Introduce el  dinero: ")
    placa = input("Introduce la  placa: ")
    vendedor = input("Introduce el vendedor: ")

    if fecha != "":
        ticket = Ticket(copia, fecha, hora, int(posicion), int(consecutivo), producto, int(ppu), int(volumen),
                        float(dinero), placa, vendedor)
        ticket.print_ticket()
    else:
        ticket = Ticket(copia, posicion=int(posicion), consecutivo=int(consecutivo), producto=producto, ppu=int(ppu),
                        volumen=int(volumen), dinero=float(dinero), placa=placa, vendedor=vendedor)
        ticket.print_ticket()

    des = input("¿Que desea hacer? \n\t1.-Exportar a txt y crear nuevo \n\t2.-Editar \n\t3.-Nuevo \n\t4.Quitar programa(Puede perder información si "
                "no exporto antes)")
    if des == "2":
        opcion = input("¿Que desea modificar? \n\t1.Copia\n\t2.Fecha\n\t3.Hora\n\t4.Posición\n\t5.Consecutivo\n\t6"
                       ".Producto"
                       "\n\t7.Ppu\n\t8.Volumen\n\t9.Dinero\n\t10.Placa\n\t11.Vendedor")
        ticket.modificar(opcion)
        ticket.print_ticket()
        des = input(
            "¿Que desea hacer? 1.-Exportar a txt 2.-Editar 3.-Nuevo 4.Quitar programa(Puede perder información si "
            "no exporto antes)")
    elif des == "1":
        ticket.save_ticket()
    print("\n\n\n")


print("Gracias por usar el programa")
