# Documento de Decisiones de Diseño
## Proyecto Final - Sistema de Gestión de Gimnasio

**Curso:** Programación Orientada a Objetos  
**Proyecto:** Sistema de Gestión de Gimnasio  
**Repositorio:** *(Completar con el enlace del repositorio de GitHub del proyecto final)*  

### Integrantes
- *(Nombre completo - integrante 1)*
- *(Nombre completo - integrante 2)*
- *(Nombre completo - integrante 3)*
- *(Nombre completo - integrante 4)*
- *(Nombre completo - integrante 5, si aplica)*

---

## 1. Introducción

Este documento presenta las decisiones de diseño tomadas durante el desarrollo de un **Sistema de Gestión de Gimnasio** implementado en Python. El propósito del sistema es administrar información básica del gimnasio: personas vinculadas (miembros y entrenadores), membresías, rutinas personalizadas y reservas de clases grupales, aplicando de manera integrada los conceptos de Programación Orientada a Objetos estudiados en el módulo.

El contexto seleccionado es un **gimnasio**, diferente a los escenarios trabajados previamente (biblioteca, tienda/comercio y universidad/sistema académico). A partir de este dominio se definieron clases, relaciones, validaciones y excepciones coherentes con situaciones reales del negocio.

## 2. Descripción general de la solución propuesta

La solución se organizó en un paquete `modelos/` que contiene las entidades del dominio y un archivo `main.py` que ejecuta casos normales y excepcionales. La estructura permite separar responsabilidades: `PersonaGimnasio` actúa como abstracción base; `MiembroRegular`, `MiembroPremium` y `Entrenador` especializan comportamientos; `Membresia`, `RutinaPersonalizada` y `ReservaClase` representan componentes del dominio; y `excepciones.py` concentra el manejo de errores personalizados.

El sistema crea al menos ocho objetos para evidenciar su funcionamiento, recorre una colección heterogénea para demostrar polimorfismo y utiliza `try/except` para capturar excepciones personalizadas sin interrumpir la ejecución.

## 3. Problema específico que resuelve el sistema

El sistema resuelve la necesidad de **gestionar de forma estructurada la información operativa básica de un gimnasio**: registrar personas con roles distintos, asociar membresías a los miembros, controlar el acceso a servicios según la vigencia de la membresía, personalizar rutinas para miembros premium, y administrar la inscripción a clases grupales con control de cupo y validación de duplicados.

De esta forma, el sistema no solo almacena datos, sino que aplica reglas del dominio (vigencia, cupos, reservas válidas) y responde adecuadamente ante situaciones anormales mediante excepciones personalizadas.

## 4. Clases principales y responsabilidades

| Clase | Tipo | Responsabilidad principal |
|---|---|---|
| `PersonaGimnasio` | Abstracta | Define la estructura y comportamiento común de las personas del gimnasio (identificación, nombre, correo, teléfono) y obliga a implementar métodos específicos. |
| `MiembroRegular` | Concreta (hija) | Representa un miembro con acceso básico; gestiona visitas y calcula su costo mensual. |
| `MiembroPremium` | Concreta (hija) | Representa un miembro con beneficios avanzados; compone una rutina personalizada y gestiona sesiones con entrenador. |
| `Entrenador` | Concreta (hija) | Representa al profesional que dirige entrenamientos/clases; gestiona especialidad, tarifa y sesiones realizadas. |
| `Membresia` | Concreta | Modela el plan contratado, su precio, vigencia y estado; valida si puede usarse para acceder a servicios. |
| `RutinaPersonalizada` | Concreta | Contiene el objetivo, ejercicios y duración de la rutina de un miembro premium. |
| `ReservaClase` | Concreta | Administra una clase grupal programada, su entrenador, cupo e inscritos, aplicando reglas de inscripción. |
| Excepciones (`MembresiaVencidaException`, `CupoClaseException`, `ReservaInvalidaException`) | Concretas | Representan situaciones anormales del dominio y permiten un manejo claro de errores. |

En total se implementan **7 clases concretas de dominio + 1 clase abstracta + 3 excepciones personalizadas** (además de la excepción base `GimnasioException`).

## 5. Clase abstracta y justificación

Se definió `PersonaGimnasio` como **clase abstracta** utilizando `abc.ABC` y el decorador `@abstractmethod`. Esta clase **no debe instanciarse** porque representa un concepto general: en el gimnasio no existe una "persona genérica" operando sin rol; toda persona relevante en el sistema es, concretamente, un miembro regular, un miembro premium o un entrenador.

La abstracción establece un contrato común mediante los métodos `mostrar_informacion()` y `obtener_beneficio_principal()`, garantizando que cada especialización implemente su propia versión con datos y comportamiento coherentes. Esto refuerza la consistencia del diseño y evita objetos incompletos o ambiguos.

