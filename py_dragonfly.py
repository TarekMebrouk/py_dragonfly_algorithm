import random as rand


class Solution:

    # create new random solution
    def __init__(self):
        size = rand.randint(0, 20)
        self.fitness = 0
        self.array = []
        # generate random array for solution
        for i in range(size):
            self.array.append(rand.randint(0, 10))

        # evaluate solution
        self.evaluate()

    # evaluate fitness of solution
    def evaluate(self):
        # take random evaluation of solution
        self.fitness = rand.uniform(20, 50)

    # view solution summary
    def view(self):
        print(f"Solution : Fitness => {self.fitness}, array => {self.array}")


class DragonFly:

    # create new dragonfly meta-heuristic
    def __init__(self, size, neighborhood_radius):
        # init algorithm parameters
        self.population_size = size
        self.neighborhood_radius = neighborhood_radius
        self.enemies_history = []

        # generate random population to start
        self.population = []
        print(f" DragonFly Algorithm")
        print(f"Generation of the starting population")
        print("--------------------------------------------------------------------------------")
        for i in range(self.population_size):
            solution = Solution()
            self.population.append(solution)
        print("--------------------------------------------------------------------------------")

    # launch dragon fly algorithm
    def launch(self, max_iterations):
        count = 0
        while count < max_iterations:
            # update neighborhood_radius
            self.neighborhood_radius += radius

            # update food (best solution) & enemy (worst solution)
            food = max(self.population, key=lambda s: s.fitness)
            enemy = min(self.population, key=lambda s: s.fitness)

            # save worst solution (enemy) in enemies history list
            self.enemies_history.append(enemy)

            for solution in self.population:
                # get neighbors of solution
                neighbors = self.get_neighbors(solution)

                # empty neighbors
                if len(neighbors) == 0:
                    solution = Solution()
                # inheritance and elimination of the best and bad solutions .resp
                else:
                    # get best neighbor solution
                    best_neighbor = max(neighbors, key=lambda s: s.fitness)
                    DragonFly.transformation(solution=solution, food=best_neighbor)

                # evaluate solution
                solution.evaluate()

                # increment iteration
                count += 1
                solution.view()

        # return best solution of population
        return max(self.population, key=lambda s: s.fitness)

    # get list of solution neighbors
    def get_neighbors(self, solution):
        neighbors = []
        for s in self.population:
            distance = abs(s.fitness - solution.fitness)
            if distance <= self.neighborhood_radius:
                neighbors.append(s)
        return neighbors

    # inheritance & escape from best & worst neighbor solution
    @staticmethod
    def transformation(solution, food):
        # inheritance array size & some values
        if len(solution.array) >= len(food.array):
            solution.array = solution.array[:len(food.array)]
        else:
            for i in range(len(food.array) - len(solution.array)):
                solution.array.append(food.array[i])


# main method
if __name__ == "__main__":
    # constants
    iterations = 100
    population_size = 50
    radius = 0.5

    # launch dragonfly algorithm
    process = DragonFly(size=population_size, neighborhood_radius=radius)
    result = process.launch(max_iterations= iterations)
    print("\n\nBest solution found  : ")
    result.view()
