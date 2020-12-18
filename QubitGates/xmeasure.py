from qiskit import Aer, execute, QuantumCircuit
from math import sqrt, pi
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt

def x_measure(qc, qubit, cbit):
    qc.h(qubit)
    qc.measure(qubit, cbit)
    qc.h(qubit)
    return qc

state = [1, 0]
qc = QuantumCircuit(1, 1)
qc.initialize(state, 0)
x_measure(qc, 0, 0)
print(qc)

backend = Aer.get_backend('statevector_simulator')
result = execute(qc, backend).result()
out = result.get_statevector()
plot_bloch_multivector(out)

plt.show()