## 6. Herencia y relación “es un”

La relación de herencia implementada es:

- `MiembroRegular` **es un** `PersonaGimnasio`
- `MiembroPremium` **es un** `PersonaGimnasio`
- `Entrenador` **es un** `PersonaGimnasio`

Esta jerarquía representa correctamente una relación de **generalización y especialización**: las tres clases comparten la naturaleza de ser personas vinculadas al gimnasio (identidad y datos de contacto), pero se especializan en responsabilidades y comportamientos distintos. No se utilizó herencia solo para reutilizar código; se usó porque el dominio lo justifica semánticamente.

### Atributos y métodos comunes
Las clases hijas heredan de `PersonaGimnasio` atributos encapsulados como `_identificacion`, `_nombre`, `_correo` y `_telefono`, junto con sus getters/setters y validaciones. También comparten la interfaz de los métodos `mostrar_informacion()` y `obtener_beneficio_principal()` definidos como abstractos.

### Atributos y métodos propios de cada clase hija
- **`MiembroRegular`:** `_membresia`, `_fecha_ingreso`, `_visitas_mes`; métodos propios `registrar_visita()` y `calcular_costo_mensual()`.
- **`MiembroPremium`:** `_membresia`, `_fecha_ingreso`, `_rutina` (composición), `_sesiones_entrenador_mes`; métodos propios `agendar_sesion_entrenador()`, `get_rutina()` y `calcular_costo_mensual()`.
- **`Entrenador`:** `_especialidad`, `_anos_experiencia`, `_tarifa_sesion`, `_sesiones_realizadas`; métodos propios `registrar_sesion()` y `calcular_pago_estimado_mes()`.

## 7. Sobreescritura de métodos

Las tres clases hijas sobrescriben los mismos dos métodos de la clase abstracta:

1. **`mostrar_informacion()`**: aunque conserva el mismo nombre en todas las clases, cada implementación presenta datos específicos del rol. Por ejemplo, `MiembroRegular` muestra fecha de ingreso y tipo de membresía; `MiembroPremium` añade el objetivo de su rutina; `Entrenador` muestra especialidad, experiencia y tarifa.
2. **`obtener_beneficio_principal()`**: devuelve un mensaje distinto según el tipo de objeto. El miembro regular recibe beneficios básicos, el premium obtiene acceso total y acompañamiento, y el entrenador ofrece su servicio especializado. El comportamiento cambia porque usa atributos propios (`_rutina`, `_especialidad`, `_anos_experiencia`, etc.).

Esta sobreescritura permite que el mismo mensaje enviado desde el programa principal produzca resultados coherentes con el tipo real del objeto.

## 8. Polimorfismo en el programa principal

En `main.py` se crea una **única colección heterogénea** llamada `personas_gimnasio` que contiene instancias de `MiembroRegular`, `MiembroPremium` y `Entrenador` mezcladas en la misma lista. Luego, esa colección se recorre con **un solo ciclo `for`** que invoca `mostrar_informacion()` y `obtener_beneficio_principal()` sobre cada elemento.

No se utilizan condicionales (`if`, `isinstance`, `type`) para decidir qué método ejecutar. Python resuelve dinámicamente la llamada según el tipo real del objeto, evidenciando el polimorfismo.

## 9. Relaciones entre objetos y composición

Se implementaron las relaciones requeridas:

- **Relación 1 (asociación):** `MiembroRegular` y `MiembroPremium` **tienen una** `Membresia` (`self._membresia`). La membresía existe como objeto independiente y puede ser consultada/validada por el miembro.
- **Relación 2 (asociación):** `ReservaClase` se relaciona con un `Entrenador` (`self._entrenador`) y con los miembros inscritos (`self._miembros_inscritos`). Esto modela que una clase grupal es dirigida por un entrenador y recibe participantes.

- **Composición:** `MiembroPremium` **compone** una `RutinaPersonalizada`. En el constructor de `MiembroPremium` se crea internamente el objeto `RutinaPersonalizada` a partir de los datos recibidos (`self._rutina = RutinaPersonalizada(...)`). Esta relación se modeló como composición porque la rutina personalizada es **parte esencial** del servicio premium dentro del diseño del sistema: se define junto con el miembro premium y representa un componente propio de su plan. No se resolvió mediante herencia porque un miembro premium **no es** una rutina; simplemente **tiene** una rutina como parte de su estructura.

## 10. Excepciones personalizadas

Se definieron tres excepciones personalizadas (heredando de `GimnasioException`) para controlar situaciones anormales del dominio:

