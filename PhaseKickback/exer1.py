from qiskit import Aer, execute, QuantumCircuit
from qiskit.visualization import plot_bloch_multivector
from math import pi
import matplotlib.pyplot as plt

qc = QuantumCircuit(2)
qc.h(0)
qc.cu1(pi/4, 0, 1)

backend = Aer.get_backend('statevector_simulator')
out = execute(qc, backend).result().get_statevector()
print(out)
plot_bloch_multivector(out)
plt.show()