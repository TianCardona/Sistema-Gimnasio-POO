"""
Sistema de Gestión de Gimnasio - Programa principal.

Demuestra la aplicación integrada de POO: encapsulamiento, herencia,
clases abstractas, sobreescritura, polimorfismo, composición y
excepciones personalizadas en un contexto de gimnasio.
"""

from datetime import date, timedelta

from modelos import (
    CupoClaseException,
    Entrenador,
    GimnasioException,
    Membresia,
    MiembroPremium,
    MiembroRegular,
    MembresiaVencidaException,
    ReservaClase,
    ReservaInvalidaException,
)


def separador(titulo):
    print("\n" + "=" * 72)
    print(titulo)
    print("=" * 72)


def main():
    separador("1. CREACIÓN DE OBJETOS (mínimo 8) - Membresías y personas")

    hoy = date.today()
    membresia_regular_1 = Membresia("Regular Mensual", 80000, hoy + timedelta(days=30))
    membresia_regular_2 = Membresia("Regular Trimestral", 70000, hoy + timedelta(days=90))
    membresia_premium_1 = Membresia("Premium Gold", 150000, hoy + timedelta(days=30))
    membresia_premium_2 = Membresia("Premium Platinum", 180000, hoy + timedelta(days=60))
    membresia_vencida = Membresia("Regular Vencida", 80000, hoy - timedelta(days=5))

    miembro_r1 = MiembroRegular(
        "M001", "Ana López", "ana.lopez@gym.com", "3001112233",
        membresia_regular_1, hoy - timedelta(days=120)
    )
    miembro_r2 = MiembroRegular(
        "M002", "Carlos Ruiz", "carlos.ruiz@gym.com", "3002223344",
        membresia_regular_2, hoy - timedelta(days=45)
    )
    miembro_p1 = MiembroPremium(
        "P001", "María Gómez", "maria.gomez@gym.com", "3003334455",
        membresia_premium_1, hoy - timedelta(days=200),
        objetivo_rutina="Pérdida de grasa",
        ejercicios_rutina=["Sentadillas", "Cardio HIIT", "Peso muerto", "Plancha"],
        duracion_rutina_semanas=8,
    )
    miembro_p2 = MiembroPremium(
        "P002", "Julián Torres", "julian.torres@gym.com", "3004445566",
        membresia_premium_2, hoy - timedelta(days=60),
        objetivo_rutina="Ganancia muscular",
        ejercicios_rutina=["Press banca", "Dominadas", "Remo", "Curl bíceps"],
        duracion_rutina_semanas=12,
    )
    miembro_con_vencida = MiembroRegular(
        "M003", "Pedro Mora", "pedro.mora@gym.com", "3005556677",
        membresia_vencida, hoy - timedelta(days=400)
    )

    entrenador_1 = Entrenador(
        "E001", "Laura Pérez", "laura.perez@gym.com", "3101112233",
        especialidad="Funcional y CrossFit", anos_experiencia=6, tarifa_sesion=60000
    )
    entrenador_2 = Entrenador(
        "E002", "Diego Sánchez", "diego.sanchez@gym.com", "3102223344",
        especialidad="Hipertrofia y fuerza", anos_experiencia=10, tarifa_sesion=75000
    )

    # Relación: ReservaClase se relaciona con Entrenador y con Miembros
    clase_spinning = ReservaClase(
        nombre_clase="Spinning Intenso",
        fecha=str(hoy + timedelta(days=1)),
        hora="06:30",
        entrenador=entrenador_1,
        cupo_maximo=2,
    )

    print(f"Objetos creados: {4} membresías, {5} miembros, {2} entrenadores, {1} clase = 12 objetos.")

    separador("2. MÉTODOS PROPIOS Y RELACIONES ENTRE OBJETOS")
    miembro_r1.registrar_visita()
    miembro_p1.agendar_sesion_entrenador()
    entrenador_2.registrar_sesion()
    print(f"Costo mensual {miembro_r1.get_nombre()}: ${miembro_r1.calcular_costo_mensual():,.0f}")
    print(f"Costo mensual {miembro_p1.get_nombre()}: ${miembro_p1.calcular_costo_mensual():,.0f}")
    print(f"Pago estimado (8 sesiones) {entrenador_2.get_nombre()}: ${entrenador_2.calcular_pago_estimado_mes(8):,.0f}")

    separador("3. COMPOSICIÓN - MiembroPremium contiene RutinaPersonalizada")
    print("El miembro premium compone (contiene) su rutina personalizada como parte esencial:")
    miembro_p1.mostrar_informacion()
    miembro_p1.get_rutina().mostrar_resumen()
    print("\nModificando la rutina compuesta (agregando ejercicio):")
    miembro_p1.get_rutina().agregar_ejercicio("Estiramiento guiado")
    miembro_p1.get_rutina().mostrar_resumen()

    separador("4. POLIMORFISMO - Colección heterogénea (un solo ciclo)")
    # Colección heterogénea: objetos de las 3 clases hijas de PersonaGimnasio
    personas_gimnasio = [
        miembro_r1,
        miembro_r2,
        miembro_p1,
        miembro_p2,
        entrenador_1,
        entrenador_2,
    ]
    print("Recorriendo UNA sola lista con MiembroRegular, MiembroPremium y Entrenador.")
    print("Se invocan los mismos métodos sin condicionales por tipo.\n")
    for persona in personas_gimnasio:
        persona.mostrar_informacion()           # método sobrescrito
        print(f"  Beneficio: {persona.obtener_beneficio_principal()}")  # sobrescrito
        print("-" * 72)

    separador("5. CASOS NORMALES - Inscripciones a clase (relaciones)")
    clase_spinning.mostrar_informacion()
    try:
        clase_spinning.inscribir_miembro(miembro_r1)
        clase_spinning.inscribir_miembro(miembro_p1)
        clase_spinning.listar_inscritos()
    except GimnasioException as e:
        print(f"Error inesperado: {e}")

    separador("6. EXCEPCIONES PERSONALIZADAS - Casos excepcionales (try/except)")

    print("Caso 1: CupoClaseException (clase llena)")
    try:
        clase_spinning.inscribir_miembro(miembro_p2)
    except CupoClaseException as e:
        print(f"EXCEPCIÓN CAPTURADA [CupoClaseException]: {e}")
    except GimnasioException as e:
        print(f"EXCEPCIÓN CAPTURADA: {e}")

    print("\nCaso 2: ReservaInvalidaException (miembro ya inscrito)")
    try:
        clase_spinning.inscribir_miembro(miembro_r1)
    except ReservaInvalidaException as e:
        print(f"EXCEPCIÓN CAPTURADA [ReservaInvalidaException]: {e}")
    except GimnasioException as e:
        print(f"EXCEPCIÓN CAPTURADA: {e}")

    print("\nCaso 3: MembresiaVencidaException (membresía vencida al inscribirse)")
    clase_yoga = ReservaClase(
        nombre_clase="Yoga Matutino",
        fecha=str(hoy + timedelta(days=2)),
        hora="07:00",
        entrenador=entrenador_2,
        cupo_maximo=10,
    )
    try:
        clase_yoga.inscribir_miembro(miembro_con_vencida)
    except MembresiaVencidaException as e:
        print(f"EXCEPCIÓN CAPTURADA [MembresiaVencidaException]: {e}")
    except GimnasioException as e:
        print(f"EXCEPCIÓN CAPTURADA: {e}")

    separador("7. DEMOSTRACIÓN DE CONTINUIDAD DEL SISTEMA")
    print("El sistema continúa ejecutándose después de capturar las excepciones.\n")
    try:
        # Cancelar y reinscribir para mostrar flujo normal
        clase_spinning.cancelar_inscripcion(miembro_r1)
        clase_spinning.inscribir_miembro(miembro_p2)
        clase_spinning.listar_inscritos()
        clase_yoga.inscribir_miembro(miembro_r2)
        clase_yoga.mostrar_informacion()
        clase_yoga.listar_inscritos()
    except GimnasioException as e:
        print(f"Error: {e}")

    separador("RESUMEN DE CONCEPTOS APLICADOS")
    print("- Contexto: Gimnasio (diferente a biblioteca, tienda, universidad)")
    print("- Clase abstracta: PersonaGimnasio (ABC) con 2 métodos abstractos")
    print("- Herencia: MiembroRegular, MiembroPremium, Entrenador heredan de PersonaGimnasio")
    print("- Encapsulamiento: atributos privados con getters/setters y validaciones")
    print("- Sobreescritura: mostrar_informacion() y obtener_beneficio_principal() en cada hija")
    print("- Polimorfismo: colección heterogénea recorrida con un único ciclo")
    print("- Relaciones: Miembro-Membresia, ReservaClase-Entrenador/Miembros")
    print("- Composición: MiembroPremium contiene RutinaPersonalizada")
    print("- Excepciones: MembresiaVencidaException, CupoClaseException, ReservaInvalidaException")
    print("\n¡Sistema de Gestión de Gimnasio ejecutado correctamente!")


if __name__ == "__main__":
    main()
