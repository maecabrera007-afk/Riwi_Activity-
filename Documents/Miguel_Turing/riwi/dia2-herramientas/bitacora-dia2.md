# Bitácora · Día 2 · Herramientas de desarrollo

- **Coder: Miguel Angel Echavarria Cabrera **
- **Fecha: 14/10/2026 **
- **TL: **

---

## 1. Mi entorno de desarrollo (Etapa 1)

- Versión de Ubuntu: Ubuntu 26.04.1 LTS
- Versión de Python: Python 3.14.4
- ¿Dónde está instalado Python? (resultado de `which python3`): Esta instalado urs/bin/python3
- Con mis palabras, la diferencia entre un compilador y un intérprete es: un compilador se encarga de traducir el codigo y ya ponerlo dentro de un archivo para ejecutarlo a diferencia del interprete aparte de traducirlo lo va ejecutando inmediatamente linea a linea
- ¿Qué pasó con la línea 4 de `hola.py` y por qué?: No se esjecuto como texto porque no estaba dentro de las " " ,la terminal dio el error mostrando la ruta y exactamente subrrayado en rojo  donde esta el error 


| Herramienta | ¿Qué es? (sistema operativo, editor, intérprete, compilador o navegador) |
|---|---|
| Ubuntu | Sistemas operatios|
| VS Code | editor  |
| Python |  inerpretes  |
| Chrome | Navegadores |
| gcc |  Compiladores |

## 2. Reinstalación de VS Code (Etapa 2)

- ¿Cómo estaba instalado VS Code? (snap, .deb o no estaba): Estaba instalado con el comando snap 
- Comando que usé para desinstalarlo: sudo snap remove code
- Comando que usé para instalarlo:  sudo apt install ./code_*.deb
- ¿Por qué es importante instalar desde la fuente oficial?: Porque si se instala desde otra fuentes puede tener sofware malicioso y contaminar el dispositivo 
- ¿Qué pasó con mi configuración al desinstalar? ¿Dónde vive?: la configuracion se mantiene y vive en la ruta  ls ~/.vscode

## 3. Perfiles y extensiones (Etapa 3)

- Con mis palabras, un perfil de VS Code es: Una cofiguracion personalizada de cada persona en el mismo editor 
- ¿Qué cambia en el Explorador entre un perfil y otro?: cambia la manera en la que se ven y esta organizado tu editor y tu proyecto 
- ¿Por qué VS Code pregunta si confío en el publicador de una extensión?:Pregunta por temas de seguridad ya que estas pueden manipular cosas dentro de tu proyecto o dispositivo. 

## 4. Duelo de perfiles (Etapa 4)

| Prueba | Perfil2-Basico | Perfil1-Pro |
|---|---|---|
| 1. Auto guardado |si |no |
| 2. Auto Rename Tag |si |no|
| 3. Error Lens |General|Especifico|
| 4. Íconos |Originales de VSC | Mas grandes y representativos al tipode archivo |
| 5. Guías de indentación | las normales casi inperseptibles|Con mayor visibilidad |
| 6. Extensiones corriendo | Mas rapido |Mas lento  |

**Reflexión**

1. ¿Noté diferencias en la experiencia de trabajo entre los dos perfiles? ¿Cuáles?
   - Se ahorra mucho tiempo utilizando las extenciones y cambiando la configuracion todo el proceso se vuelve mas intuitivo y fluido 
2. ¿Qué ventajas tiene usar múltiples perfiles en VS Code?
   - Si varias personas trabajan en el mismo pc cada una puede tener las configuraciones que mas le favoresca a su rendimiento o tambien dependiendo del tipo de proyecto en el cual este trabajando 
3. ¿Cómo influyen las extensiones en la productividad y en el rendimiento del editor?
   -Como ya mencione te da ciertos atajos que te ayudan a mejorar el rendimiento 
4. ¿Cuándo sería útil usar perfiles distintos en un entorno profesional? (dos ejemplos)
   - Cuando varias personas usan el mimso dispositivo
   - Cuando se trabaja con diferentes arquitecturas o tipos de proyectos 

## 5. Inspección y modificación (Etapa 5)

- Página que usé: https://es.wikipedia.org/wiki/Medell%C3%ADn
- Cinco etiquetas que encontré y para qué sirven:
  1. animation : añadir animaciones a los objetos ya sea , fuentes , imagnes fondos etc
  2. background-position:Posicion del fondo con respecto a eje x ,y 
  3. image-orientation : posicion de la pagina en el eje x , y
  4. resize : Para ajustar el metodo de algo respecto a toda la pagina
  5. font_weight : este sirve para controlar el tamaño de la negrilla de la  fuente
- ¿Qué pasó con mis cambios al recargar y por qué?: porque los cambios que estamos haciendo son solo de vista mas no editando el documento en realidad
- Con mis palabras, el DOM es: DOM es como un borrador en el cual podemos hacer cambios para pruebas sin modificar directamente al archivo original 

## 6. La consola (Etapa 6)

| Operación | Mi predicción | Resultado real |
|---|---|---|
| `2 + 3` | 5|5 |
| `10 - 4 * 2` |12 | 2|
| `(10 - 4) * 2` | 12|12 |
| `10 / 4` |2.5 |2.5 |
| `10 % 3` |1 | 1|
| `2 ** 8` |256 |256 |
| `120000 * 0.19` |280 |22800 |
| `365 * 24` | 8760|8760 |

