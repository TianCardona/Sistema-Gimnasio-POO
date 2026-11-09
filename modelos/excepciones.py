"""Excepciones personalizadas para el Sistema de Gestión de Gimnasio."""


class GimnasioException(Exception):
    """Excepción base del sistema de gimnasio."""

    pass


class MembresiaVencidaException(GimnasioException):
    """Se lanza cuando un miembro intenta usar servicios con membresía vencida o inactiva."""

    pass


class CupoClaseException(GimnasioException):
    """Se lanza cuando se intenta reservar una clase sin cupo disponible."""

    pass


class ReservaInvalidaException(GimnasioException):
    """Se lanza cuando una reserva es inválida (duplicada, datos incorrectos, etc.)."""

    pass
