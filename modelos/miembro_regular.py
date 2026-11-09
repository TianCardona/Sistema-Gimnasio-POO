"""Miembro regular del gimnasio."""

from .persona import PersonaGimnasio


class MiembroRegular(PersonaGimnasio):
    """Miembro con acceso básico al gimnasio."""

    def __init__(self, identificacion, nombre, correo, telefono, membresia, fecha_ingreso):
        super().__init__(identificacion, nombre, correo, telefono)
        self._membresia = membresia  # Relación: el miembro tiene una membresía
        self._fecha_ingreso = fecha_ingreso
        self._visitas_mes = 0

    def get_membresia(self):
        return self._membresia

    def get_fecha_ingreso(self):
        return self._fecha_ingreso

    def get_visitas_mes(self):
        return self._visitas_mes

    def registrar_visita(self):
        self._membresia.validar_vigencia()
        self._visitas_mes += 1
        print(f"Visita registrada para {self._nombre}. Visitas este mes: {self._visitas_mes}")

    def mostrar_informacion(self):
        print(
            f"[Miembro Regular] ID: {self._identificacion} | Nombre: {self._nombre} | "
            f"Correo: {self._correo} | Ingreso: {self._fecha_ingreso} | "
            f"Membresía: {self._membresia.get_tipo()}"
        )

    def obtener_beneficio_principal(self):
        return f"{self._nombre} tiene acceso a sala de máquinas y clases básicas en horario regular."

    def calcular_costo_mensual(self):
        """Método propio: calcula el costo mensual del miembro regular."""
        return self._membresia.get_precio_base()
