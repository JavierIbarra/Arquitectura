# Arquitectura de Comutadores

## Proyecto 3
**integrantes:** 
* Javier Ibarra
* Juan Roncagliolo
* Ignacio Mayer

## Editor Assembler
**Requisitos:** 
* tkinter   sudo apt-get install python3-tk

**El programa se separa en tres archivos importantes:**
* assemply.py (logica grafica del programa)
* funciones.py (funciones para detectar errores)
* instrucciones.txt (instrucciones soportadas)

**El programa cuenta con tres textbox:**
* El de la derecha es donde se cargan los archivos con el codigo
* El de arriba a la izquierda muestra el codigo binario del programa
* El de abajo a la izquierda muestra el binario de la memoria inicial del codigo

**Opciones del menu:**
| 		Operacion		| 				Descripcion						|
| 		--			|				--							|
| "Archivos > Guardar como" 		| Genera tres archivo(*.ass,*.data,*.out)						| 
| "Archivos > Cargar"			| Carga el archivo especificado							|
| "Ejecutar > Recalcular Errores" 	| Muestra los errores del codigo							|
| "Ejecutar > Assembler" 		| Crea los binarios del codigo y memoria (no guarda los archivos automaticamente)	|
| "Editar > Deshacer" 			| Elimina ultimo cambio realizado							|
| "Editar > Rehacer" 			| Recupera ultimo cambio deshecho							|
| "Editar > Cortar" 			| Corta elemento seleccionado								|
| "Editar > Copiar" 			| Copia elemento seleccionado								|
| "Editar > Pegar" 			| Pega en el texto seleccionado							|
| "Editar > Seleccionar Todo"		| Selecciona todo los elemntos del texto seleccionado				|
| "Ayuda > Ayuda" 			| Informacion de uso									|
| "Ayuda > Acerca de"			| Mustra informacion de versiones 							|
