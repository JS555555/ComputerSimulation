from approach1 import BoardSimulation
from approach2 import BoardSimulation_app2



def main():
    simulation = BoardSimulation()
    simulation.run_simulation(show_simulation=True)
    simulation.simulation_result()

    simulation_2 = BoardSimulation_app2()
    simulation_2.run_simulation(show_simulation=True)
    simulation_2.simulation_result()


if __name__ == "__main__":
    main()