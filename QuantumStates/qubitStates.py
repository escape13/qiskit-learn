from qiskit import execute, Aer, QuantumCircuit
from math import pi, sqrt

# first measurement 

qc = QuantumCircuit(1, 2)
backend = Aer.get_backend('qasm_simulator')
statevector = [1/sqrt(2), 1j/sqrt(2)]
qc.initialize(statevector, 0)
qc.measure(0, 0)
qc.measure(0, 1)
print(qc)
result = execute(qc, backend).result()
counts = result.get_counts()
print(counts)