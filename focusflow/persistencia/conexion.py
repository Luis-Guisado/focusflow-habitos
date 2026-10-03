"""Configuración y creación de la conexión a MySQL.

Las credenciales se leen de variables de entorno para no dejar
contraseñas escritas en el código ni subirlas al repositorio.
"""
import os

import mysql.connector


def obtener_conexion():
    """Crea y retorna una conexión nueva a la base de datos bd_focusflow."""
    return mysql.connector.connect(
        host=os.getenv("FF_DB_HOST", "localhost"),
        user=os.getenv("FF_DB_USER", "root"),
        passwd=os.getenv("FF_DB_PASSWORD", ""),
        database=os.getenv("FF_DB_NAME", "bd_focusflow"),
    )
