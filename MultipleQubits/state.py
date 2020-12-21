from qiskit import Aer, execute, QuantumCircuit

qc = QuantumCircuit(3)
for qubit in range(3):
    qc.h(qubit)

print(qc)

backend = Aer.get_backend('statevector_simulator')
out = execute(qc, backend).result().get_statevector()
print(out)