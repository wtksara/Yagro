import random
from components import A, B, P
from worker import Worker


class ProductionLine:
    # Parameters:
    # workers_stations : stations start from 1 instead 0
    # lenght: lenght of the conveyor
    # components : list of available components
    # distribution : distribution of components
    def __init__(self, workers_stations, lenght, components, distribution):

        # Setting of the production conveyor
        self.conveyor = [None] * lenght
        self.lenght = lenght
        self.components = components
        self.distribution = distribution

        # Setting workers stations
        self.workers = []

        for x in range(len(workers_stations)):
            # Creation of top worker
            self.workers.append(Worker(workers_stations[x] - 1))
            # Creation of bottom worker
            self.workers.append(Worker(workers_stations[x] - 1))

        # History of production
        self.finished_products = 0
        self.not_collected_A = 0
        self.not_collected_B = 0

    # Function, which simulate the movement of conveyor
    def simulation(self, steps):

        # Simulation of amount of steps
        for x in range(steps):

            # Component is coming off the production line
            component = self.conveyor.pop(self.lenght-1)

            if isinstance(component, P):
                self.finished_products += 1

            elif isinstance(component, A):
                self.not_collected_A += 1

            elif isinstance(component, B):
                self.not_collected_B += 1

            # Release memory
            del component

            # Creation of new component
            component_type = random.choices(self.components, self.distribution)
            if component_type[0] == 'A':
                self.conveyor.insert(0, A())
            elif component_type[0] == 'B':
                self.conveyor.insert(0, B())
            else:
                self.conveyor.insert(0, None)

            print(self.conveyor)

            # Pair of workers are checking the conveyor
            for top_worker, bottom_worker in zip(self.workers[0::2], self.workers[1::2]):
                top_worker.check_conveyor(self.conveyor)
                # Top worker has performed a action, so bottom one has to wait for next slot
                if not top_worker.performed:
                    bottom_worker.check_conveyor(self.conveyor)

            # Resetting the actions of workers after each loop
            for worker in self.workers:
                worker.performed = False
            print(self.conveyor)
            print("")

    # Function, which shows results of the production line
    def result(self):
        print(' Result of simulation of production line' +
              '\n Amount of finished products: ' + repr(self.finished_products) +
              '\n Amount of not collected A: ' + repr(self.not_collected_A) +
              '\n Amount of not collected B: ' + repr(self.not_collected_B))
