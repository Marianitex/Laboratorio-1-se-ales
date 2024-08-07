# Importar paquetes necesarios
import wfdb  # Para leer "records" de PhysioNet
import matplotlib.pyplot as plt  # Para graficar los datos
import numpy as np  # Para cálculos numéricos
import math  # Para cálculos matemáticos
from scipy.stats import variation  # Para calcular el coeficiente de variación
import seaborn as sns
# Mensaje de bienvenida
print("Bienvenido a la práctica de lab #1 de señales, hecho por Mariana Higuera y Deysi Gomez :D")

# Cargar la información desde los archivos .dat y .hea
# Esto carga un record de ECG de PhysioNet con las señales asociadas
signal = wfdb.rdrecord('a18')

# Obtener los valores de la señal
valores = signal.p_signal  # p_signal es un array numpy con las señales
valoresreducido = valores.flatten()[:500]  # Reducir a las primeras 500 muestras para algunas gráficas
valoresreducido2 = valores.flatten()[:100]  # Reducir aún más para otras gráficas

# Obtener el número de muestras
tamano = signal.sig_len  # sig_len es la longitud de la señal

# Contaminación con ruido gaussiano
N = 500  # Número de muestras a simular, se puede elegir cualquier número
sumatoriavalores = 0.0  # Inicializar la sumatoria de los valores de la señal

# Calcular la potencia de la señal
for a in valores:
    sumatoriavalores += (a)**2  # Sumar el cuadrado de cada valor para obtener la potencia
potenciasenal = sumatoriavalores / tamano  # Dividir por el número de muestras para obtener la potencia promedio

# Definir función para calcular valores estadísticos
def valores_estadisticos():
    print("Tamaño del vector de la señal:", tamano)
    print("Valores de la matriz", valores)

    # MEDIA CON CÁLCULOS A MANO
    suma_vector = sum(valores)  # Sumar todos los valores de la señal
    media = suma_vector / tamano  # Calcular la media dividiendo por el número de muestras
    print('Media manual:', media)

    # MEDIA CON FUNCIONES DE PYTHON
    media_python = np.mean(valores)  # Usar numpy para calcular la media
    print('Media con python:', media_python)

    # DESVIACIÓN ESTÁNDAR A MANO
    sumatoria = 0.0  # Inicializar la sumatoria para la desviación estándar
    for valor in valores:
        sumatoria += (valor - media) ** 2  # Sumar el cuadrado de la diferencia de cada valor con la media
    varianza = sumatoria / tamano  # Calcular la varianza dividiendo por el número de muestras
    desviacion = math.sqrt(varianza)  # Calcular la desviación estándar tomando la raíz cuadrada de la varianza
    print('Desviación estándar manual:', desviacion)

    # DESVIACIÓN ESTÁNDAR CON FUNCIONES DE PYTHON
    desviacion_python = np.std(valores, ddof=1)  # Usar numpy para calcular la desviación estándar (ddof=1 para muestras)
    print('Desviación estándar con python:', desviacion_python)

    # COEFICIENTE DE VARIACIÓN A MANO
    coeficiente = (desviacion / media) * 100  # Calcular el coeficiente de variación como la desviación estándar dividida por la media
    print('Coeficiente de variación manual:', coeficiente, '%')

    # COEFICIENTE DE VARIACIÓN CON FUNCIONES DE PYTHON
    coeficiente_variacion = variation(valores) * 100  # Usar scipy.stats para calcular el coeficiente de variación
    print('Coeficiente de variación con python:', coeficiente_variacion, '%')

# Definir función para graficar la señal original
def señal():   
    plt.plot(valores, color='blue')  # Graficar los valores de la señal en azul
    plt.title('Gráfica de los valores de la señal')  # Título de la gráfica
    plt.xlabel('Muestras(ms)')  # Etiqueta del eje x
    plt.ylabel('Amplitud(mV)')  # Etiqueta del eje y
    plt.xlim(0, 500)  # Limitar el eje x para mostrar solo las primeras 500 muestras
    plt.ylim(-4, 4)  # Limitar el eje y para que todas las gráficas tengan la misma escala
    plt.show()  # Mostrar la gráfica
    print("POTENCIA SEÑAL ELEGIDA", potenciasenal)  # Imprimir la potencia de la señal