- ¿Por qué `0.1 + 0.2` no da exactamente `0.3`?: los computadores guardan los numeros en binarios y algunos decimales como el 0.1 no se guardan de forma exacta 
- Errores o advertencias que encontré en la página (o "ninguno"): An aria-labelledby attribute doesn’t match any element id. This might stop the browser from correctly autofilling the form and accessibility tools from working correctly.

- Diferencia entre un error y una advertencia: Un error detiene todo el proceso y no deja ejecutar lo que escribiste a diferencia de las advertencias que te avisan de que algo no esta del todo bien o que posiblemente pueda fallar si sigues escribiendo o editando 

## 7. La red / Network (Etapa 7)

| Imagen | Formato | Tamaño | Tiempo | Código de estado |
|---|---|---|---|---|
|smart-take_endframe__fzy3ygxinq2y_small.jpg|jpeg|66.6kB |177ms | 200|
|siri__bklrx9fgx0pe_small.jpg |jpeg |42.8kB |61ms |200 |
|tent__68ysumotbs2m_small.jpg |jpeg |28.8kB | 410ms|200 |

| Experimento | Solicitudes | Transferido | Load |
|---|---|---|---|
| A. Sin caché | 55|3.3MB |1.70s |
| B. Con caché | 55|542kB |869ms |
| C. Red lenta | 24/55|928/3316 kB |19.32s |

- Archivo más pesado de la página y su tipo: ca-analytics.js type :Script
- ¿Por qué la página cargó más rápido con caché?: porque ya son archivos que estan cargados y no se le teiene que volver a pedir a servidor dandole prioridad a los que no mejorando el tiempo de carga 
- ¿Por qué un desarrollador querría probar con una red lenta?: La pagina tiene que ser provada en todo los ecenarios posibles para poder entregar un producto de calidad y aseguarse de que funciones de manera efectiva 
- ¿Qué haría para que una imagen pesada cargue más rápido?:yo la guardaria en la cache para que la proxima vez que se recargue no tenga 

## 8. Dispositivos móviles (Etapa 8)

| Ancho (px) | Dispositivo | ¿Cambia el menú? | ¿Imágenes bien? | ¿Scroll horizontal? | Observación |
|---|---|---|---|---|---|
| 320 |Responsive | si|si|si |Las imagenes y general la estructura de la pagina se mantiene intuitiva y organizada|
| 375 |Responsive|si |si |si | Todo se mantiene de la misma manera lo unico que cambia es la distribucion de el texto|
| 768 |Responsive |si |si|si|Mantiene el scroll horizontal porque asi estan organizadas las imagenes por defecto en la pagina no a causa del formato  |
| 1024 |Responsive|no |si |si | Al volverse mas grande las imagenes y todos los elementos dentro de la pagina se organizan en el centro de manera efectiva |
| 1440 |Responsive |no |si | si|La pagina ya tiene suficiente espacio trata de organizar todo de manera que no queden espacios blancos grandes |

- ¿Por qué es importante probar varias resoluciones antes de entregar un proyecto?: Ya que no sabemos en que dispositivo se va a ver nuestra pagina y la variedad de tipos y tamaños que hay es indispensable probar en diferentes resoluciones para asegurarnos que no hay errores

## 9. Laboratorio de errores (Etapa 9)

| # | Tipo | ¿Dónde lo detecté? | Mensaje o síntoma | Causa | Solución aplicada |
|---|---|---|---|---|---|
| 1 |Error de escritura| En el contador de visitas|No se suma ningun valor al contador|Estaba mal escrito el nombreCode |Se corrigio el nombre como se definio arriba  |
| 2 | reading 'addEventListener')"|El el html|el boton no hacia lo que se suponia que hiciera  y el console.log no se ejecutaba|etaban definidoscon diferente nombre en el js y en el html |se modifico para que los nombres coincidieran |
| 3 | | | | | |
| 4 | | | | | |

- Uno de los errores, descrito con detalle, y cómo lo resolví:
- ¿Qué vi al pausar con el breakpoint?:
- ¿Qué pasó al cambiar `visitas` por 99 y al borrarlo?:
- ¿Para qué usan el localStorage las páginas reales? ¿Qué NO debería guardar ahí?:
- Ancho exacto en el que se apilan las tarjetas y regla de CSS responsable:
- ¿Por qué no basta con mirar solo la consola para encontrar errores?:

## 10. Comparación con Firefox (Etapa 10)

| Herramienta | Chrome: nombre y atajo | Firefox: nombre y atajo | Diferencia que noté |
|---|---|---|---|
| Inspeccionar HTML y CSS | | | |
| Consola | | | |
| Red | | | |
| Simulación de dispositivos | | | |
| Almacenamiento local | | | |
| Mensaje del error que reintroduje | | | |

- Una característica de Firefox interesante o diferente a Chrome (qué es, para qué sirve y cómo la probé):

## 11. Reflexión final (Etapa 11)

- La herramienta que más voy a usar y por qué:
- Lo más difícil del día y cómo lo resolví:
- Las DevTools explicadas para alguien que no programa (3 líneas):