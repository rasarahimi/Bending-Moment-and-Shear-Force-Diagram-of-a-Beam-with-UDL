import numpy as np
import matplotlib.pyplot as plt

# Inputs (units are in SI)
L = 6
w = 3000
n = 6 * 1000

# Discretization 
x = np.linspace(0, L, n+1)

# Reactions (Supports are simple pin)
RA = w * L / 2
RB = RA
V = RA - w * x
M = RA * x - 0.5 * w * x**2

# Plotting 
fig, (axV, axM,) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

# Shear Force Diagram (linear)
axV.plot(x, V, lw=2, color='crimson')
axV.axhline(0, color='k', lw=2)
axV.axvline(0, color = 'k', lw = 2)
axV.set_ylabel("Shear V [N]")
axV.set_title("Shear Force Diagram (UDL over entire span)")
axV.grid(True)
indexV_max = np.argmax(np.abs(V))
V_max = V[indexV_max]
xV_max = x[indexV_max]

# Bending Moment Diagram (parabolic)
axM.plot(x, M, lw=2, color='navy')
axM.axhline(0, color='k', lw=2)
axM.axvline(0, color = 'k', lw = 2)
axM.set_xlabel("x [m]")
axM.set_ylabel("Moment M [N·m]")
axM.set_title("Bending Moment Diagram")
axM.grid(True)
indexM_max = np.argmax(np.abs(M))
M_max = M[indexM_max]
xM_max = x[indexM_max]
print(f'{V_max} and{xV_max}')
print(f'{M_max} and{xM_max}')


plt.tight_layout()
plt.savefig("udl_sfd_bmd.png", dpi=160)  # optional: export figure
plt.show()

