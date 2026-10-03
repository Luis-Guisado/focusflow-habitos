"""Acceso a datos (CRUD) de la tabla habitos usando consultas parametrizadas."""
from focusflow.modelo.habito import Habito
from focusflow.persistencia.conexion import obtener_conexion


class HabitoDAO:
    """Gestiona las operaciones de inserción, consulta, actualización y
    eliminación de hábitos en MySQL."""

    def __init__(self):
        self.conexion = obtener_conexion()

    def cerrar(self):
        """Cierra la conexión con la base de datos."""
        if self.conexion.is_connected():
            self.conexion.close()

    # ---------- CREATE ----------
    def insertar_habito(self, habito):
        """Inserta un hábito y retorna el número de filas afectadas."""
        consulta = """
            INSERT INTO habitos (nombre, descripcion, frecuencia, meta_veces, racha_actual)
            VALUES (%s, %s, %s, %s, %s)
        """
        valores = (habito.nombre, habito.descripcion, habito.frecuencia,
                   habito.meta_veces, habito.racha_actual)
        return self._ejecutar_escritura(consulta, valores)

    # ---------- READ ----------
    def obtener_todos_los_habitos(self):
        """Retorna una lista con todos los hábitos."""
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM habitos ORDER BY id_habito")
        filas = cursor.fetchall()
        cursor.close()
        return [Habito.desde_fila(fila) for fila in filas]

    def buscar_habito_por_id(self, id_habito):
        """Retorna el hábito con ese id o None si no existe."""
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM habitos WHERE id_habito = %s", (id_habito,))
        fila = cursor.fetchone()
        cursor.close()
        return Habito.desde_fila(fila) if fila else None

    def buscar_habitos_por_nombre(self, texto):
        """Retorna los hábitos cuyo nombre contiene el texto indicado."""
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM habitos WHERE nombre LIKE %s",
                       (f"%{texto}%",))
        filas = cursor.fetchall()
        cursor.close()
        return [Habito.desde_fila(fila) for fila in filas]

    # ---------- UPDATE ----------
    def actualizar_habito(self, habito):
        """Actualiza un hábito existente y retorna las filas afectadas."""
        consulta = """
            UPDATE habitos
            SET nombre = %s, descripcion = %s, frecuencia = %s,
                meta_veces = %s, racha_actual = %s
            WHERE id_habito = %s
        """
        valores = (habito.nombre, habito.descripcion, habito.frecuencia,
                   habito.meta_veces, habito.racha_actual, habito.id_habito)
        return self._ejecutar_escritura(consulta, valores)

    # ---------- DELETE ----------
    def eliminar_habito_por_id(self, id_habito):
        """Elimina un hábito por su id y retorna las filas afectadas."""
        return self._ejecutar_escritura(
            "DELETE FROM habitos WHERE id_habito = %s", (id_habito,))

    # ---------- Auxiliar ----------
    def _ejecutar_escritura(self, consulta, valores):
        """Ejecuta INSERT/UPDATE/DELETE con commit y rollback ante errores."""
        cursor = self.conexion.cursor()
        try:
            cursor.execute(consulta, valores)
            filas = cursor.rowcount
            self.conexion.commit()
            return filas
        except Exception:
            self.conexion.rollback()
            raise
        finally:
            cursor.close()
