from refl1d.names import *
from copy import copy
## === Data files ===
#probe = load4('', back_reflectivity=False)
probe = Probe(T=numpy.linspace(0.0022797, 2.2803, 251), L=5.0000)

# Background parameter
probe.background.value = 0.0000
# probe.background.range(1e-9, 1e-5)

## === Stack ===
##
## First, we create a 'material' for each layer, which has an real and imaginary
## scattering length density, stored in a Refl1d object called 'SLD'
sld0 = SLD(name='sld0', rho=2.0690, irho=0.0000)
sld1 = SLD(name='sld1', rho=4.0000, irho=0.0000)
sld2 = SLD(name='sld2', rho=4.0000, irho=0.0000)
sld3 = SLD(name='sld3', rho=4.0000, irho=0.0000)
sld4 = SLD(name='sld4', rho=0.0000, irho=0.0000)

## Then layers are created, each with its own 'material'.  If you want to force
## two layers to always match SLD you can use the same material in multiple layers.
## The roughnesses of each layer are set to zero to begin with:
layer0 = Slab(material=sld0, thickness=0.0000, interface=10.000)
layer1 = Slab(material=sld1, thickness=1250.0, interface=10.000)
layer2 = Slab(material=sld2, thickness=0.0000, interface=10.000)
layer3 = Slab(material=sld3, thickness=0.0000, interface=10.000)
layer4 = Slab(material=sld4, thickness=0.0000, interface=0.0000)

sample = Stack()
sample.add(layer0)
sample.add(layer1)
sample.add(layer2)
sample.add(layer3)
sample.add(layer4)

## can also be specified as:
# sample = layer0 | layer1 | layer2 | layer3 | layer4
  
## === Constraints ===
## thickness, interface (roughness) etc. are parameters and
## can be constrained, e.g.
# layer0.thickness = layer2.thickness
## (to tie the first layer to have exactly the same thickness as the third layer)
# layer1.interface = layer2.interface
## (to make the roughness between layer1 and layer2 the same as between layer2 and layer3)
# layer0.material = layer4.material
## (make their sld properties match, real and imaginary)
# sld0.rho = sld1.rho
## (to force only the real rho to match for two materials)

## === Fit parameters ===
## "range" specifies a fitting range in terms of min/max value
## "pmp" specifies fitting range in terms of +/-  %
## "pm" specifies fitting range in terms of +/- value

## THETA OFFSET
## this parameter accounts for theta misalignment
## probe.theta_offset.range(-.01,.01)

## INTENSITY
probe.intensity.range(0.95,1.05)

## LAYER RHOs
# sld0.rho.range(1.0690, 3.0690)
# sld1.rho.range(3.0000, 5.0000)
# sld2.rho.range(3.0000, 5.0000)
# sld3.rho.range(3.0000, 5.0000)
# sld4.rho.range(-1.0000, 1.0000)

## LAYER ABSORPTIONS (imaginary rho)
sld0.irho.range(-1.0000, 1.0000)
sld1.irho.range(-1.0000, 1.0000)
sld2.irho.range(-1.0000, 1.0000)
# sld3.irho.range(-1.0000, 1.0000)
sld4.irho.range(-1.0000, 1.0000)

## LAYER THICKNESSES
layer0.thickness.range(0.0000, 100.00)
layer1.thickness.range(1150.0, 1350.0)
# layer2.thickness.range(0.0000, 100.00)
layer3.thickness.range(0.0000, 100.00)
layer4.thickness.range(0.0000, 100.00)

## LAYER ROUGHNESSES
###################################################################
## the 'interface' associated with layer0 is the boundary between #
## layer0 and layer1, and similarly for layer(N) and layer(N+1)   #
###################################################################
layer0.interface.range(0.0000, 20.000)
# layer1.interface.range(0.0000, 20.000)
# layer2.interface.range(0.0000, 20.000)
layer3.interface.range(0.0000, 20.000)

## === Problem definition ===
## a model object consists of a sample and a probe,
## zed is the step size in Angstroms to be used for rendering the profile
## increase zed to speed up the calculation
zed = 1    

## step = True corresponds to a calculation of the reflectivity from an actual profile
## with microslabbed interfaces.  When step = False, the Nevot-Croce
## approximation is used to account for roughness.  This approximation speeds up
## the calculation tremendously, and is reasonably accuarate as long as the
## roughness is much less than the layer thickness
step = False

model = Experiment(sample=sample, probe=probe, dz=zed, step_interfaces = step)
## simultaneous fitting: if you define two models
# models = model1, model2
# problem = MultiFitProblem(models=models)

# fitting a single model:
problem = FitProblem(model)

problem.name = ""