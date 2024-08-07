# Laboratorio-1-señales
>  Análisis estadístico de la señal 
---
Agosto 2024

## Tabla de contenidos
* [¿Qué se va a realizar?](#introduccion)
* [Señal en Physionet](#señal)
* [Estadisticos descriptivos](#estadisticos)
* [Histogramas](#histograma)
* [Ruido Gaussiano](#ruido1)
* [Ruido Impulso](#ruido2)
* [Ruido Tipo artefcato](#ruido3)
* [Contacto](#contacto)
---
<a name="introduccion"></a> 
## ¿Qué se va a realizar?
Las señales medidas de un entorno real, en este caso, las señales biomédicas están caracterizadas por contener información relevante, como amplitud y 
frecuencia e información que la contamina, denominada ruido.Adicionalmente, existe información que puede describir una señal biomédica a partir de variables estadísticas. Para esta práctica de laboratorio el estudiante deberá descargar una señal fisiológica y calcular los estadísticos que la describen, explicando para qué sirve cada uno.

1. Entrar a bases de datos de señales fisiológicas como physionet, buscar y descargar una señal fisiológica de libre elección. Tenga en cuenta que si por 
algún motivo no puede calcular todos los parámetros solicitados porque la señal es muy corta, deberá descargar una nueva señal.  
2. Importar la señal en python y graficarla. Para esto pueden hacer uso de cualquier compilador, como spyder, google colab, sistema operativo Linux, etc. Se 
recomienda utilizar la librería matplotlib para graficar en python. 
3. Calcular los estadísticos descriptivos de dos maneras diferentes cuando sea posible: la primera vez, programando las formulas desde cero; la segunda vez, 
haciendo uso de las funciones predefinidas de python.  
Los estadísticos que se espera obtener son:
- Media de la señal 
- Desviación estándar
- Coeficiente de variación 
- Histogramas 
- Función de probabilidad
5. Investigar qué es la relación señal ruido (SNR):
- Contaminar la señal con ruido gaussiano y medir el SNR 
- Contaminar la señal con ruido impulso y medir el SNR 
- Contaminar la señal con ruido tipo artefacto y medir el SNR

<a name="Señal"></a> 
## Señal en Physionet
1. Buscar Physionet desde su navegador preferido y seleccionar el boton "DATA".
![Agregar](imagen1.png)
2. Al ingresar en "DATA" van a aparecer todos los archivos de señales que la pagina tiene en su repositorio, para este proyecto el seleccionado fue "Apnea-ECG Database: Seventy ECG signals with expert-labelled apnea annotations and machine-generated QRS annotations".
![Agregar](imagen2.png)
3. Al ingresar a la señal seleccionada podremos evidenciar toda la informacion que nos comunica sobre que se trata la misma.
![Agregar](imagen3.png)
- Descripción de los datos:

Los datos constan de 70 registros, divididos en un conjunto de aprendizaje de 35 registros (a01 a a20, b01 a b05 y c01 a c10) y un conjunto de prueba de 35 registros (x01 a x35), todos los cuales pueden descargarse desde esta página. La duración de los registros varía desde un poco menos de 7 horas hasta casi 10 horas cada uno. Cada registro incluye una señal de ECG digitalizada continua, un conjunto de anotaciones de apnea (derivadas por expertos humanos sobre la base de la respiración registrada simultáneamente y las señales relacionadas) y un conjunto de anotaciones de QRS generadas por máquina (en las que todos los latidos, independientemente del tipo, se han etiquetado como normales). Además, ocho registros (a01 a a04, b01 y c01 a c03) están acompañados por cuatro señales adicionales (Resp C y Resp A, señales de esfuerzo respiratorio torácico y abdominal obtenidas mediante pletismografía de inductancia; Resp N, flujo de aire oronasal medido mediante termistores nasales; y SpO2, saturación de oxígeno).

Se asocian varios archivos con cada registro. Los archivos con nombres de la forma rnn.dat contienen los ECG digitalizados (16 bits por muestra, el byte menos significativo primero en cada par, 100 muestras por segundo, nominalmente 200 unidades A/D por milivoltio). Los archivos .hea son archivos de encabezado (de texto) que especifican los nombres y formatos de los archivos de señal asociados; estos archivos de encabezado son necesarios para el software disponible en este sitio. Los archivos .apn son archivos de anotación (binarios), que contienen una anotación para cada minuto de cada registro que indica la presencia o ausencia de apnea en ese momento; Estos archivos están disponibles únicamente para las 35 grabaciones del conjunto de aprendizaje. Los archivos qrs son archivos de anotación generados por máquina (binarios), realizados con sqrs125, y proporcionados para la conveniencia de aquellos que no desean utilizar sus propios detectores QRS.

Tenga en cuenta que los archivos .qrs no están auditados y contienen errores. Es posible que desee corregir estos errores. De lo contrario, puede utilizar estas anotaciones en forma no corregida si desea investigar métodos de detección de apnea que sean robustos con respecto a pequeñas cantidades de errores de detección de QRS, o puede ignorar estas anotaciones por completo y trabajar directamente a partir de los archivos de señal. Puede encontrar más información sobre los archivos de anotación, incluidas las interpretaciones de los tipos de anotación (códigos) y los detalles de cómo se crearon los archivos .qrs, aquí.
4. Al deslizar hacia abajo en la pagiam podremos encontrar "FILES", alli es donde realizaraemos la descarga de nuestros archivos .hea y .dat, en este caso los que utilizamos son a18.hea y a18.dat.
![Agregar](imagen4.png)
5. Despues de tener descargados los archivos de nuestra señal recuerde que es necesario que estos sean guardados en la misma carpeta en que se guarde nuestro proyecto en python.
![Agregar](imagen5.png)
![Agregar](imagen4.png)
