import pyvisa
import pyvisa-sim
rm = pyvisa.ResourceManager()
print(rm.list_resources_info())