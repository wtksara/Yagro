from components import A, B, P


class Worker:

    def __init__(self, station):
        # Station on which worker is working
        self.station = station
        # Worker has only two hands available
        self.left_hand = None
        self.right_hand = None
        # Auxiliary variables
        self.component_A = False
        self.component_B = False
        # Status of assembling
        self.assembly_status = False
        # Time to finish assembling
        self.assembly_time = 0
        # Worker performed a action
        self.performed = False

    # Function, which check the slot on conveyor
    def check_conveyor(self, conveyor):
        # During assembling worker can not touch the conveyor
        if not self.assembly_status:
            # Collecting the components
            self.check_component(conveyor)

            # Both components are collected
            if self.component_A and self.component_B:
                # Start of assembling
                self.assembly_status = True

        else:
            self.assembly_time += 1
            # Product can be placed on fourth slot
            # First attempt of placing product failed
            if self.assembly_time > 4:
                self.put_product(conveyor)

            # First attempt of placing product
            elif self.assembly_time == 4:
                # Product has been created and is being hold in right hand
                product = P(self.left_hand, self.right_hand)
                self.left_hand = None
                self.right_hand = product
                self.component_A = False
                self.component_B = False

                self.put_product(conveyor)

    def put_product(self, conveyor):
        # Conveyor is empty, product can be placed
        if conveyor[self.station] is None:
            conveyor.pop(self.station)
            conveyor.insert(self.station, self.right_hand)

            self.assembly_status = False
        # On the conveyor there is a component which can be taken if the left hand is empty
        else:
            self.check_component(conveyor)

    # Function, which check what kind of component is on slot
    def check_component(self, conveyor):

        if isinstance(conveyor[self.station], A):
            # If there is not component A yet in hands
            if not self.component_A:
                self.component_A = True
                self.pick(conveyor)

        elif isinstance(conveyor[self.station], B):
            # If there is not component B yet in hands
            if not self.component_B:
                self.component_B = True
                self.pick(conveyor)

    def pick(self, conveyor):
        # Worker can hold two items (component or product) at the time
        if self.left_hand is None:
            # Taking the component
            self.left_hand = conveyor.pop(self.station)
            conveyor.insert(self.station, None)
            # Action has been performed
            self.performed = True

        elif self.right_hand is None:
            self.right_hand = conveyor.pop(self.station)
            conveyor.insert(self.station, None)
            self.performed = True

