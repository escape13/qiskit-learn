from qiskit import Aer, execute, QuantumCircuit
from math import sqrt, pi

def x_measure(qc, qubit, cbit):
    qc.h(qubit)
    qc.measure(qubit, cbit)
    qc.h(qubit)
    return qc

def y_measure(qc, qubit, cbit):
    qc.sdg(qubit)
    qc.h(qubit)
    qc.measure(qubit, cbit)
    qc.h(qubit)
    qc.s(qubit)
    return qc

print()
print("Measuring 3 zero-statevectors: \n")

qc = QuantumCircuit(1, 1)
backend = Aer.get_backend('qasm_simulator')

zero_x = [1/sqrt(2), 1/sqrt(2)]
zero_y = [1/sqrt(2), 1j/sqrt(2)]
zero_z = [1, 0]

# measuring in the z-basis (computational basis)

print("Z-basis:", end="\n\n")

print("Zero_x: ", end='')
qc.initialize(zero_x, 0)
qc.measure(0, 0)
print(execute(qc, backend).result().get_counts())

print("Zero_y: ", end='')
qc.initialize(zero_y, 0)
qc.measure(0, 0)
print(execute(qc, backend).result().get_counts())

print("Zero_z: ", end='')
qc.initialize(zero_z, 0)
qc.measure(0, 0)
print(execute(qc, backend).result().get_counts())

print("\n#########################\n")

print("X-basis: ", end='\n\n')

print("Zero_x: ", end='')
qc.initialize(zero_x, 0)
x_measure(qc, 0, 0)
print(execute(qc, backend).result().get_counts())

print("Zero_y", end='')
qc.initialize(zero_y, 0)
x_measure(qc, 0, 0)
print(execute(qc, backend).result().get_counts())

print("Zero_z", end='')
qc.initialize(zero_z, 0)
x_measure(qc, 0, 0)
print(execute(qc, backend).result().get_counts())

print("\n#########################\n")

print("Y-basis: ", end='\n\n')

print("Zero_x: ", end='')
qc.initialize(zero_x, 0)
y_measure(qc, 0, 0)
print(execute(qc, backend).result().get_counts())

print("Zero_y", end='')
qc.initialize(zero_y, 0)
y_measure(qc, 0, 0)
print(execute(qc, backend).result().get_counts())

print("Zero_z", end='')
qc.initialize(zero_z, 0)
y_measure(qc, 0, 0)
print(execute(qc, backend).result().get_counts())


print()
print(qc)