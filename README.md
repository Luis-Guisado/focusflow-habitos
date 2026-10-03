# FocusFlow – Módulo de Seguimiento de Hábitos

Evidencia **GA7-220501096-AA2-EV01 – Codificación de módulos del software**
Aprendiz: Luis Ángel Guisado Gorredo · SENA – Tecnólogo en Análisis y Desarrollo de Software

Módulo de FocusFlow que gestiona hábitos con operaciones **CRUD** sobre MySQL.
Por indicación del instructor se desarrolla en **Python** (el equivalente de JDBC es
`mysql-connector-python`).

## Estructura (paquetes)

```
focusflow/
├── modelo/          -> Habito (entidad)
└── persistencia/    -> conexion.py (conexión MySQL) y habito_dao.py (CRUD)
base_datos/          -> bd_focusflow_habitos.sql
main_habitos.py      -> menú de consola (capa de presentación)
```

Sigue la separación en capas de la arquitectura MVC de FocusFlow: modelo (`Habito`),
acceso a datos (`HabitoDAO`) y vista/control de consola (`main_habitos.py`).

## Ejecución

1. Instalar dependencias: `pip install -r requirements.txt`
2. Crear la base de datos: ejecutar `base_datos/bd_focusflow_habitos.sql` en MySQL.
3. Definir credenciales (variables de entorno):
   - Windows (CMD): `set FF_DB_PASSWORD=tu_clave`
   - Linux/Mac: `export FF_DB_PASSWORD=tu_clave`
   (opcionales: `FF_DB_HOST`, `FF_DB_USER`, `FF_DB_NAME`)
4. Ejecutar: `python main_habitos.py`

## Funcionalidades

| Operación | Método (HabitoDAO) | SQL |
|---|---|---|
| Inserción | `insertar_habito` | INSERT |
| Consulta | `obtener_todos_los_habitos`, `buscar_habito_por_id`, `buscar_habitos_por_nombre` | SELECT |
| Actualización | `actualizar_habito` | UPDATE |
| Eliminación | `eliminar_habito_por_id` | DELETE |

Todas las consultas son **parametrizadas** (`%s`) para evitar inyección SQL, y las
escrituras usan `commit()` con `rollback()` ante errores.

## Estándares de codificación

- **Paquetes y módulos:** minúsculas (`focusflow.modelo`, `habito_dao.py`).
- **Clases:** PascalCase (`Habito`, `HabitoDAO`).
- **Métodos y funciones:** snake_case con verbo (`insertar_habito`, `buscar_habito_por_id`).
- **Variables:** snake_case descriptivo (`id_habito`, `meta_veces`).
- **Constantes:** MAYÚSCULAS (`FRECUENCIAS_VALIDAS`, `ENCABEZADOS`).
- Docstrings en clases y métodos; validación de entradas en la capa de consola.

## Versionamiento

```
git init
git add .
git commit -m "Módulo de seguimiento de hábitos - CRUD con Python y MySQL"
git branch -M main
git remote add origin <URL_DEL_REPOSITORIO>
git push -u origin main
```
