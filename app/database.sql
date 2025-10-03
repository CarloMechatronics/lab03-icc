-- database.sql
-- Base solo para gestión de usuarios (login + panel de administración + CRUD)

-- Si ya tienes una tabla y quieres eliminarla antes de crear esta, descomenta la siguiente línea:
-- DROP TABLE IF EXISTS `usuarios`;

-- 1) Crear base de datos
CREATE DATABASE IF NOT EXISTS `lab03-icc`
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE `lab03-icc`;

-- 2) Crear tabla de usuarios
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `nombre` VARCHAR(100) NOT NULL,
  `email` VARCHAR(120) NOT NULL UNIQUE,
  `password` VARCHAR(255) NOT NULL,
  `rol` ENUM('admin','usuario') NOT NULL DEFAULT 'admin',
  `fecha_creacion` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- 3) Datos de ejemplo (8 usuarios)
-- Passwords en texto plano solo para pruebas: formato = inicial + apellido + 123 (todo en minúsculas)
INSERT INTO `usuarios` (`nombre`, `email`, `password`, `rol`) VALUES
('Ana Garcia',      'ana.garcia@lab03-icc.com',      'agarcia123',    'admin'),
('Juan Perez',      'juan.perez@lab03-icc.com',      'jperez123',     'admin'),
('Lucia Fernandez', 'lucia.fernandez@lab03-icc.com', 'lfernandez123', 'admin'),
('Carlos Ramirez',  'carlos.ramirez@lab03-icc.com',  'cramirez123',   'admin'),
('Maria Torres',    'maria.torres@lab03-icc.com',    'mtorres123',    'admin'),
('Diego Suarez',    'diego.suarez@lab03-icc.com',    'dsuarez123',    'admin'),
('Sofia Morales',   'sofia.morales@lab03-icc.com',   'smorales123',   'admin'),
('Andres Castillo', 'andres.castillo@lab03-icc.com', 'acastillo123',  'admin');
