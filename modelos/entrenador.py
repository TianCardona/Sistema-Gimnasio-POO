"""Entrenador del gimnasio."""

from .persona import PersonaGimnasio


class Entrenador(PersonaGimnasio):
    """Profesional que guía clases y entrenamientos personalizados."""

    def __init__(
        self,
        identificacion,
        nombre,
        correo,
        telefono,
        especialidad,
        anos_experiencia,
        tarifa_sesion,
    ):
        super().__init__(identificacion, nombre, correo, telefono)
        self._especialidad = None
        self._anos_experiencia = None
        self._tarifa_sesion = None
        self.set_especialidad(especialidad)
        self.set_anos_experiencia(anos_experiencia)
        self.set_tarifa_sesion(tarifa_sesion)
        self._sesiones_realizadas = 0

    def get_especialidad(self):
        return self._especialidad

    def get_anos_experiencia(self):
        return self._anos_experiencia

    def get_tarifa_sesion(self):
        return self._tarifa_sesion

    def get_sesiones_realizadas(self):
        return self._sesiones_realizadas

    def set_especialidad(self, especialidad):
        if especialidad is None or not str(especialidad).strip():
            raise ValueError("La especialidad no puede estar vacía.")
        self._especialidad = str(especialidad).strip()
        return True

    def set_anos_experiencia(self, anos_experiencia):
        try:
            valor = int(anos_experiencia)
        except (TypeError, ValueError):
            raise ValueError("Los años de experiencia deben ser un entero.")
        if valor < 0:
            raise ValueError("Los años de experiencia no pueden ser negativos.")
        self._anos_experiencia = valor
        return True

    def set_tarifa_sesion(self, tarifa_sesion):
        try:
            valor = float(tarifa_sesion)
        except (TypeError, ValueError):
            raise ValueError("La tarifa por sesión debe ser un número válido.")
        if valor <= 0:
            raise ValueError("La tarifa por sesión debe ser mayor que cero.")
        self._tarifa_sesion = valor
        return True

    def registrar_sesion(self):
        self._sesiones_realizadas += 1
        print(f"Sesión registrada para el entrenador {self._nombre}.")

    def mostrar_informacion(self):
        print(
            f"[Entrenador] ID: {self._identificacion} | Nombre: {self._nombre} | "
            f"Especialidad: {self._especialidad} | Experiencia: {self._anos_experiencia} años | "
            f"Tarifa: ${self._tarifa_sesion:,.0f}"
        )

    def obtener_beneficio_principal(self):
        return (
            f"{self._nombre} ofrece entrenamiento especializado en {self._especialidad} "
            f"con {self._anos_experiencia} años de experiencia."
        )

    def calcular_pago_estimado_mes(self, sesiones_mes):
        """Método propio: estima el pago mensual según sesiones."""
        return self._tarifa_sesion * max(0, int(sesiones_mes))
