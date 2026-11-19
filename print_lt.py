import inspect
from PyLTSpice import AscEditor, LTSpiceLogReader, LTspice, RawRead, RawWrite, SimCommander, SimRunner, SpiceCircuit, SpiceEditor, SpiceReadException, Trace
from PyLTSpice.sim.tookit.montecarlo import Montecarlo

print("Metody třídy AscEditor:")
for name, member in inspect.getmembers(AscEditor, predicate=inspect.isfunction):
    print(" > " + name)

print("Metody třídy LTSpiceLogReader:")
for name, member in inspect.getmembers(LTSpiceLogReader, predicate=inspect.isfunction):
    print(" > " + name)
    
print("Metody třídy LTspice:")
for name, member in inspect.getmembers(LTspice, predicate=inspect.isfunction):
    print(" > " + name)
    
print("Metody třídy RawRead:")
for name, member in inspect.getmembers(RawRead, predicate=inspect.isfunction):
    print(" > " + name)
    
print("Metody třídy RawWrite:")
for name, member in inspect.getmembers(RawWrite, predicate=inspect.isfunction):
    print(" > " + name)
    
print("Metody třídy SimCommander:")
for name, member in inspect.getmembers(SimCommander, predicate=inspect.isfunction):
    print(" > " + name)
    
print("Metody třídy SimRunner:")
for name, member in inspect.getmembers(SimRunner, predicate=inspect.isfunction):
    print(" > " + name)
    
print("Metody třídy SpiceCircuit:")
for name, member in inspect.getmembers(SpiceCircuit, predicate=inspect.isfunction):
    print(" > " + name)
        
print("Metody třídy SpiceEditor:")
for name, member in inspect.getmembers(SpiceEditor, predicate=inspect.isfunction):
    print(" > " + name)
        
print("Metody třídy SpiceReadException:")
for name, member in inspect.getmembers(SpiceReadException, predicate=inspect.isfunction):
    print(" > " + name)
        
print("Metody třídy Trace:")
for name, member in inspect.getmembers(Trace, predicate=inspect.isfunction):
    print(" > " + name)

print("Metody třídy Montecarlo:")
for name, member in inspect.getmembers(Montecarlo, predicate=inspect.isfunction):
    print(" > " + name)

