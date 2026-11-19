from PyLTSpice import SimRunner, SpiceEditor, LTspice, RawRead
import numpy as np
import matplotlib.pyplot as plt         # use matplotlib for plotting the results
from LTspiceLIB import extract_all_traces 

runner = SimRunner(output_folder='./current_lim_out', simulator=LTspice)  # Configures the simulator to use and output
# folder

netlist = SpiceEditor("Current_limiter_NPN_tb.net")  # Open the Spice Model, and creates the .net
# set default arguments
#netlist.set_parameters(res=1e3, cap=1e-6)
netlist.set_component_value('Rsense', '0.6')
netlist.set_component_value('Rc', '100')
#netlist.set_component_value('Rload', '0.6')
#netlist.set_component_value('R1', '4k')
netlist.set_element_model('Vcc', "15")
#netlist.set_component_value('XU1:C2', 20e-12)  # modifying a
# define simulation
#netlist.add_instructions(".tran 3m")
#netlist.add_instructions(".ac dec 100 1 10Meg")

raw, log = runner.run_now(netlist, run_filename="current_lim_out")

raw = RawRead("current_lim_out/current_lim_out.raw")   # Read the RAW file contents from disk

dict = extract_all_traces(raw, plot=True)

"""print(raw.get_trace_names())            # Get and print a list of all the traces
#print(raw.get_raw_property())           # Print all the properties found in the Header section

xdata = raw.get_axis() 
vin = raw.get_trace('V(in)')      
vout = raw.get_trace('V(out)') 
vb = raw.get_trace('V(b)') 
ve = raw.get_trace('V(e)')         
irload = raw.get_trace('I(Rload)')  
irsense = raw.get_trace('I(Rsense)')  
irc = raw.get_trace('I(Rc)')  
ibq1= raw.get_trace('Ib(Q1)')  
icq1= raw.get_trace('Ic(Q1)')
ieq1= raw.get_trace('Ie(Q1)')
ibq2= raw.get_trace('Ib(Q2)')
icq2= raw.get_trace('Ic(Q2)')
ieq2= raw.get_trace('Ie(Q2)')

yVin = vin.get_wave()                  
yVout = vout.get_wave()                
yVb = vb.get_wave() 
yVe = ve.get_wave()
yIrload = irload.get_wave() 
yIrsense = -irsense.get_wave()
yIrc = -irc.get_wave()
yIbq1 = ibq1.get_wave()
yIcq1 = icq1.get_wave()
yIeq1 = ieq1.get_wave()
yIbq2 = ibq2.get_wave()
yIcq2 = icq2.get_wave()
yIeq2 = ieq2.get_wave()
yPrload = yVout * yIrload
yPrsense = (yVe - yVout) * yIrsense
yPrc = (yVin - yVb) * yIrc
yPq1 = (yVb - yVout) * yIcq1 + (yVe - yVout) * yIbq1
yPq2 = (yVin - yVe) * yIcq2 + (yVb - yVe) * yIbq2

# Najdi index a hodnotu maxima
max_idx = np.argmax(yPrload)
max_x = xdata[max_idx]
max_y = yPrload[max_idx]

print(f"Max ztráty na Rload: {max_y} W")

deriv = (yIrload[0] - yIrload[max_idx]) / (0 - xdata[max_idx])
smr = deriv * xdata + yIrload[0]

print(f"Max proud Rload: {yIrload[0]:.2f} A")
print(f"Cutoff proud Rload: {yIrload[max_idx]:.2f} A")
print(f"Směrnice cutoff části proudu: {deriv:.3f}")


# Vykreslení
fig, ((axV, axI), (axP, axN)) = plt.subplots(2, 2, figsize=(16, 9))
fig.suptitle("Current limiter NPN")

# Napětí
axV.plot(xdata, yVin, label="V(in)")
axV.plot(xdata, yVout, label="V(out)")
axV.plot(xdata, yVb, label="V(b)")
axV.plot(xdata, yVe, label="V(e)")
axV.axvline(x=max_x, color='r', linestyle='--', linewidth=1)

axV.set_ylabel("Voltage [V]")
axV.set_xlabel("Load [ohm]")
axV.grid(which='both', linestyle='--')
axV.margins(x=0)
axV.legend()

# Proudy
axI.plot(xdata, yIrload, label="I(Rload)")
axI.plot(xdata, yIrsense, label="I(Rsense)")
axI.plot(xdata, yIrc, label="I(Rc)")
axI.plot(xdata, yIcq1, label="Ic(Q1)")
axI.plot(xdata, yIcq2, label="Ic(Q2)")
axI.axvline(x=max_x, color='r', linestyle='--', linewidth=1)
axI.axhline(y=yIrload[max_idx], color='b', linestyle='--', linewidth=1)
axI.axhline(y=yIrload[0], color='b', linestyle='--', linewidth=1)
axI.plot(xdata, smr, 'g--', label=f'y = {deriv:.3f} * x + {yIrload[0]:.2f}')

axI.set_ylabel("Current [A]")
axI.set_xlabel("Load [ohm]")
axI.grid(which='both', linestyle='--')
axI.margins(x=0)
axI.legend()

# Ztrátové výkony
axP.plot(xdata, yPrload, label="P(Rload)")
axP.plot(xdata, yPrsense, label="P(Rsense)")
axP.plot(xdata, yPrc, label="P(Rc)")
axP.plot(xdata, yPq1, label="P(Q1)")
axP.plot(xdata, yPq2, label="P(Q2)")
axP.plot(max_x, max_y, 'ro', label='Maximum')
axP.axvline(x=max_x, color='r', linestyle='--', linewidth=1)
axP.axhline(y=max_y, color='r', linestyle='--', linewidth=1)

axP.set_ylabel("Power losses [W]")
axP.set_xlabel("Load [ohm]")
axP.grid(which='both', linestyle='--')
axP.margins(x=0)
axP.legend()

plt.tight_layout()
plt.show() """
