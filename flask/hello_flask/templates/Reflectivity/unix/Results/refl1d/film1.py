from refl1d.names import *

nickel = Material('Ni')
iron = Material('Fe')

#nickel = SLD(rho=9.4)

sample = silicon(0,5) | nickel(100,5) | iron (1,100) | air
sample = silicon(0,5) | nickel(100,5000) | air

T = numpy.linspace(0, 5, 100)

probe = NeutronProbe(T=T, dT=0.01, L=4.75, dL=0.0475)

M = Experiment(probe=probe, sample=sample)

M.simulate_data(5)

problem = FitProblem(M)
