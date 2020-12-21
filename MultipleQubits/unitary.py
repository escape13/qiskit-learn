from qiskit import Aer, execute, QuantumCircuit

qc = QuantumCircuit(3)
qc.h(0)
qc.z(1)
qc.x(2)

backend = Aer.get_backend('unitary_simulator')
out = execute(qc, backend).result().get_unitary()
print(out)