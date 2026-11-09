"""Rutina personalizada para miembros premium (parte esencial en composición)."""


class RutinaPersonalizada:
    """Representa una rutina de entrenamiento diseñada para un miembro premium."""

    def __init__(self, objetivo, ejercicios, duracion_semanas):
        self._objetivo = None
        self._ejercicios = None
        self._duracion_semanas = None
        self.set_objetivo(objetivo)
        self.set_ejercicios(ejercicios)
        self.set_duracion_semanas(duracion_semanas)

    def get_objetivo(self):
        return self._objetivo

    def get_ejercicios(self):
        return list(self._ejercicios)

    def get_duracion_semanas(self):
        return self._duracion_semanas

    def set_objetivo(self, objetivo):
        if objetivo is None or not str(objetivo).strip():
            raise ValueError("El objetivo de la rutina no puede estar vacío.")
        self._objetivo = str(objetivo).strip()
        return True

    def set_ejercicios(self, ejercicios):
        if not isinstance(ejercicios, list) or len(ejercicios) == 0:
            raise ValueError("La rutina debe incluir al menos un ejercicio.")
        ejercicios_limpios = [str(e).strip() for e in ejercicios if str(e).strip()]
        if not ejercicios_limpios:
            raise ValueError("La rutina debe incluir al menos un ejercicio válido.")
        self._ejercicios = ejercicios_limpios
        return True

    def set_duracion_semanas(self, duracion_semanas):
        try:
            valor = int(duracion_semanas)
        except (TypeError, ValueError):
            raise ValueError("La duración en semanas debe ser un entero.")
        if valor <= 0:
            raise ValueError("La duración en semanas debe ser mayor que cero.")
        self._duracion_semanas = valor
        return True

    def agregar_ejercicio(self, ejercicio):
        if ejercicio is None or not str(ejercicio).strip():
            raise ValueError("El ejercicio no puede estar vacío.")
        self._ejercicios.append(str(ejercicio).strip())

    def mostrar_resumen(self):
        print(
            f"Rutina: {self._objetivo} | Duración: {self._duracion_semanas} semanas | "
            f"Ejercicios: {', '.join(self._ejercicios)}"
        )
