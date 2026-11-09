"""Miembro premium del gimnasio."""

from .persona import PersonaGimnasio
from .rutina import RutinaPersonalizada


class MiembroPremium(PersonaGimnasio):
    """Miembro con beneficios premium y rutina personalizada (composición)."""

    def __init__(
        self,
        identificacion,
        nombre,
        correo,
        telefono,
        membresia,
        fecha_ingreso,
        objetivo_rutina,
        ejercicios_rutina,
        duracion_rutina_semanas,
    ):
        super().__init__(identificacion, nombre, correo, telefono)
        self._membresia = membresia  # Relación: el miembro tiene una membresía
        self._fecha_ingreso = fecha_ingreso
        # Composición: MiembroPremium crea y contiene su RutinaPersonalizada
        self._rutina = RutinaPersonalizada(
            objetivo=objetivo_rutina,
            ejercicios=ejercicios_rutina,
            duracion_semanas=duracion_rutina_semanas,
        )
        self._sesiones_entrenador_mes = 0

    def get_membresia(self):
        return self._membresia

    def get_fecha_ingreso(self):
        return self._fecha_ingreso

    def get_rutina(self):
        return self._rutina

    def get_sesiones_entrenador_mes(self):
        return self._sesiones_entrenador_mes

    def agendar_sesion_entrenador(self):
        self._membresia.validar_vigencia()
        self._sesiones_entrenador_mes += 1
        print(
            f"Sesión con entrenador agendada para {self._nombre}. "
            f"Sesiones este mes: {self._sesiones_entrenador_mes}"
        )

    def mostrar_informacion(self):
        print(
            f"[Miembro Premium] ID: {self._identificacion} | Nombre: {self._nombre} | "
            f"Correo: {self._correo} | Ingreso: {self._fecha_ingreso} | "
            f"Membresía: {self._membresia.get_tipo()} | Objetivo: {self._rutina.get_objetivo()}"
        )

    def obtener_beneficio_principal(self):
        return (
            f"{self._nombre} tiene acceso total, clases ilimitadas, rutina personalizada "
            f"y acompañamiento de entrenador."
        )

    def calcular_costo_mensual(self):
        """Método propio: costo base + recargo por servicios premium."""
        recargo_premium = 45000
        return self._membresia.get_precio_base() + recargo_premium
