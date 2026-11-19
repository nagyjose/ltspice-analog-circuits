from PyLTSpice import AscEditor, SimRunner, SpiceEditor  # Imports the class that manipulates the asc file
from PyLTSpice.sim.tookit.montecarlo import Montecarlo  # Imports the Montecarlo toolkit class
import time

start_time = time.time()

netlist = SpiceEditor("rc2.net")  # Reads the asc file into memory
netlist.set_component_value('R1', '1000')
netlist.set_component_value('C1', '1u')
#netlist.set_parameters(cap=1e-6)
netlist.add_instructions(
    ".ac dec 100 1 100k",
    ".meas AC Gain MAX mag(V(OUT))",
    ".meas AC Fcut TRIG mag(V(OUT))=Gain/sqrt(2) FALL=last"
)

runner = SimRunner(output_folder='./test_rc_mc')  # Instantiates the runner class, with the output folder already set
mc = Montecarlo(netlist, runner)  # Instantiates the Montecarlo class, with the asc file already in memory

# The following lines set the default tolerances for the components
mc.set_tolerance('R1', 0.05)  # 1% tolerance, default distribution is uniform
mc.set_tolerance('C1', 0.1, distribution='uniform')  # 10% tolerance, explicit uniform distribution
#mc.set_tolerance('V', 0.1, distribution='normal')  # 10% tolerance, but using a normal distribution

# Some components can have a different tolerance
#mc.set_tolerance('R1', 0.05)  # 5% tolerance for R1 only. This only overrides the default tolerance for R1

# Tolerances can be set for parameters as well
#mc.set_parameter_deviation('Vos', 3e-4, 5e-3, 'uniform')  # The keyword 'distribution' is optional
mc.prepare_testbench(num_runs=1000)  # Prepares the testbench for 1000 simulations

# Finally the netlist is saved to a file
#mc.save_netlist('./testfiles/rc.net')

setup_time = time.time()
print(f"Setup time: {setup_time - start_time:.3f} s")

mc.run_testbench(runs_per_sim=100)  # Runs the simulation with splits of 100 runs each
logs = mc.read_logfiles()   # Reads the log files and stores the results in the results attribute
logs.obtain_amplitude_and_phase_from_complex_values()  # Splits the complex values into real and imaginary parts
logs.export_data('./test_rc_mc/data_testbench.csv')  # Exports the data to a csv file

run1_time = time.time()
print(f"Run #1 time: {run1_time - setup_time:.3f} s")

logs.plot_histogram('fcut_from')  # Plots the histograms for the results
mc.cleanup_files()  # Deletes the temporary files

run1_time = time.time()
print(f"Run #1 time: {run1_time - setup_time:.3f} s")

#print("=====================================")
# Now using the second method, where the simulations are ran one by one
"""mc.clear_simulation_data()  # Clears the simulation data
mc.reset_netlist()  # Resets the netlist to the original
mc.run_analysis(num_runs=1000)  # Runs the 1000 simulations
logs = mc.read_logfiles()   # Reads the log files and stores the results in the results attribute
logs.export_data('./test_rc_mc/data_sims.csv')  # Exports the data to a csv file
logs.plot_histogram('fcut_from')  # Plots the histograms for the results
mc.cleanup_files()  # Deletes the temporary files"""

#run2_time = time.time()
#print(f"Run #2 time: {run2_time - run1_time:.3f} s")
#print(f"Run all time: {run2_time - start_time:.3f} s")