# Definir función para graficar el histograma de los datos
def histograma():
    
    min_valor = min(valoresreducido)  # Encontrar el valor mínimo en los datos reducidos
    max_valor = max(valoresreducido)  # Encontrar el valor máximo en los datos reducidos
    numero_intervalos = int(np.ceil(np.log2(N) + 1))  # Calcular el número de intervalos usando la regla de Sturges
    ancho_intervalo = (max_valor - min_valor) / numero_intervalos  # Calcular el ancho de cada intervalo
    intervalos = [min_valor + i * ancho_intervalo for i in range(numero_intervalos + 1)]  # Crear una lista de intervalos
    frecuencias = [0] * numero_intervalos  # Inicializar las frecuencias en 0
    # Calcular las frecuencias para cada intervalo
    for valor3 in valoresreducido:
        for i in range(numero_intervalos):
            if intervalos[i] <= valor3 < intervalos[i + 1]:
                frecuencias[i] += 1  # Incrementar la frecuencia correspondiente
                break
        if valor3 == max_valor:
            frecuencias[-1] += 1  # Ajustar la última frecuencia para incluir el valor máximo

    menu = 0
    while menu!=3:
        print("1. Histograma a mano\n2. Histograma funciónes de python\n3. Volver")
        menu = int(input("Elige una opción:"))
        if menu ==1:
            plt.bar(intervalos[:-1], frecuencias, width=ancho_intervalo,color='green', edgecolor='black', align='edge')  # Crear el histograma
            plt.title('Histograma de datos - hecho a mano')  # Título de la gráfica
            plt.xlabel('Intervalos(S)')  # Etiqueta del eje x
            plt.ylabel('Frecuencia(Hz)')  # Etiqueta del eje y
            plt.xticks(intervalos)  # Establecer los ticks en los intervalos
            plt.ylim(0, max(frecuencias) + 1)  # Ajustar el límite del eje y para asegurar que todas las gráficas tengan la misma escala
            plt.show()  # Mostrar el histograma
        if menu ==2:
            ax = sns.distplot(valoresreducido,
                  kde = True,            
                  bins=numero_intervalos,
                  color='red',
                  hist_kws={"linewidth": 200,'alpha':1})
            ax.set(xlabel='Normal Distribution', ylabel='Frequency')
            plt.title('Histograma de datos con plt.hist')
            plt.xlabel('Intervalos(S)')
            plt.ylabel('Frecuencia(Hz)')
            plt.grid(axis='y', alpha=0.75)
            plt.show()
        if menu == 3:
            break  # Salir del menú
        if menu > 3 or menu < 1:
            print("Opción inválida") 
# Definir función para agregar ruido gaussiano y graficar
def ruido_gaussiano():
    ruidogaussiano = np.random.randn(N)  # Generar ruido gaussiano (distribución normal estándar)
    ruido1normalizado = ((ruidogaussiano * 0.3) / 4)  # Normalizar el ruido
    snrneg = 10.0 * np.log10(potenciasenal / np.var(ruidogaussiano))  # Calcular el SNR para el ruido sin normalizar
    snrpos = 10.0 * np.log10(potenciasenal / np.var(ruido1normalizado))  # Calcular el SNR para el ruido normalizado

    menu = 0
    while menu != 5:
        # Mostrar el menú de opciones
        print("1. Ruido sin normalizar\n2. Ruido normalizado\n3. Señal + ruido normalizado\n4. Señal + ruido sin normalizar\n5. Volver")
        menu = int(input("Elige una opción:"))
        if menu == 1:
            plt.plot(ruidogaussiano, color='red')  # Graficar ruido gaussiano sin normalizar
            plt.title("Ruido Gaussiano Sin Normalizar")  # Título de la gráfica
            plt.xlabel('Muestras(ms)')  # Etiqueta del eje x
            plt.ylabel('Amplitud(mV)')  # Etiqueta del eje y
            plt.xlim(0, 500)  # Limitar el eje x
            plt.ylim(-4, 4)  # Limitar el eje y
            plt.show()  # Mostrar la gráfica
        if menu == 2:
            plt.plot(ruido1normalizado, color='orange')  # Graficar ruido gaussiano normalizado
            plt.title("Ruido Gaussiano Normalizado")  # Título de la gráfica
            plt.xlabel('Muestras(ms)')  # Etiqueta del eje x
            plt.ylabel('Amplitud(mV)')  # Etiqueta del eje y
            plt.xlim(0, 500)  # Limitar el eje x
            plt.ylim(-4, 4)  # Limitar el eje y
            plt.show()  # Mostrar la gráfica
        if menu == 3:
            senal_ruido1normal = valoresreducido + ruido1normalizado  # Sumar la señal original con el ruido normalizado
            plt.plot(senal_ruido1normal, color='purple')  # Graficar la señal con ruido normalizado
            plt.xlabel('Muestras(ms)')  # Etiqueta del eje x
            plt.ylabel('Amplitud(mV)')  # Etiqueta del eje y
            plt.title("Señal + Ruido Gaussiano Normalizado")  # Título de la gráfica
            plt.xlim(0, 500)  # Limitar el eje x
            plt.ylim(-4, 4)  # Limitar el eje y
            plt.show()  # Mostrar la gráfica
            print("SNR positivo:", snrpos)  # Imprimir el SNR para el ruido normalizado
        if menu == 4:
            senal_ruidogauss = valoresreducido + ruidogaussiano  # Sumar la señal original con el ruido sin normalizar
            plt.plot(senal_ruidogauss, color='brown')  # Graficar la señal con ruido sin normalizar
            plt.xlabel('Muestras(ms)')  # Etiqueta del eje x
            plt.ylabel('Amplitud(mV)')  # Etiqueta del eje y
            plt.title("Señal + Ruido Gaussiano Sin Normalizar")  # Título de la gráfica
            plt.xlim(0, 500)  # Limitar el eje x
            plt.ylim(-4, 4)  # Limitar el eje y
            plt.show()  # Mostrar la gráfica
            print("SNR negativo:", snrneg)  # Imprimir el SNR para el ruido sin normalizar
        if menu == 5:
            break  # Salir del menú
        if menu > 5 or menu < 1:
            print("Opción inválida")  # Manejar opciones inválidas

