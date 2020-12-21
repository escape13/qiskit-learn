from qiskit import Aer, execute, QuantumCircuit

qc = QuantumCircuit(2)
qc.h(0)
print(qc)
backend = Aer.get_backend('statevector_simulator')
out_state = execute(qc, backend).result().get_statevector()

print(out_state)

qc.cx(0, 1)
out_state = execute(qc, backend).result().get_statevector()

print(out_state)