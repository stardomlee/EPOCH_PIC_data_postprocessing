#################
##  postpic define ### 

import postpic as pp

print pp.__version__     # postpic version

pp.chooseCode('epoch')
dr = pp.readDump('Data/0020.sdf') 
print(dr)
# the dumpreader knwos all the information of the simulation
print('The simulations was running on {} spatial dimensions.'.format(dr.simdimensions()))

# if needed, postpic can be bypassed and the underlying datastructure (sdf in this case)
# can be accessed directly via keys
print(dr.keys())
print dr['Header']

print(dr.listSpecies())# the multispecies Object is used to access particle data
ms = pp.MultiSpecies(dr, 'electron')
# ms is representing the species "Electrons"
print(ms)

x = ms('x')
print(len(x))

# you can look at  for a list of predefined values
#print pp.particle_scalars