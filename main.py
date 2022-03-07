from production_line import ProductionLine

# Creating a new production line with a initial parameters
production_line = ProductionLine([1, 2, 5], 5, [None, 'A', 'B'], [.3, .3, .3])
# Simulation of production for 100 steps
production_line.simulation(100)
# Result of the simulation
production_line.result()
del production_line
