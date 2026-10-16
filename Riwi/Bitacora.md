1 ) Ana dejó de ser cliente activo. Mueve su archivo a clientes/inactivos y agrega una línea indicando el cambio.
| mv cliente_ana.txt .~/Riwi/clientes/inactivos "Estando dentro de la carperta el .txt se utiliza el comando mv para  moverlo y se espesifica a la ruta a la que se va a mover.
2)  La factura 001 fue pagada. Agrega una línea con esa novedad, conservando el historial.
| nano factura_001.txt "Estado actual : Pagado " crl + o ,Enter, ctrl + x "Usando el comando nano te permite editar el contenido del archivo
3 ) El proyecto móvil fue cancelado. Mueve app_domicilios.txt a proyectos/archivados.
| mv app_domicilios.txt  ~/Videos/Riwi/proyectos/archivados/ "Estando dentro de la carpeta  el .txt se utiliza el comando mv para mover el archivo y se tiene que espesificar la ruta a la cual lo quieres mover 
4)Crea en reportes/mensuales un archivo llamado resumen_octubre.txt con cinco líneas que describan los cambios anteriores.
|touch resumen_octubre.txt "Crear el archivo en la carpeta idicara | nano resumen_octubre.txt "se añaden las 5 lineas de los cambios 
5)Copia ese resumen a respaldos y nombra la copia resumen_octubre_respaldo.txt.
| cp resumen_octubre.txt ~/Videos/Riwi/respaldos/ "La misma explicacion para mover archivos de una carpeta a otra |mv resumen_octubre.txt  copia_resumen_octubre.txt " Estando deontro de la carpeta donde esta la copia  se usa el mv pero en este caso se cambia  la ruta por el nombre que le quieras poner al archivo
6)Dentro de reportes/diarios, crea los archivos lunes.txt, martes.txt, miercoles.txt, jueves.txt y viernes.txt
|touch lunes.txt martes.txt miercoles.txt jueves.txt vierenes.txt " Con touch creamos todos los archivos de en un solo comando 
7)Agrega una actividad ficticia a cada archivo.
|nano dia_de_la_semana.txt " en ese caso se ejecuta este comando pero usando el dia de la semana y agragando a cada uno una reporte de tarea ficticia 
8)Crea resumen_semana.txt concatenando los cinco reportes en orden de lunes a viernes. Conserva los archivos originales.
|cat lunes.txt martes.txt miercoles.txt jueves.txt vierenes.txt > ../resumen_semana.txt "Con el cat se pueden unir todos los archivos para crear el resumen nombrando el archivo resultante al final
9)Crea en temporal los archivos demo_01.tmp, demo_02.tmp y demo_03.tmp.
|touch demo_01.tmp demo_02.tmp demo_03.tmp"Para crear los archivos con un solo comando se ponen los nombres separados por espacios
10)Crea también conservar.txt en esa carpeta.
|touch conservar.txt"El comando touch para crear el archivo 
11)Elimina los tres archivos .tmp con una sola ejecución y conserva conservar.txt.
|rm *.tmp " El comando rm sirve para eliminar archivos o carptetas y le puedes especiicar que tipo der archivo deseas eliminar en este caso todos los que tengan la terminacion .tmp
12)Regresa a la raíz de Riwi y presenta el resultado.
|cd.. " Se usa para devolverse a la carpeta inmediatamente anterior en este caso la carpeta Raiz





