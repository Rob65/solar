# Test code
This directory contains some test code to verify the correct working of my setup.

The system used consists of 2 Growatt inverters (MID 25KTL3-X1) and a Waveshare RS485  to PoE ethernet module.

## Growatt inverter configuration

The Growatt inverters are setup to use address 1 and 2

## RS485 to PoE ETH configuration

The Waveshare module must be configured to use the Modbus TCP to RTU protocol.
Set the Device Port to 502 which is the standard Modbus TCP/Scada port
The serial settings should match those in the inverter. Standard settings are 9600 Baud, 8 Databits, no parity and 1 stopbit.
All other settings can be kept at the default.

The PoE ETH module should be connected to the Growatt inverters using only the RS485A and RS485B wires. Make sure that all RS485 A wires as well as the RS485B wires are connected together.

## solar.py

This is a simple test program to read the most useful data from both inverters. It reads data from the holding and input registers and presents them in a human readable form. See below for an example of the output

```
Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import solar
>>> solar.read()
Inverter 1:
        Time: Fri 23-6-2023  9:42:19
        PV input
                PV1 417.3 V, 9.0 A, 3755.7 W
                PV2 473.8 V, 5.9 A, 2795.4 W
                PV3 254.1 V, 0.0 A,   0.0 W
                Total: 6551.1 W

        Output
                Freq: 50.02 Hz
                L1: 234.9 V 9.1 A 2137.5 W
                L2: 236.4 V 9.4 A 2222.1 W
                L3: 236.0 V 8.9 A 2100.4 W
                408.1 / 409.4 / 407.5 V
        Summary
                PV1: today   4.6 kWh, total  91.1 kWh
                PV2: today   3.7 kWh, total  90.7 kWh
                PV3: today   0.0 kWh, total   0.0 kWh
                Today:   8.6 kWh, total: 185.3 kWh
                running for 64.8 Hours
                Inverter temp: 55.8 °C

Inverter 2:
        Time: Fri 23-6-2023  9:42:45
        PV input
                PV1 451.3 V, 17.8 A, 8033.1 W
                PV2 428.1 V, 11.7 A, 5008.7 W
                PV3 54.2 V, 0.0 A,   0.0 W
                Total: 13041.8 W
        Output
                Freq: 50.02 Hz
                L1: 233.9 V 18.0 A 4210.2 W
                L2: 238.2 V 18.0 A 4287.6 W
                L3: 236.7 V 17.7 A 4189.5 W
                405.6 / 412.0 / 409.9 V
        Summary
                PV1: today   9.8 kWh, total 181.1 kWh
                PV2: today   6.8 kWh, total 155.3 kWh
                PV3: today   0.0 kWh, total  11.9 kWh
                Today:  17.1 kWh, total: 356.4 kWh
                running for 58.1 Hours
                Inverter temp: 60.3 °C

>>>
```