"""Entidad Habito del módulo de seguimiento de hábitos de FocusFlow."""

FRECUENCIAS_VALIDAS = ("Diaria", "Semanal", "Mensual")


class Habito:
    """Representa un hábito que el usuario quiere construir."""

    def __init__(self, nombre, descripcion, frecuencia, meta_veces,
                 racha_actual=0, id_habito=None, fecha_creacion=None):
        self.id_habito = id_habito
        self.nombre = nombre
        self.descripcion = descripcion
        self.frecuencia = frecuencia
        self.meta_veces = meta_veces
        self.racha_actual = racha_actual
        self.fecha_creacion = fecha_creacion

    @classmethod
    def desde_fila(cls, fila):
        """Crea un Habito a partir de una fila devuelta por la base de datos."""
        id_habito, nombre, descripcion, frecuencia, meta_veces, racha, fecha = fila
        return cls(nombre, descripcion, frecuencia, meta_veces,
                   racha, id_habito, fecha)

    def a_fila_tabla(self):
        """Devuelve los datos listos para mostrarse en una tabla."""
        return [self.id_habito, self.nombre, self.descripcion,
                self.frecuencia, self.meta_veces, self.racha_actual,
                self.fecha_creacion]

    def __str__(self):
        return f"[{self.id_habito}] {self.nombre} ({self.frecuencia})"
