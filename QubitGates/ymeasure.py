from qiskit import Aer, execute, QuantumCircuit
from math import sqrt, pi
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt

def y_measure(qc, qubit, cbit):
    qc.sdg(qubit)
    qc.h(qubit)
    qc.measure(qubit, cbit)
    qc.h(qubit)
    qc.s(qubit)
    return qc

qc = QuantumCircuit(1, 1)
state = [1, 0]
qc.initialize(state, 0)

y_measure(qc, 0, 0)

backend = Aer.get_backend('statevector_simulator')
result = execute(qc, backend).result()
out, counts = result.get_statevector(), result.get_counts()
plot_bloch_multivector(out)
print(counts)

plt.show()