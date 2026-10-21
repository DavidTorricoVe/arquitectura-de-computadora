# Análisis de Resultados: Comunicación entre Procesos (IPC) en Linux

Este documento presenta la explicación de las capturas de pantalla obtenidas tras ejecutar las pruebas de rendimiento entre un modelo de comunicación No Optimizado (usando Named Pipes) y uno Optimizado (usando Memoria Compartida y Batching).

## 1. Análisis de la Primera Imagen: Versión No Optimizada (Named Pipes)

En la primera prueba ejecutamos `./Cons_NO & ./Prod_NO`. Esta versión transfiere 10 millones de paquetes de 64 bytes utilizando llamadas al sistema tradicionales (`read()` y `write()`) para cada paquete individual.

**Lo que muestran los resultados:**
* **Productor (`Prod_NO`):** Tardó **19.73 segundos** en enviar todos los paquetes, alcanzando una velocidad de transferencia de **30.92 MB/s**.
* **Consumidor (`Cons_NO`):** Sufrió un retraso enorme, tardando **160.47 segundos** (casi 3 minutos) en terminar de leer los datos, con un rendimiento de apenas **3.80 MB/s**.

**Explicación del fenómeno (¿Por qué es tan lento?):**
La lentitud extrema se debe al **"Context Switching" (Cambios de Contexto)**. Al enviar y recibir paquete por paquete, obligamos al procesador a saltar entre el "Modo Usuario" (donde corren nuestros programas) y el "Modo Kernel" (el núcleo del sistema operativo) 20 millones de veces. Este trabajo de intermediación del sistema operativo satura el procesador y genera un cuello de botella terrible, especialmente del lado del consumidor.

---

## 2. Análisis de la Segunda Imagen: Versión Optimizada (Memoria Compartida)

En la segunda prueba ejecutamos `./Prod_OPT & sleep 1 && ./Cons_OPT`. Esta versión utiliza Memoria Compartida POSIX (`mmap`), Semáforos y procesa los datos en bloques de 500 paquetes.

**Lo que muestran los resultados:**
* **Consumidor (`Cons_OPT`):** El tiempo de procesamiento total cayó drásticamente a solo **0.39 segundos**. 
* **Rendimiento:** La velocidad se disparó a más de 25 millones de paquetes por segundo, logrando un ancho de banda de **1559.37 MB/s**.

**Explicación del fenómeno (¿Por qué es tan rápido?):**
La mejora es gigantesca (más de 400 veces más rápido que el consumidor anterior). Esto se logra gracias a dos técnicas:
1. **Zero-Copy (Copia Cero):** Al usar `mmap`, ambos programas (productor y consumidor) comparten exactamente el mismo espacio físico en la memoria RAM. El productor escribe los datos y el consumidor los lee directamente de ahí, sin que el Kernel del sistema operativo tenga que intervenir ni copiar los datos a espacios intermedios.
2. **Batching (Por lotes):** En lugar de que los programas se comuniquen cada vez que envían 1 paquete, agrupan el trabajo y solo se avisan mediante semáforos cada 500 paquetes. Esto reduce drásticamente las interrupciones del CPU.

## Conclusión Final
Las métricas demuestran que para transmitir grandes volúmenes de datos a alta velocidad, las llamadas al sistema (Pipes/FIFO) son ineficientes. El uso de Memoria Compartida (Zero-Copy) es la técnica definitiva para aprovechar el ancho de banda real del hardware.