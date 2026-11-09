# Sistema de Gestión de Gimnasio

Proyecto final desarrollado en Python aplicando de forma integrada los conceptos de Programación Orientada a Objetos (POO): encapsulamiento, herencia, clases abstractas, sobreescritura, polimorfismo, composición y manejo de excepciones personalizadas.

## Contexto

El sistema modela la gestión básica de un **gimnasio**, un contexto diferente a los trabajados durante el módulo (biblioteca, tienda, universidad). Permite administrar personas vinculadas al gimnasio (miembros y entrenadores), membresías, rutinas personalizadas y reservas de clases grupales, incluyendo validaciones y manejo de situaciones excepcionales.

## Requisitos del proyecto

- Python 3.10 o superior
- No requiere librerías externas

## Ejecución

Desde la carpeta del proyecto:

```bash
python main.py
```

En Windows también puede usarse:

```bash
py main.py
```

## Estructura del proyecto

```text
Sistema-Gimnasio/
├── main.py                  # Programa principal (casos normales y excepcionales)
├── README.md
├── DECISIONES_DISEÑO.md     # Documento técnico de decisiones de diseño
├── DIAGRAMA_UML.md          # Diagrama UML de clases (Mermaid)
├── diagrama_uml.puml        # Diagrama UML de clases (PlantUML)
├── .gitignore
└── modelos/
    ├── __init__.py
    ├── persona.py           # Clase abstracta PersonaGimnasio
    ├── miembro_regular.py   # Hereda de PersonaGimnasio
    ├── miembro_premium.py   # Hereda de PersonaGimnasio (compone RutinaPersonalizada)
    ├── entrenador.py        # Hereda de PersonaGimnasio
    ├── membresia.py
    ├── rutina.py            # RutinaPersonalizada (composición)
    ├── reserva.py           # ReservaClase (relaciones con miembros y entrenador)
    └── excepciones.py       # Excepciones personalizadas
```

## Conceptos de POO aplicados

- **Clase abstracta:** `PersonaGimnasio` (ABC) con métodos abstractos.
- **Herencia:** `MiembroRegular`, `MiembroPremium` y `Entrenador` heredan de `PersonaGimnasio`.
- **Encapsulamiento:** atributos privados (`_atributo`) con getters/setters y validaciones.
- **Sobreescritura:** `mostrar_informacion()` y `obtener_beneficio_principal()` implementados de forma específica en cada clase hija.
- **Polimorfismo:** colección heterogénea recorrida con un único ciclo, sin condicionales por tipo.
- **Relaciones:** `Miembro`–`Membresia` y `ReservaClase`–`Entrenador`/`Miembro`.
- **Composición:** `MiembroPremium` crea y contiene una `RutinaPersonalizada` como parte esencial.
- **Excepciones personalizadas:** `MembresiaVencidaException`, `CupoClaseException`, `ReservaInvalidaException`.

## Evidencia de funcionamiento

Al ejecutar `main.py` se muestran:
- creación de 12+ objetos,
- uso de métodos propios y relaciones,
- demostración de composición,
- recorrido polimórfico con un único ciclo,
- casos normales de inscripción,
- captura de las 3 excepciones personalizadas con `try/except`,
- continuidad del sistema tras los errores.

## Integrantes

- *(Nombre del integrante 1)*
- *(Nombre del integrante 2)*
- *(Nombre del integrante 3)*
- *(Nombre del integrante 4)*
- *(Nombre del integrante 5, si aplica)*

> Cada integrante debe realizar al menos un commit con una contribución real al desarrollo.

## Uso de herramientas de inteligencia artificial

Se declararon las herramientas de IA utilizadas, su propósito y las modificaciones realizadas en el archivo `DECISIONES_DISEÑO.md`. Todo el código entregado fue revisado, comprendido y verificado por el equipo.
