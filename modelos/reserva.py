"""Reserva de clase grupal en el gimnasio."""

from .excepciones import CupoClaseException, ReservaInvalidaException


class ReservaClase:
    """Clase grupal programada con entrenador, cupo y miembros inscritos."""

    def __init__(self, nombre_clase, fecha, hora, entrenador, cupo_maximo):
        self._nombre_clase = None
        self._fecha = None
        self._hora = None
        self._entrenador = entrenador  # Relación: la clase tiene un entrenador
        self._cupo_maximo = None
        self._miembros_inscritos = []  # Relación: la clase tiene miembros inscritos
        self.set_nombre_clase(nombre_clase)
        self.set_fecha(fecha)
        self.set_hora(hora)
        self.set_cupo_maximo(cupo_maximo)

    def get_nombre_clase(self):
        return self._nombre_clase

    def get_fecha(self):
        return self._fecha

    def get_hora(self):
        return self._hora

    def get_entrenador(self):
        return self._entrenador

    def get_cupo_maximo(self):
        return self._cupo_maximo

    def get_miembros_inscritos(self):
        return list(self._miembros_inscritos)

    def set_nombre_clase(self, nombre_clase):
        if nombre_clase is None or not str(nombre_clase).strip():
            raise ValueError("El nombre de la clase no puede estar vacío.")
        self._nombre_clase = str(nombre_clase).strip()
        return True

    def set_fecha(self, fecha):
        if fecha is None or not str(fecha).strip():
            raise ValueError("La fecha no puede estar vacía.")
        self._fecha = str(fecha).strip()
        return True

    def set_hora(self, hora):
        if hora is None or not str(hora).strip():
            raise ValueError("La hora no puede estar vacía.")
        self._hora = str(hora).strip()
        return True

    def set_cupo_maximo(self, cupo_maximo):
        try:
            valor = int(cupo_maximo)
        except (TypeError, ValueError):
            raise ValueError("El cupo máximo debe ser un entero.")
        if valor <= 0:
            raise ValueError("El cupo máximo debe ser mayor que cero.")
        self._cupo_maximo = valor
        return True

    def inscribir_miembro(self, miembro):
        """Inscribe un miembro validando membresía, duplicados y cupo."""
        if miembro is None:
            raise ReservaInvalidaException("El miembro no puede ser nulo.")

        # Validar membresía vigente (si el miembro tiene membresía)
        if hasattr(miembro, "get_membresia"):
            miembro.get_membresia().validar_vigencia()

        # Validar duplicado
        for inscrito in self._miembros_inscritos:
            if inscrito.get_identificacion() == miembro.get_identificacion():
                raise ReservaInvalidaException(
                    f"{miembro.get_nombre()} ya está inscrito en la clase '{self._nombre_clase}'."
                )

        # Validar cupo
        if len(self._miembros_inscritos) >= self._cupo_maximo:
            raise CupoClaseException(
                f"No hay cupo en '{self._nombre_clase}'. Cupo máximo: {self._cupo_maximo}."
            )

        self._miembros_inscritos.append(miembro)
        print(
            f"Inscripción exitosa: {miembro.get_nombre()} en '{self._nombre_clase}' "
            f"({self._fecha} {self._hora})."
        )
        return True

    def cancelar_inscripcion(self, miembro):
        for i, inscrito in enumerate(self._miembros_inscritos):
            if inscrito.get_identificacion() == miembro.get_identificacion():
                self._miembros_inscritos.pop(i)
                print(f"Inscripción cancelada: {miembro.get_nombre()} en '{self._nombre_clase}'.")
                return True
        raise ReservaInvalidaException(
            f"{miembro.get_nombre()} no tiene inscripción en '{self._nombre_clase}'."
        )

    def mostrar_informacion(self):
        print(
            f"Clase: {self._nombre_clase} | Fecha: {self._fecha} {self._hora} | "
            f"Entrenador: {self._entrenador.get_nombre()} | "
            f"Cupo: {len(self._miembros_inscritos)}/{self._cupo_maximo}"
        )

    def listar_inscritos(self):
        print(f"Inscritos en '{self._nombre_clase}':")
        if not self._miembros_inscritos:
            print("  - Sin inscritos.")
            return
        for m in self._miembros_inscritos:
            print(f"  - {m.get_nombre()} ({m.get_identificacion()})")
