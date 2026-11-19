from PyLTSpice import SimRunner, SpiceEditor, LTspice, RawRead
import numpy as np
import matplotlib.pyplot as plt         # use matplotlib for plotting the results

runner = SimRunner(output_folder='./test_rc_2', simulator=LTspice)  # Configures the simulator to use and output
# folder

netlist = SpiceEditor("rc.net")  # Open the Spice Model, and creates the .net
# set default arguments
netlist.set_parameters(res=1e3, cap=1e-6)
#netlist.set_component_value('R2', '2k')  # Modifying the value of a resistor
#netlist.set_component_value('R1', '4k')
#netlist.set_element_model('V1', "SINE(0 1 3k)")  # Modifying the
#netlist.set_component_value('XU1:C2', 20e-12)  # modifying a
# define simulation
#netlist.add_instructions(".tran 3m")
netlist.add_instructions(".ac dec 100 1 10Meg")

#raw, log = runner.run_now(netlist, run_filename="rc_out")

# Vykreslení
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))

for xres in (1e2, 1e3, 1e4, 1e5):
    netlist.set_parameters(res=xres)
    for xcap in (1e-8, 1e-7, 1e-6, 1e-5):
        netlist.set_parameters(cap=xcap)
        # overriding he automatic netlist naming
        run_netlist_file = "{}_{}_{}.net".format(netlist.netlist_file.name, xres, xcap)
        raw, log = runner.run_now(netlist, run_filename=run_netlist_file)
        # Process here the simulation results

        raw = RawRead("test_rc_2/{}_{}_{}.raw".format(netlist.netlist_file.name, xres, xcap))   # Read the RAW file contents from disk

        #print(raw.get_trace_names())            # Get and print a list of all the traces
        #print(raw.get_raw_property())           # Print all the properties found in the Header section

        vin = raw.get_trace('V(in)')            # Get the trace data
        vout = raw.get_trace('V(out)')          # Get the second trace

        #steps = raw.get_steps()                 # Get list of step numbers ([0,1,2]) for sweeped simulations
                                                # Returns [0] if there is just 1 step

        #print(f"Počet .step analýz: {steps}")

        xdata = raw.get_axis()                  # Get the X-axis data (time)
        # Get all the values for the 'vin' trace
        yVin = vin.get_wave()                  

        # Get all the values for the 'vout' trace
        yVout = vout.get_wave()                 
        gain_db = 20 * np.log10(np.abs(yVout/yVin))
        phase_deg = np.angle(vout, deg=True)

        # Najdi -3 dB bod (přibližně)
        target_db = max(gain_db) - 3
        idx_3db = np.where(gain_db <= target_db)[0]
        f_3db = np.abs(xdata[idx_3db[0]]) if len(idx_3db) > 0 else None

        # Zisk
        ax1.semilogx(xdata, gain_db, label=f"Zisk [{xres}_{xcap}]")
        if f_3db:
            ax1.axvline(f_3db, color="red", linestyle="--", label=f"-3 dB bod: {f_3db:.1f} Hz")

        # Fáze
        ax2.semilogx(xdata, phase_deg, label=f"Fáze [{xres}_{xcap}]")

ax1.set_title("Bodeho diagram")
ax1.set_ylabel("Zisk [dB]")
ax1.set_xlabel("Frekvence [Hz]")
ax1.grid(which='both', linestyle='--')
ax1.legend()
ax2.set_ylabel("Fáze [°]")
ax2.set_xlabel("Frekvence [Hz]")
ax2.grid(which='both', linestyle='--')
ax2.legend()

plt.tight_layout()
plt.show()                              # Show matplotlib's interactive window with the plots
