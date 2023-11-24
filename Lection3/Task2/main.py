import utils
import json

system = {
    "Name": 
    "--DESKTOP-B9JSHAT",
    "CPU": "CPU_Name" "Intel(R) Core(TM) i3-8100",
    "Architecture": "X86-64",
    "Socket": "LGA 1151",
    "Cores": 6,
    "MaxFreq": "4096x2304",
    

"--RAM": "Kingston-16Gb",
    "Form-factor": "SO-DIMM",
    "Frequency": 3200,
    
"--Motherboard": "Asus PRIME H510M-K R2.0 (s1200, Intel H470, PCI-Ex16)" ,
    "Network card type": "Intel I219V",
    "LAN ports quantity": 1,
    "Type of RAM": "DDR4",
    "Chipset model": "Intel H510", 

"--Disk": "HDD THOSHIBA HDWD110",
    "Maximum interface speed": "600 MB/s",
    "Maximum read speed": "901 MB/s",

"--GPU": "GeForce GTX 1050",
    "VRAM": "6 Gb",
    "Graphics Clock (MHz)": 1354,
    "Processor Clock (MHz)": 1455,
}

print ("System details: ")
print (json.dumps(system, indent=5))
utils.drawLine()
