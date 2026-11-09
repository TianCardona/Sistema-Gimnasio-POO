"""Clase base abstracta para personas vinculadas al gimnasio."""

from abc import ABC, abstractmethod


class PersonaGimnasio(ABC):
    """Información común de cualquier persona en el gimnasio."""

    def __init__(self, identificacion, nombre, correo, telefono):
        self._identificacion = identificacion
        self._nombre = None
        self._correo = None
        self._telefono = None
        self.set_nombre(nombre)
        self.set_correo(correo)
        self.set_telefono(telefono)

    def get_identificacion(self):
        return self._identificacion

    def get_nombre(self):
        return self._nombre

    def get_correo(self):
        return self._correo

    def get_telefono(self):
        return self._telefono

    def set_nombre(self, nombre):
        if nombre is None or not str(nombre).strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = str(nombre).strip()
        return True

    def set_correo(self, correo):
        if correo is None or not str(correo).strip() or "@" not in str(correo):
            raise ValueError("El correo debe ser válido y no puede estar vacío.")
        self._correo = str(correo).strip()
        return True

    def set_telefono(self, telefono):
        if telefono is None or not str(telefono).strip():
            raise ValueError("El teléfono no puede estar vacío.")
        self._telefono = str(telefono).strip()
        return True

    @abstractmethod
    def mostrar_informacion(self):
        """Muestra la información específica de la persona."""
        pass

    @abstractmethod
    def obtener_beneficio_principal(self):
        """Retorna el beneficio principal asociado al tipo de persona."""
        pass
