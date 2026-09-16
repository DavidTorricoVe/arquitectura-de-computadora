#include <iostream>
#include <vector>
#include <cmath>
#include <time.h>
#include <stdio.h>

double medir_tiempo_segundos() {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return (double)ts.tv_sec + (double)ts.tv_nsec / 1e9;
}



void filtrar_lento(std::vector<float> datos, std::vector<float>& resultado) {
    for (size_t i = 0; i < datos.size(); i++) {
        float limite = sqrt(250000.0f) * 2.5f; 
        if (datos[i] > limite) {
            resultado.push_back(datos[i]);
        }
    }
}



int main() {
    int N = 30000000; 
    std::vector<float> datos(N, 1500.0f);
    std::vector<float> res_lento;
    std::vector<float> res_opt;

    double t0, t_lento, t_opt;

    t0 = medir_tiempo_segundos(); 
    filtrar_lento(datos, res_lento); 
    t_lento = medir_tiempo_segundos() - t0;


    printf("\n=== METRICAS DE REFACTORIZACION (N=%d) ===\n", N);
    printf("1. Sin Optimizar (Copia + Loop Ineficiente) : %7.4f s | Speedup: 1.00x\n", t_lento);
    printf("========================================================\n\n");

    return 0;
}