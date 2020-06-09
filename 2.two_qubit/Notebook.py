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

# # Two qubit operations

from qiskit import (QuantumCircuit,
                        QuantumRegister,
                        ClassicalRegister,
                        execute,
                        Aer)
import numpy as np

from qiskit import transpile
qc = QuantumCircuit(1)
qc.initialize([1/np.sqrt(2), 1/np.sqrt(2)], 0)
print(qc)
new_qc = transpile(qc, basis_gates=["cx", "u3"])
print(new_qc)


# + code_folding=[]
def show_result(qc):
    job = execute(qc, backend = Aer.get_backend("statevector_simulator"))
    vec = job.result().get_statevector(qc)
    
    bins = [format(i, '0%db'%np.ceil(np.log2(len(vec)))) for i, _ in enumerate(vec)]
    for i, j in zip(vec, bins):
        print(i, ": |%s>"%str(j))


# -

# ### Q1. Create state 
# $$|\psi_0\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}}$$

q = QuantumRegister(2)
c = ClassicalRegister(2)
qc = QuantumCircuit(q, c)
#  here create circuit
show_result(qc)

# ### Q2. Create state 
# $$|\psi_0\rangle = \frac{|01\rangle + |10\rangle}{\sqrt{2}}$$



# ### Q3. Validate CHSH inequality (A little bit advanced)
# What is CHSH inequality? https://en.wikipedia.org/wiki/CHSH_inequality  
# Briefly, CHSH inequality is a proof of bell's theorem.   
# Usually, CHSH inequality satisfies
# $$|\langle{A, B}\rangle-\langle{a, B}\rangle+\langle{A, b}\rangle + \langle{a, b}\rangle| \leq 2$$  
# in a classical system. However, in a quantum system, this inequality satisfies
# $$2 < |\langle{A, B}\rangle-\langle{a, B}\rangle+\langle{A, b}\rangle + \langle{a, b}\rangle|\leq2\sqrt{2}$$  
# A, B, a, b represent the basis of measurement.

# #### First step (prepare quantum circuit)
# We need two qubits to simulate CHSH inequality.



# #### Second step (prepare bell state)
# Bell state is one of the most important quantum states. There are four types of bell states.
# $$|\psi^{+}\rangle = \frac{|00\rangle+|11\rangle}{\sqrt{2}}$$
# $$|\psi^{-}\rangle = \frac{|00\rangle-|11\rangle}{\sqrt{2}}$$
# $$|\phi^{+}\rangle = \frac{|01\rangle+|10\rangle}{\sqrt{2}}$$
# $$|\phi^{-}\rangle = \frac{|01\rangle-|10\rangle}{\sqrt{2}}$$
# Choose one of them and prepare it on the circuit.



# #### Third step (Measurement basis)
# Prepare four measurement basis.  
# A = Z  
# a = X  
# B = $\frac{Z+X}{\sqrt{2}}$  
# b = $\frac{Z-X}{\sqrt{2}}$  
# In the qiskit, measurement basis is Z if you don't apply any operations.
# To change the measurement basis, you need to apply operations before measurement.  
# Hint: This is the basis of B
# ![Bbasis](./image/Bbasis.png)
# You have to calculate one state with four basis.
# Fill this table.
#
# |Basis\Outcome |$P(|00\rangle)$ | $P(|01\rangle)$ | $P(|10\rangle)$ | $P(|11\rangle)$ |
# |-------------|----------------------|----------------------|----------------------| ----------------------|
# | AB         |                      |                      |                     |                      |
# | aB          |                      |                     |                      |                      |
# | Ab         |                      |                      |                      |                      |
# | ab          |                     |                      |                      |                      |



# #### Final step (Calculate S value)
# Finally, we need to calculate S value.
# If you chose $|\psi^+\rangle$ or  $|\psi^-\rangle$, calculate $$\langle{MN}\rangle =  P(|00\rangle)+P(|11\rangle)-P(|01\rangle)-P(|10\rangle)$$   
# else you chose $|\phi^+\rangle$ or $|\phi^+\rangle$, then you need to  
# $$\langle{MN}\rangle = P(|01\rangle)+P(|10\rangle)-P(|00\rangle)-P(|11\rangle)$$
# for each of basis.
# And $$S = |\langle{AB}\rangle-\langle{aB}\rangle+\langle{Ab}\rangle+\langle{ab}\rangle|$$


