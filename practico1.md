Práctica: Sistemas Numéricos y Aritmética Binaria

Nivel 1 — Conversión de bases (fundamentos)
1.1 Convierte los siguientes números decimales a binario: 45, 128, 255, 1000
45.- 101101
128.- 10000000
255.- 11111111
1000.- 1111101000

1.2 Convierte los siguientes números binarios a decimal: 1011, 10110110, 11111111, 100000000
1011.- 11
10110110.- 182
11111111.- 255
100000000.- 128

1.3 Convierte a hexadecimal los siguientes números binarios: 10101100, 111100001111, 1010101010101010
10101100.- AC
111100001111.- FOF
1010101010101010.- AAAA

1.4 Convierte de octal a decimal: 17, 254, 777
17.- 15
254.- 172
777.- 511

Nivel 2 — Aritmética binaria básica
2.1 Realiza las siguientes sumas binarias (muestra el acarreo): 
1011 + 0110:  10001
11101 + 01011:  101000   

2.2 Realiza las siguientes restas binarias usando préstamo (borrow): 
1100 - 0101: 0111 
10000 - 00111: 01001

2.3 Multiplica en binario: 
1011 × 0101: 110111

Nivel 3 — Complemento a dos
3.1 Representa los siguientes números decimales en complemento a dos usando 8 bits: 
-45.- 1101 0011
-1.- 0000 0001
-128.- 1000 0000
27.- 1110 0101

3.2 Dado el número en complemento a dos de 8 bits 11010110, indica su valor decimal.
-42

3.3 Realiza la resta 45 - 60 usando complemento a dos con registros de 8 bits, y verifica el resultado.
45  = 00101101
-60 = 11000100
00101101 + 11000100: 11110001

Nivel 4 — Desbordamiento (overflow) y banderas
4.1 Determina si ocurre overflow al sumar, en complemento a dos de 8 bits:
01111111 + 00000001: si hay overflow(127 + 1 = 128 que está fuera de rango positivo)
10000000 + 11111111: si hay overflow(-128 + -1 = -129 que está fuera de rango negativo)

4.2 Explica, con tus propias palabras, la diferencia entre carry (acarreo) y overflow en una suma con signo, y da un ejemplo de cada caso usando registros de 4 bits.
El carry es el bit que sobra al sumar en aritmética sin signo. Indica que el resultado no cabe en el número de bits disponible, sin importar el signo.
El overflow aplica a la aritmética con signo (complemento a 2) y ocurre cuando el resultado se sale del rango representable


Nivel 5 — Punto flotante (IEEE 754)
5.1 Representa el número decimal 10.25 en formato IEEE 754 de precisión simple (32 bits), mostrando signo, exponente y mantisa por separado.
Signo: 0
Exponente: 3+127 = 130 = 10000010
Mantisa (23 bits): 01001000000000000000000

5.2 Dado el patrón de bits IEEE 754 de 32 bits 1 10000010 01100000000000000000000, calcula su valor decimal.

5.3 Explica qué es la pérdida de precisión en punto flotante y demuéstralo con un ejemplo numérico (por ejemplo, sumar 0.1 + 0.2 en punto flotante)
La pérdida de precisión ocurre porque muchas fracciones decimales no tienen representación binaria finita. Ejemplo: 0.1 + 0.2 en punto flotante da 0.30000000000000004 en vez de 0.3 exacto, porque 0.1 y 0.2 son fracciones periódicas en binario y se almacenan redondeadas a la cantidad finita de bits de la mantisa.