# Definir función para agregar ruido de impulso y graficar
def ruido_impulso():
    n = np.linspace(0, 30, 500)
    ruidoimpulso = np.abs(np.random.randn(N))
    ruido2normalizado = (ruidoimpulso * 0.3 / 4)
    señalsumada3 = ruido2normalizado + valoresreducido
    snrneg2 = 10.0 * np.log10(potenciasenal / np.var(ruidoimpulso))
    snrpos2 = 10.0 * np.log10(potenciasenal / np.var(ruido2normalizado))
    menu = 0
    while menu != 5:
        print("1. Ruido sin normalizar\n2. Ruido normalizado\n3. Señal + ruido normalizado\n4. Señal + ruido sin normalizar\n5. Volver")
        menu = int(input("Elige una opción:"))
        if menu == 1:
            plt.xlabel('Muestras(ms)')  # Etiqueta del eje x
            plt.ylabel('Amplitud(mV)')  # Etiqueta del eje y
            plt.stem(n, ruidoimpulso, linefmt='C0-', markerfmt='C0o', basefmt='C0-')
            plt.title("Ruido de Impulso Sin Normalizar")
            plt.xlim(0, 30)
            plt.ylim(-4, 4)
            plt.show()
        if menu == 2:
            plt.xlabel('Muestras(ms)')  # Etiqueta del eje x
            plt.ylabel('Amplitud(mV)')  # Etiqueta del eje y
            plt.plot(ruido2normalizado, color='cyan')
            plt.title("Ruido de Impulso Normalizado")
            plt.xlim(0, 500)
            plt.ylim(-4, 4)
            plt.show()
        if menu == 3:
            plt.xlabel('Muestras(ms)')  # Etiqueta del eje x
            plt.ylabel('Amplitud(mV)')  # Etiqueta del eje y
            plt.plot(señalsumada3, color='magenta')
            plt.title("Señal + Ruido de Impulso Normalizado")
            plt.xlim(0, 500)
            plt.ylim(-4, 4)
            plt.show()
            print("SNR 2 positivo:", snrpos2)
        if menu == 4:
            plt.xlabel('Muestras(ms)')  # Etiqueta del eje x
            plt.ylabel('Amplitud(mV)')  # Etiqueta del eje y
            señalsumada2 = ruidoimpulso + valoresreducido
            plt.plot(señalsumada2, color='lime')
            plt.title("Señal + Ruido de Impulso Sin Normalizar")  # Título de la gráfica
            plt.xlim(0, 500)  # Limitar el eje x
            plt.ylim(-4, 4)  # Limitar el eje y
            plt.show()  # Mostrar la gráfica
            print("SNR 2 negativo:", snrneg2)
        if menu == 5:
            break  # Salir del menú
        if menu > 5 or menu < 1:
            print("Opción inválida")  # Manejar opciones inválidas
