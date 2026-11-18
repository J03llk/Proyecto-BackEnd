CREATE DATABASE tienda_manga;

USE tienda_manga; 
 
USE tienda_manga;

SELECT COUNT(*) AS total_categorias 
FROM catalogo_categoria;

SELECT COUNT(*) AS total_mangas 
FROM catalogo_manga;

SELECT m.id, m.titulo, c.nombre AS clasificacion
FROM catalogo_manga m
INNER JOIN catalogo_categoria c ON m.categoria_id = c.id;