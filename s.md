Conversión de decimal a binario
45: 
45/2 = 22 (resto 1),
22/2 = 11 (resto 0), 
11/2 = 5  (resto 1),
5/2 = 2   (resto 1), 
2/2 = 1   (resto 0), 
1/2 = 0   (resto 1) 
          -> 101101
          
128: 
     128/2 = 64 (resto 0), 
      64/2 = 32 (resto 0), 
      32/2 = 16 (resto 0), 
       16/2 = 8 (resto 0), 
        8/2 = 4 (resto 0), 
        4/2 = 2 (resto 0),
        2/2 = 1 (resto 0), 
        1/2 = 0 (resto 1)
              -> 10000000

255: 
255/2 = 127 (resto 1), 
 127/2 = 63 (resto 1), 
  63/2 = 31 (resto 1), 
  31/2 = 15 (resto 1), 
   15/2 = 7 (resto 1), 
    7/2 = 3 (resto 1), 
    3/2 = 1 (resto 1), 
    1/2 = 0 (resto 1) 
        -> 11111111

1000: 
1000/2 = 500 (resto 0), 
 500/2 = 250 (resto 0), 
 250/2 = 125 (resto 0), 
  125/2 = 62 (resto 1), 
   62/2 = 31 (resto 0), 
   31/2 = 15 (resto 1), 
    15/2 = 7 (resto 1), 
     7/2 = 3 (resto 1), 
     3/2 = 1 (resto 1), 
     1/2 = 0 (resto 1) 
         -> 1111101000


Conversión de binario a decimal
1011: 
(1 * 2^3) + (0 * 2^2) + (1 * 2^1) + (1 * 2^0) = 8 + 0 + 2 + 1 -> 11
10110110: 
(1 * 2^7) + (0 * 2^6) + (1 * 2^5) + (1 * 2^4) + (0 * 2^3) + (1 * 2^2) + (1 * 2^1) + (0 * 2^0) = 128 + 0 + 32 + 16 + 0 + 4 + 2 + 0 -> 182
11111111: 
(1 * 2^7) + (1 * 2^6) + (1 * 2^5) + (1 * 2^4) + (1 * 2^3) + (1 * 2^2) + (1 * 2^1) + (1 * 2^0) = 128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 -> 255
100000000:
(1 * 2^8) + (0 * 2^7) + (0 * 2^6) + (0 * 2^5) + (0 * 2^4) + (0 * 2^3) + (0 * 2^2) + (0 * 2^1) + (0 * 2^0) = 256 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 -> 256


10101100: 
Agrupar de 4 bits: 1010 | 1100. 
Bloque 1010 = 8 + 2 = 10 (A en Hex).
Bloque 1100 = 8 + 4 = 12 (C en Hex) -> AC

111100001111: 
Agrupar de 4 bits: 1111 | 0000 | 1111.
Bloque 1111 = 15 (F en Hex). Bloque 0000 = 0 (0 en Hex). 
Bloque 1111 = 15 (F en Hex) -> F0F

1010101010101010: Agrupar de 4 bits: 1010 | 1010 | 1010 | 1010. 
Cada bloque 1010 = 10 (A en Hex) -> AAAA


Conversión de octal a decimal
17: 
(1 * 8^1) + (7 * 8^0) = (1 * 8) + (7 * 1) = 8 + 7 -> 15
254: 
(2 * 8^2) + (5 * 8^1) + (4 * 8^0) = (2 * 64) + (5 * 8) + (4 * 1) = 128 + 40 + 4 -> 172
777: 
(7 * 8^2) + (7 * 8^1) + (7 * 8^0) = (7 * 64) + (7 * 8) + (7 * 1) = 448 + 56 + 7 -> 511


Aritmética binaria básica
Acarreos:  1 1 1 0
             1 0 1 1  (11 decimal)
           + 0 1 1 0  (6 decimal)
           ---------
             1 0 0 0 1  (17 decimal) -> Resultado: 10001

Acarreos: 1 1 1 1 1
            1 1 1 0 1  (29 decimal)
          + 0 1 0 1 1  (11 decimal)
          -----------
          1 0 1 0 0 0  (40 decimal)

Restas Binarias usando Préstamo (Borrow)

Préstamos:   1 10 10
               1  1  0  0  (12 decimal)
             - 0  1  0  1  (5 decimal)
             ------------
               0  1  1  1  (7 decimal)    

Préstamos:   0 1 1 1 10
               1 0 0 0 0  (16 decimal)
             - 0 0 1 1 1  (7 decimal)
             -----------
               0 1 0 0 1  (9 decimal)


Multiplica en binario

       1 0 1 1  (11 decimal)
     x 0 1 0 1  (5 decimal)
     ---------
       1 0 1 1  (Multiplicando x 1)
     0 0 0 0    (Multiplicando x 0, desplazado 1 bit)
   1 0 1 1      (Multiplicando x 1, desplazado 2 bits)
 + 0 0 0 0      (Multiplicando x 0, desplazado 3 bits)
 -------------
   1 1 0 1 1 1  (55 decimal)


Complemento a Dos (8 bits)
Representación de Números en Complemento a Dos 
