from qiskit import QuantumCircuit, Aer, execute

qc = QuantumCircuit(4, 2)

qc.x(0)
qc.x(1)
qc.barrier()

qc.cx(0, 2)
qc.cx(1, 2)
qc.ccx(0, 1, 3)
qc.barrier()

qc.measure(2, 0)
qc.measure(3, 1)

counts = execute(qc, Aer.get_backend('qasm_simulator')).result().get_counts()
print(qc)
print(counts)