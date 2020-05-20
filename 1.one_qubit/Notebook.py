# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # One qubit operations

# Links: https://qiskit.org/textbook/ch-states/single-qubit-gates.html

import numpy as np
from qiskit import QuantumCircuit, Aer, execute
from qiskit.tools.visualization import plot_histogram
# backend
statevector = Aer.get_backend("statevector_simulator")
qasm_simulator = Aer.get_backend("qasm_simulator")

# ## Assignments

# ### Q1. Make quantum state
#
# $$|\psi_1\rangle = \frac{1}{\sqrt{2}}|0\rangle + \frac{1}{\sqrt{2}}|1\rangle$$



# ### Q2. Make quantum state
#
# $$|\psi_2\rangle = \sqrt{\frac{3}{4}}|0\rangle + \frac{1}{\sqrt{4}}|1\rangle$$



# ### Q3. Make quantum state
#
# $$|\psi_3\rangle = \frac{1}{\sqrt{2}}|0\rangle - \frac{1}{\sqrt{2}}|1\rangle$$



# ### Q4. Make quantum state
#
# $$|\psi_4\rangle = \frac{1}{\sqrt{2}}|0\rangle - \frac{\mathcal{i}}{\sqrt{2}}|1\rangle$$



# ### Q5. Visualize state with histogram
#
# $$|\psi_5\rangle = \frac{1}{\sqrt{2}}|0\rangle + \frac{1}{\sqrt{2}}|1\rangle$$



# ### Q6. Draw the circuit of this Quantum state and show result
#
# $$|\psi_6\rangle = HR_z\Big(\frac{\pi}{2}\Big)H|0\rangle$$



# ### Q7. How to represent quantum state with the Broch Sphere?



# ### Q8. How to represent a rotation quantum gate on the Broch Sphere?



# ### Q9. Plot bloch sphere using qiskit
# [Bloch Sphere on qiskit](https://qiskit.org/documentation/stubs/qiskit.visualization.plot_bloch_vector.html)  
# (1) $|0\rangle$  
# (2) $|1\rangle$  
# (3) $|+\rangle$  
# (4) $|-\rangle$  
# (5) $\sqrt{\frac{3}{4}}|0\rangle + \frac{1}{\sqrt{4}}|1\rangle$


