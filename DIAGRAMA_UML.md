# Diagrama UML de Clases - Sistema de Gestión de Gimnasio

```mermaid
classDiagram
    direction TB

    class PersonaGimnasio {
        <<abstract>>
        -_identificacion
        -_nombre
        -_correo
        -_telefono
        +get_identificacion()
        +get_nombre()
        +get_correo()
        +get_telefono()
        +set_nombre(nombre)
        +set_correo(correo)
        +set_telefono(telefono)
        +mostrar_informacion()* 
        +obtener_beneficio_principal()*
    }

    class MiembroRegular {
        -_membresia : Membresia
        -_fecha_ingreso
        -_visitas_mes
        +get_membresia()
        +registrar_visita()
        +calcular_costo_mensual()
        +mostrar_informacion()
        +obtener_beneficio_principal()
    }

    class MiembroPremium {
        -_membresia : Membresia
        -_fecha_ingreso
        -_rutina : RutinaPersonalizada
        -_sesiones_entrenador_mes
        +get_membresia()
        +get_rutina()
        +agendar_sesion_entrenador()
        +calcular_costo_mensual()
        +mostrar_informacion()
        +obtener_beneficio_principal()
    }

    class Entrenador {
        -_especialidad
        -_anos_experiencia
        -_tarifa_sesion
        -_sesiones_realizadas
        +get_especialidad()
        +registrar_sesion()
        +calcular_pago_estimado_mes(sesiones_mes)
        +mostrar_informacion()
        +obtener_beneficio_principal()
    }

    class Membresia {
        -_tipo
        -_precio_base
        -_fecha_vencimiento
        -_activa
        +get_tipo()
        +get_precio_base()
        +validar_vigencia()
        +activar()
        +desactivar()
        +mostrar_informacion()
    }

    class RutinaPersonalizada {
        -_objetivo
        -_ejercicios
        -_duracion_semanas
        +get_objetivo()
        +get_ejercicios()
        +agregar_ejercicio(ejercicio)
        +mostrar_resumen()
    }

    class ReservaClase {
        -_nombre_clase
        -_fecha
        -_hora
        -_entrenador : Entrenador
        -_cupo_maximo
        -_miembros_inscritos
        +inscribir_miembro(miembro)
        +cancelar_inscripcion(miembro)
        +mostrar_informacion()
        +listar_inscritos()
    }

    class GimnasioException {
        <<exception>>
    }
    class MembresiaVencidaException
    class CupoClaseException
    class ReservaInvalidaException

    PersonaGimnasio <|-- MiembroRegular : herencia
    PersonaGimnasio <|-- MiembroPremium : herencia
    PersonaGimnasio <|-- Entrenador : herencia

    MiembroRegular --> Membresia : tiene
    MiembroPremium --> Membresia : tiene
    MiembroPremium *-- RutinaPersonalizada : compone
    ReservaClase --> Entrenador : dirigido por
    ReservaClase --> PersonaGimnasio : inscribe miembros

    GimnasioException <|-- MembresiaVencidaException
    GimnasioException <|-- CupoClaseException
    GimnasioException <|-- ReservaInvalidaException
```

## Notas

- **Herencia (es un):** `MiembroRegular`, `MiembroPremium` y `Entrenador` son tipos especializados de `PersonaGimnasio`.
- **Composición:** `MiembroPremium` crea y contiene una `RutinaPersonalizada`; la rutina forma parte esencial del plan premium.
- **Relaciones:** los miembros tienen una `Membresia`; `ReservaClase` se relaciona con un `Entrenador` y con los miembros inscritos.
- **Excepciones:** jerarquía con clase base `GimnasioException`.
