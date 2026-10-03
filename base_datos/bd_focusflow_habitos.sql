-- FocusFlow - Modulo de Seguimiento de Habitos
-- Evidencia GA7-220501096-AA2-EV01

CREATE DATABASE IF NOT EXISTS bd_focusflow
    CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

USE bd_focusflow;

CREATE TABLE IF NOT EXISTS habitos (
    id_habito      INT AUTO_INCREMENT PRIMARY KEY,
    nombre         VARCHAR(100) NOT NULL,
    descripcion    TEXT,
    frecuencia     ENUM('Diaria', 'Semanal', 'Mensual') NOT NULL DEFAULT 'Diaria',
    meta_veces     INT NOT NULL DEFAULT 1,
    racha_actual   INT NOT NULL DEFAULT 0,
    fecha_creacion DATE NOT NULL DEFAULT (CURRENT_DATE)
);

INSERT INTO habitos (nombre, descripcion, frecuencia, meta_veces, racha_actual) VALUES
('Beber agua', 'Tomar 8 vasos de agua al día', 'Diaria', 8, 5),
('Leer 20 minutos', 'Lectura de un libro técnico o de desarrollo personal', 'Diaria', 1, 12),
('Hacer ejercicio', 'Rutina de ejercicio de al menos 30 minutos', 'Semanal', 3, 2),
('Estudiar programación', 'Practicar Python y bases de datos', 'Diaria', 2, 7),
('Revisar metas del mes', 'Evaluar el avance de los objetivos mensuales', 'Mensual', 1, 1),
('Meditar', 'Sesión corta de respiración y enfoque', 'Diaria', 1, 3);
