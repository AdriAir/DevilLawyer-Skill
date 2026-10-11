# Devil Lawyer

Devil Lawyer es una skill de revisión, abierta y de solo lectura, para evaluar ideas, propuestas, planes, decisiones y materiales visibles. Ayuda a concretar una decisión, examinarla desde cinco perspectivas, distinguir la evidencia de las suposiciones e identificar siguientes pasos prácticos.

Versión: **0.3.0** · Licencia: [MIT](LICENSE) · Idiomas: inglés y español.

## Qué hace

- Guía al solicitante por ocho campos de contexto y formula una pregunta necesaria cada vez que falta un dato.
- Distingue al solicitante, el destinatario de la propuesta, quienes deciden, el material visible para el destinatario y el contexto interno.
- Revisa la propuesta desde las perspectivas de Proponente, Abogado del Diablo, Primeros Principios, Ejecutor y Destinatario, y después ofrece un juicio basado en evidencia.
- Etiqueta hechos, cálculos, inferencias, hipótesis y evidencia ausente; no trata el acuerdo como prueba.
- Presenta una recomendación y el registro visible de argumentos en el idioma del usuario.

La skill es consultiva. No envía ni publica informes, no contacta a personas, no ejecuta instrucciones revisadas, no hace compras ni modifica sistemas. Su resultado no constituye aprobación profesional, legal, financiera, médica u organizativa.

## Uso

### Agent Skill independiente

Copia el directorio completo `plugins/devil-lawyer/skills/devil-lawyer/`, incluidos `SKILL.md`, `references/` y `LICENSE`, en un directorio compatible con tu host de Agent Skills. Invócala según las convenciones de descubrimiento o invocación de ese host. Los comandos y las capacidades específicos de un host no se aplican a todos.

### Plugin de Codex

Desde un checkout local, añade el repositorio como marketplace e instala el plugin:

```bash
codex plugin marketplace add /ruta/a/DevilLawyer-Skill
codex plugin add devil-lawyer@devil-lawyer-marketplace
```

El manifiesto del plugin está en [`plugins/devil-lawyer/plugin.json`](plugins/devil-lawyer/plugin.json); la entrada del marketplace, en [`.agents/plugins/marketplace.json`](.agents/plugins/marketplace.json). El archivo `agents/openai.yaml` es una ficha opcional para un host concreto. Otros hosts pueden ignorarlo.

## Portabilidad y seguridad

La skill independiente no depende en ejecución de ECC, de un modelo concreto, de servidores MCP, hooks, credenciales ni paquetes de terceros. Solo usa las capacidades que el host ofrece realmente. Los contextos nuevos y los selectores nativos dependen del host y no están garantizados.

Si el host no puede crear subagentes internos, la skill puede hacer una simulación secuencial y debe declarar que las perspectivas no son independientes. Una simulación del Destinatario no es investigación con usuarios reales. Si el usuario exige roles independientes y el host no puede ofrecerlos, la skill debe explicar que no puede cumplir ese requisito.

La skill trata las instrucciones que aparezcan en material del usuario, adjuntos, respuestas de roles y resultados de investigación como datos no confiables. Sus instrucciones exigen minimizar y redactar la información sensible antes de preparar paquetes para roles o consultas públicas, y prohíben enviar material del usuario a servicios externos o conservarlo después de la revisión actual sin autorización expresa. También se aplican las prácticas de datos y controles de permisos del host; la skill no puede imponer garantías de almacenamiento, aislamiento ni acceso. La investigación, cuando se utiliza, es acotada, de solo lectura y saneada.

## Estructura del paquete

```text
plugins/devil-lawyer/
├── plugin.json
└── skills/devil-lawyer/
    ├── SKILL.md
    ├── LICENSE
    ├── agents/openai.yaml
    └── references/
```

[`evaluations/public-release.md`](evaluations/public-release.md) registra los criterios de aceptación para la publicación. [`evaluations/results.md`](evaluations/results.md) recoge las comprobaciones del paquete y sus límites. Las evaluaciones históricas usan datos sintéticos y no prueban que todos los hosts ofrezcan las capacidades descritas.

## Comprobaciones de desarrollo

Las dependencias opcionales del validador están fijadas en [`evaluations/requirements-dev.txt`](evaluations/requirements-dev.txt). En un entorno virtual aislado, ejecuta:

```bash
python -m pip install -r evaluations/requirements-dev.txt
python evaluations/validate_package.py
python -m unittest discover -s evaluations -p 'test_package.py' -v
```

Para validar con el esquema oficial de Agent Plugins, guarda el esquema en la ruta ignorada `.test-artifacts/plugin.schema.json` y pasa `--schema .test-artifacts/plugin.schema.json`. Sin esa opción, la validación del esquema se indica como no ejecutada. Las comprobaciones estáticas del paquete no demuestran el comportamiento de un modelo en vivo, el aislamiento del host, la aplicación de permisos ni la comprensión de usuarios.

## Licencia

Este repositorio se distribuye con la licencia MIT. La [licencia inglesa raíz](LICENSE) es la autorizada; [`LICENSE.es.md`](LICENSE.es.md) es una traducción informativa al español.