1. **`MembresiaVencidaException`:** controla el intento de usar servicios cuando la membresía está inactiva o vencida. Se lanza desde `Membresia.validar_vigencia()` y se captura en `main.py` al intentar inscribir un miembro con membresía vencida.
2. **`CupoClaseException`:** controla la inscripción a una clase grupal sin cupo disponible. Se lanza desde `ReservaClase.inscribir_miembro()` cuando se alcanza el cupo máximo y se captura en `main.py`.
3. **`ReservaInvalidaException`:** controla reservas inválidas, como inscribir un miembro duplicado, cancelar una inscripción inexistente o recibir un miembro nulo. Se lanza desde `ReservaClase` y se captura en `main.py`.

En todos los casos, el método responsable lanza la excepción, el programa principal la captura con `try/except`, muestra un mensaje claro y **continúa ejecutándose**, como se evidencia en la sección final de `main.py`.

## 11. Decisiones de diseño modificadas durante el desarrollo

Durante el desarrollo se realizaron ajustes para mantener coherencia con los requisitos:

- Inicialmente se consideró modelar la composición como una relación simple pasada desde fuera; se cambió para que `MiembroPremium` **cree internamente** `RutinaPersonalizada`, haciendo más explícita la composición.
- Se evaluó usar una excepción genérica para reservas, pero se separó en `CupoClaseException` y `ReservaInvalidaException` para que cada situación anormal del dominio tuviera un control específico y mensajes más claros.
- Se decidió que `ReservaClase` validara la vigencia de la membresía antes de inscribir (cuando el objeto tiene membresía), integrando reglas del dominio y conectando la excepción de membresía con el flujo de reservas.

## 12. Herramientas de inteligencia artificial utilizadas

Se utilizó **OpenCode (asistente de IA para programación)** como herramienta de apoyo durante el desarrollo del proyecto.

## 13. Uso dado a cada herramienta

La herramienta se empleó para:
- apoyar la selección y delimitación del contexto (gimnasio) cumpliendo las restricciones del enunciado;
- proponer una estructura inicial de clases, relaciones y responsabilidades;
- generar borradores de código para clases, excepciones y el programa principal;
- revisar la coherencia entre los requisitos (herencia, polimorfismo, composición, excepciones) y la implementación;
- ayudar a redactar una versión base de la documentación técnica.

## 14. Propuestas generadas por IA modificadas, descartadas o corregidas

El equipo revisó críticamente las propuestas generadas:
- Se **ajustaron** nombres, mensajes y validaciones para que correspondieran mejor al dominio del gimnasio.
- Se **modificó** la forma de evidenciar la composición para que `MiembroPremium` instanciara internamente `RutinaPersonalizada`, en lugar de recibirla siempre como objeto externo.
- Se **verificó y corrigió** la lógica de validaciones (cupo, duplicados, vigencia) para asegurar que las excepciones se lanzaran desde los métodos responsables.
- Se **completaron** secciones del documento para integrar las 15 preguntas obligatorias en una redacción continua y alineada con el código real, evitando respuestas genéricas.
- Se **descartaron** sugerencias que agregaban complejidad innecesaria o que no aportaban al cumplimiento de los criterios de evaluación.

## 15. Verificación del funcionamiento y correspondencia con los conceptos

El equipo verificó el proyecto mediante las siguientes acciones:
- Ejecución completa de `main.py` con `python main.py` (y `py main.py` en Windows) para confirmar que el sistema corre sin errores no controlados.
- Revisión de la salida para comprobar la creación de más de ocho objetos, la ejecución de métodos propios, la demostración de composición y el recorrido polimórfico con un único ciclo.
- Pruebas de casos excepcionales para confirmar que `MembresiaVencidaException`, `CupoClaseException` y `ReservaInvalidaException` se lanzan, se capturan con `try/except`, muestran mensajes claros y permiten que el programa continúe.
- Revisión manual del código para validar encapsulamiento (atributos privados y getters/setters), herencia desde la clase abstracta, sobreescritura de los dos métodos en las tres clases hijas y coherencia entre el diagrama UML, el documento de diseño y la implementación.

## 16. Conclusiones

El desarrollo del Sistema de Gestión de Gimnasio permitió aplicar de forma integrada los conceptos de POO en un contexto distinto a los trabajados en clase. La principal dificultad fue diseñar relaciones coherentes (especialmente la composición) sin agregar complejidad innecesaria, manteniendo al mismo tiempo el cumplimiento de todos los requisitos técnicos.

Como aprendizaje, el equipo fortaleció la comprensión de cómo la abstracción, la herencia y el polimorfismo facilitan extender el sistema, y cómo las excepciones personalizadas mejoran la claridad del control de errores cuando se modelan situaciones propias del dominio. El resultado es un proyecto organizado, ejecutable y documentado, con trazabilidad entre el diseño, el código y las decisiones tomadas.
