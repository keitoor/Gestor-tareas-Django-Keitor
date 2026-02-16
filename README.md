La API responde en: http://127.0.0.1:8000/

- GET    /lists/                        → ver todas las listas  
- POST   /lists/                        → crear lista nueva (body: {"name": "Mi lista"})  
- DELETE /lists/<id>/                   → borrar lista (y sus tareas)  

- GET    /lists/<id>/tasks/             → ver tareas de esa lista  
- POST   /lists/<id>/tasks/             → añadir tarea (body: {"title": "Hacer entrega"})  
- PATCH  /lists/<id>/tasks/<task_id>/   → marcar tarea completada o pendiente (body: {"completed": true})  
- DELETE /lists/<id>/tasks/<task_id>/   → borrar tarea  

Todo devuelve JSON y usa los códigos de estado correctos (201 para crear, 204 para borrar, 404 si no existe, etc.).

## Notas 
- He usado Django estándar sin instalar Django REST Framework
- Las fechas se devuelven en formato ISO para que se lean bien en JSON
- El código está organizado en vistas por función y con manejo básico de errores

He probado todo con Thunder Client y funciona como pide el enunciado.

Hecho por Keitor Vásquez Morán 
2º DAW - febrero 2026
