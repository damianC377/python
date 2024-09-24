class Tripulacion:
    def __init__(self, codigo_tripu, nombretripu):
        self.codigo_tripu = codigo_tripu
        self.nombretripu = nombretripu
    
    def obtenerinfotripu(self):
        return f"Codigo tripu: {self.codigo_tripu} con el nombre: {self.nombretripu}"

class Pilotos:
    def __init__(self, codigo_pilo, nombre_pilo, horas_vuelo):
        self.codigo_pilo = codigo_pilo
        self.nombre_pilo = nombre_pilo
        self.horas_vuelo = horas_vuelo

    def agregar_horas(self, horas):
        self.horas_vuelo += horas

    def obtenerinfopiloto(self):
        return f"Codigo del piloto es: {self.codigo_pilo}, nombre: {self.nombre_pilo}, y sus horas de vuelo son: {self.horas_vuelo}"
        
class Aviones:
    def __init__(self, codigo_avion, tipo):
        self.codigo_avion = codigo_avion
        self.tipo = tipo
    
    def obtenerinfoavion(self):
        return f"El avion con codigo: {self.codigo_avion} es de tipo: {self.tipo}"
    
    def realizar_mantenimiento(self):
        return f"Se le esta realizando mantenimiento al avion: {self.codigo_avion}"

class Base:
    def __init__(self, id_base, nombre_base):
        self.id_base = id_base
        self.nombre_base = nombre_base
    
    def avionmantenimiento(self, avion: Aviones):
        avion.realizar_mantenimiento()

class Vuelo:
    def __init__(self, numerovuelo, origen, destino, horasalida, avion, piloto, tripulacion):
        self.numerovuelo = numerovuelo
        self.origen = origen
        self.destino = destino
        self.horasalida = horasalida
        self.avion = avion
        self.piloto = None
        self.tripulacion = []
    
    def agregarmiembrotriuplacion(self, miembro: Tripulacion):
        self.tripulacion.append(miembro)
    
    def asignar_avion(self, avion:Aviones):
        self.avion = avion
    
    def asignar_piloto(self, piloto: Pilotos):
        self.piloto = piloto
    
    def obtnerinfovuelo(self):
        return f"El vuelo: {self.numerovuelo}, con origen: {self.origen}, destino a: {self.destino}, con hora de salida: {self.horasalida}, subir al avion: {self.avion.obtenerinfoavion()}\n"
        


avion1 = Aviones("A123", "Comercial")
piloto1 = Pilotos(1, "Juan Pérez", 1000)
tripulante1 = Tripulacion(2, "Carlos López")

vuelo1 = Vuelo("VU123", "CDMX", "NY", "10:00 AM", avion1, "", None)
vuelo1.asignar_piloto(piloto1)
vuelo1.agregarmiembrotriuplacion(tripulante1)

print(vuelo1.obtnerinfovuelo())
print(piloto1.obtenerinfopiloto())
print(tripulante1.obtenerinfotripu())