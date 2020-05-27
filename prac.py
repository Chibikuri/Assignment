from qiskit import *
from qiskit.visualization import *

qc = QuantumCircuit(2)

for quantum in range(2):
    qc.h(quantum)

qc.draw(output='mpl')