def ruido_artefacto():
    print("¿Qué tipo de señal deseas ver?")
    
    # Generar ruido tipo artefacto
    num_artefactos = 100  # Número de artefactos a añadir
    amplitud_artefacto = 0.5  # Amplitud fija para cada artefacto
    indices_artefactos = np.random.randint(0, len(valoresreducido2), num_artefactos)  # Posiciones aleatorias de los artefactos
    artefactos = np.zeros_like(valoresreducido2)  # Crear un vector de ceros con la misma longitud que valoresreducido2
    artefactos[indices_artefactos] = amplitud_artefacto  # Colocar artefactos con la amplitud especificada en las posiciones aleatorias

    # Sumar la señal de artefactos a la señal original
    suma3 = valoresreducido2 + artefactos

    # Calcular la potencia del ruido tipo artefacto
    sumatoriaarte = 0.0
    for i in artefactos:    
        sumatoriaarte += (i)**2
    potenciaartefacto = sumatoriaarte / num_artefactos

    # Normalizar la señal de artefactos
    ruido3normalizado = (artefactos * 0.3) / 4
    sumatoriaarte2 = 0.0
    for i in ruido3normalizado:    
        sumatoriaarte2 += (i)**2
    potenciaartefactonormalizado = sumatoriaarte2 / num_artefactos

    # Sumar la señal original con la señal de artefactos normalizada
    señalsumada4 = ruido3normalizado + valoresreducido2

    # Calcular la relación señal-ruido (SNR)
    snrneg3 = 10.0 * np.log10(potenciasenal / potenciaartefacto)
    snrpos3 = 10.0 * np.log10(potenciasenal / potenciaartefactonormalizado)

    # Menú para seleccionar la visualización de los diferentes tipos de ruido
    menu = 0
    while menu != 5:
        print("1. Ruido sin normalizar\n2. Ruido normalizado\n3. Señal + ruido normalizado\n4. Señal + ruido sin normalizar\n5. Volver")
        menu = int(input("Elige una opción:"))
        
        if menu == 1:
            # Graficar la señal con artefactos sin normalizar
            plt.plot(artefactos, label="Ruido sin normalizar", color='red')
            plt.xlabel('Muestras(ms)')  # Etiqueta del eje x
            plt.ylabel('Amplitud(mV)')  # Etiqueta del eje y
            plt.legend()
            plt.show()
            
        elif menu == 2:
            # Graficar la señal de artefactos normalizada
            plt.plot(ruido3normalizado, label="Ruido normalizado", color='green')
            plt.xlabel('Muestras(ms)')  # Etiqueta del eje x
            plt.ylabel('Amplitud(mV)')  # Etiqueta del eje y
            plt.xlim(0, 100)
            plt.ylim(-0.4, 1)
            plt.legend()
            plt.show()
            
        elif menu == 3:
            # Graficar la señal original con artefactos normalizados añadidos
            plt.plot(señalsumada4, label="Señal + Ruido normalizado", color='blue')
            plt.xlabel('Muestras(ms)')  # Etiqueta del eje x
            plt.ylabel('Amplitud(mV)')  # Etiqueta del eje y
            plt.legend()
            plt.show()
            print("SNR positivo:", snrpos3)
            
        elif menu == 4:
            # Graficar la señal original con artefactos sin normalizar añadidos
            plt.plot(suma3, label="Señal + Ruido sin normalizar", color='orange')
            plt.xlabel('Muestras(ms)')  # Etiqueta del eje x
            plt.ylabel('Amplitud(mV)')  # Etiqueta del eje y
            plt.legend()
            plt.show()
            print("SNR negativo:", snrneg3)
            
        elif menu == 5:
            break  # Salir del menú

        else:
            print("Opción inválida")  # Mensaje de error para opciones fuera del rango

# Menú principal para seleccionar las opciones
opcion = 0
while opcion != 7:
    print("Seleccione una opción:\n1. Mostrar la señal original\n2. Mostrar estadísticas\n3. Mostrar histograma\n4. Añadir ruido gaussiano\n5. Añadir ruido de impulso\n6. Añadir ruido artefacto. \n7.Salir")
    opcion = int(input("Opción: "))
    if opcion == 1:
        señal()  # Llama a la función para graficar la señal original
    elif opcion == 2:
        valores_estadisticos()  # Llama a la función para mostrar estadísticas
    elif opcion == 3:
        histograma()  # Llama a la función para mostrar el histograma
    elif opcion == 4:
        ruido_gaussiano()  # Llama a la función para añadir ruido gaussiano
    elif opcion == 5:
        ruido_impulso()  # Llama a la función para añadir ruido de impulso
    elif opcion == 6:
            ruido_artefacto()
    elif opcion == 7:
        print("Saliendo...")  # Imprime un mensaje de salida
        break  # Rompe el bucle y termina el programa
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 6.")  # Maneja opciones inválidas

