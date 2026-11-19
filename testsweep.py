from PyLTSpice import SimRunner, SpiceEditor, LTspice

runner = SimRunner(output_folder='./temp_batch3', simulator=LTspice)  # Configures the simulator to use and output
# folder

netlist = SpiceEditor("./Current_limiter_NPN.asc")  # Open the Spice Model, and creates the .net
# set default arguments
netlist.set_parameters(drive=100, sense=0.6, supply=15, load=10)
#netlist.set_component_value('R2', '2k')  # Modifying the value of a resistor
#netlist.set_component_value('R1', '4k')
#netlist.set_element_model('V3', "SINE(0 1 3k 0 0 0)")  # Modifying the
#netlist.set_component_value('XU1:C2', 20e-12)  # modifying a
# define simulation
"""netlist.add_instructions(
        "; Simulation settings",
        ".param run = 0"
)"""

"""for opamp in ('AD712', 'AD820'):
    netlist.set_element_model('XU1', opamp)
    for supply_voltage in (5, 10, 15):
        netlist.set_component_value('V1', supply_voltage)
        netlist.set_component_value('V2', -supply_voltage)
        # overriding he automatic netlist naming
        run_netlist_file = "{}_{}_{}.net".format(netlist.netlist_file.name, opamp, supply_voltage)
        raw, log = runner.run_now(netlist, run_filename=run_netlist_file)
        # Process here the simulation results"""

raw, log = runner.run_now(netlist, run_filename="testsweep.net")
