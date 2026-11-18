#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reto Práctico 1: Generación del Estado de Bell |Ψ+⟩ = (|01⟩ + |10⟩) / sqrt(2)
Autor: David Rodrigo Torrico Vera
Entorno: Ubuntu 22.04 LTS | Python 3.10+ | Qiskit 1.x + Qiskit Aer
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def main():
    qc = QuantumCircuit(2, 2)

    # 1. Superposición en cúbit 0
    qc.h(0)

    # 2. Compuerta Pauli-X sobre cúbit 1 (invierte |0⟩ -> |1⟩ antes o después de la CNOT)
    qc.x(1)

    # 3. Entrelazamiento mediante CNOT (genera |Ψ+⟩ = (|01⟩ + |10⟩)/√2)
    qc.cx(0, 1)

    # 4. Medición en la base computacional
    qc.measure([0, 1], [0, 1])

    print("CIRCUITO CUÁNTICO (ESTADO DE BELL |Ψ+⟩):")
    print(qc.draw(output="text"))

    backend = AerSimulator()
    shots = 10000
    counts = backend.run(qc, shots=shots).result().get_counts(qc)

    print(f"\nRESULTADOS DE LA MEDICIÓN ({shots} disparos):")
    for bitstring, count in sorted(counts.items()):
        porcentaje = (count / shots) * 100
        print(f"Estado |{bitstring}⟩: {count} ocurrencias ({porcentaje:.2f}%)")

if __name__ == "__main__":
    main()