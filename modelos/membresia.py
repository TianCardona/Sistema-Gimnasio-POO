"""Membresía de un miembro del gimnasio."""

from datetime import date

from .excepciones import MembresiaVencidaException


class Membresia:
    """Representa el plan de membresía asociado a un miembro."""

    def __init__(self, tipo, precio_base, fecha_vencimiento, activa=True):
        self._tipo = None
        self._precio_base = None
        self._fecha_vencimiento = None
        self._activa = bool(activa)
        self.set_tipo(tipo)
        self.set_precio_base(precio_base)
        self.set_fecha_vencimiento(fecha_vencimiento)

    def get_tipo(self):
        return self._tipo

    def get_precio_base(self):
        return self._precio_base

    def get_fecha_vencimiento(self):
        return self._fecha_vencimiento

    def esta_activa(self):
        return self._activa

    def set_tipo(self, tipo):
        if tipo is None or not str(tipo).strip():
            raise ValueError("El tipo de membresía no puede estar vacío.")
        self._tipo = str(tipo).strip()
        return True

    def set_precio_base(self, precio_base):
        try:
            valor = float(precio_base)
        except (TypeError, ValueError):
            raise ValueError("El precio base debe ser un número válido.")
        if valor <= 0:
            raise ValueError("El precio base debe ser mayor que cero.")
        self._precio_base = valor
        return True

    def set_fecha_vencimiento(self, fecha_vencimiento):
        if not isinstance(fecha_vencimiento, date):
            raise ValueError("La fecha de vencimiento debe ser un objeto date.")
        self._fecha_vencimiento = fecha_vencimiento
        return True

    def desactivar(self):
        self._activa = False

    def activar(self):
        self._activa = True

    def validar_vigencia(self):
        """Lanza excepción si la membresía no es válida para usar servicios."""
        if not self._activa:
            raise MembresiaVencidaException(
                f"La membresía '{self._tipo}' se encuentra inactiva."
            )
        if self._fecha_vencimiento < date.today():
            raise MembresiaVencidaException(
                f"La membresía '{self._tipo}' venció el {self._fecha_vencimiento}."
            )
        return True

    def mostrar_informacion(self):
        estado = "Activa" if self._activa else "Inactiva"
        print(
            f"Membresía: {self._tipo} | Precio base: ${self._precio_base:,.0f} | "
            f"Vence: {self._fecha_vencimiento} | Estado: {estado}"
        )
