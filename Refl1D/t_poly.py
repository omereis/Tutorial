from refl1d.names import *

from copy import copy

# === Materials ===
SiOx = SLD(name="SiOx",rho=3.47)
D_toluene = SLD(name="D-toluene",rho=5.66)
D_initiator = SLD(name="D-initiator",rho=1.5)
D_polystyrene = SLD(name="D-PS",rho=6.2)
H_toluene = SLD(name="H-toluene",rho=0.94)
H_initiator = SLD(name="H-initiator",rho=0)

D_brush = PolymerBrush(polymer=D_polystyrene, solvent=D_toluene, \
                       base_vf=70, base=120, length=80, power=2, \
                       sigma=10)
