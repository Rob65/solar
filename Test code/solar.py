import time
from pyModbusTCP.client import ModbusClient

inverter = ModbusClient(host="192.168.0.5", port=502, auto_open=True)
weekday = [ 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat' ]

def tenth(high, low):
	"""
	Return two registers as a 32 bit value with 0.1 scaling
	"""
	return high * 6553.6 + low * 0.1
	
	
def read():
	"""
	Read registers of Solar converts
	"""
	inverter.unit_id = 1
	datetime1 = inverter.read_holding_registers(45,7)
	pv1       = inverter.read_input_registers(0,15)
	output1   = inverter.read_input_registers(35,18)
	power1    = inverter.read_input_registers(53,18)
	temp1     = inverter.read_input_registers(93,1)
	
	inverter.unit_id = 2
	datetime2 = inverter.read_holding_registers(45,7)
	pv2       = inverter.read_input_registers(0,15)
	output2   = inverter.read_input_registers(35,18)
	power2    = inverter.read_input_registers(53,18)
	temp2     = inverter.read_input_registers(93,1)

###	Solar 1

	print('Inverter 1:')
	print(f'	Time: {weekday[datetime1[6]]} {datetime1[2]}-{datetime1[1]}-{datetime1[0]} {datetime1[3]:2d}:{datetime1[4]:02d}:{datetime1[5]:02d}')
	
	pv = pv1
	input_power = tenth(pv[1], pv[2])
	pv1_volt    =  pv[3] * 0.1
	pv1_current = pv[4] * 0.1
	pv1_power   = tenth(pv[5], pv[6])
	pv2_volt    =  pv[7] * 0.1
	pv2_current = pv[8] * 0.1
	pv2_power   = tenth(pv[9], pv[10])
	pv3_volt    =  pv[11] * 0.1
	pv3_current = pv[12] * 0.1
	pv3_power   = tenth(pv[13], pv[14])

	print(f'	PV input')
	print(f'		PV1 {pv1_volt:3.1f} V, {pv1_current:2.1f} A, {pv1_power:5.1f} W')
	print(f'		PV2 {pv2_volt:3.1f} V, {pv2_current:2.1f} A, {pv2_power:5.1f} W')
	print(f'		PV3 {pv3_volt:3.1f} V, {pv3_current:2.1f} A, {pv3_power:5.1f} W')

	print(f'		Total: {input_power:5.1f} W');
	print()
	
	o = output1
	output_power = tenth(o[0], o[1])
	freq = o[2]/100
	v_ac1 = o[3] * 0.1
	i_ac1 = o[4] * 0.1
	p_ac1 = tenth(o[5], o[6])
	v_ac2 = o[7] * 0.1
	i_ac2 = o[8] * 0.1
	p_ac2 = tenth(o[9], o[10])
	v_ac3 = o[11] * 0.1
	i_ac3 = o[12] * 0.1
	p_ac3 = tenth(o[13], o[14])
	v_rs  = o[15] * 0.1
	v_st  = o[16] * 0.1
	v_tr  = o[17] * 0.1
	
	print(f'	Output')
	print(f'		Freq: {freq:1.2f} Hz')
	print(f'		L1: {v_ac1:3.1f} V {i_ac1:2.1f} A {p_ac1:4.1f} W')
	print(f'		L2: {v_ac2:3.1f} V {i_ac2:2.1f} A {p_ac2:4.1f} W')
	print(f'		L3: {v_ac3:3.1f} V {i_ac3:2.1f} A {p_ac3:4.1f} W')
	print(f'		{v_rs:3.1f} / {v_st:3.1f} / {v_tr:3.1f} V')
	
	p = power1
	eac_today = tenth(p[0], p[1])
	eac_total = tenth(p[2], p[3])
	time_total = tenth(p[4], p[5]) / 720
	epv1_today = tenth(p[6], p[7])
	epv1_total = tenth(p[8], p[9])
	epv2_today = tenth(p[10], p[11])
	epv2_total = tenth(p[12], p[13])
	epv3_today = tenth(p[14], p[15])
	epv3_total = tenth(p[16], p[17])
	
	print(f'	Summary')
	print(f'		PV1: today {epv1_today:5.1f} kWh, total {epv1_total:5.1f} kWh')
	print(f'		PV2: today {epv2_today:5.1f} kWh, total {epv2_total:5.1f} kWh')
	print(f'		PV3: today {epv3_today:5.1f} kWh, total {epv3_total:5.1f} kWh')
	
	print(f'		Today: {eac_today:5.1f} kWh, total: {eac_total:5.1f} kWh')
	print(f'		running for {time_total:1.1f} Hours')
	
	temp = temp1[0] / 10.0
	print(f'		Inverter temp: {temp:1.1f} °C')
	print()

### Solar 2

	print('Inverter 2:')	
	print(f'	Time: {weekday[datetime2[6]]} {datetime2[2]}-{datetime2[1]}-{datetime2[0]} {datetime2[3]:2d}:{datetime2[4]:02d}:{datetime2[5]:02d}')
	
	pv = pv2
	input_power = tenth(pv[1], pv[2])
	pv1_volt    =  pv[3] * 0.1
	pv1_current = pv[4] * 0.1
	pv1_power   = tenth(pv[5], pv[6])
	pv2_volt    =  pv[7] * 0.1
	pv2_current = pv[8] * 0.1
	pv2_power   = tenth(pv[9], pv[10])
	pv3_volt    =  pv[11] * 0.1
	pv3_current = pv[12] * 0.1
	pv3_power   = tenth(pv[13], pv[14])

	print(f'	PV input')
	print(f'		PV1 {pv1_volt:3.1f} V, {pv1_current:2.1f} A, {pv1_power:5.1f} W')
	print(f'		PV2 {pv2_volt:3.1f} V, {pv2_current:2.1f} A, {pv2_power:5.1f} W')
	print(f'		PV3 {pv3_volt:3.1f} V, {pv3_current:2.1f} A, {pv3_power:5.1f} W')

	print(f'		Total: {input_power:5.1f} W')
	
	o = output2
	output_power = tenth(o[0], o[1])
	freq = o[2]/100
	v_ac1 = o[3] * 0.1
	i_ac1 = o[4] * 0.1
	p_ac1 = tenth(o[5], o[6])
	v_ac2 = o[7] * 0.1
	i_ac2 = o[8] * 0.1
	p_ac2 = tenth(o[9], o[10])
	v_ac3 = o[11] * 0.1
	i_ac3 = o[12] * 0.1
	p_ac3 = tenth(o[13], o[14])
	v_rs  = o[15] * 0.1
	v_st  = o[16] * 0.1
	v_tr  = o[17] * 0.1
	
	print(f'	Output')
	print(f'		Freq: {freq:2.2f} Hz')
	print(f'		L1: {v_ac1:3.1f} V {i_ac1:2.1f} A {p_ac1:4.1f} W')
	print(f'		L2: {v_ac2:3.1f} V {i_ac2:2.1f} A {p_ac2:4.1f} W')
	print(f'		L3: {v_ac3:3.1f} V {i_ac3:2.1f} A {p_ac3:4.1f} W')
	print(f'		{v_rs:3.1f} / {v_st:3.1f} / {v_tr:3.1f} V')
	
	p = power2
	eac_today = tenth(p[0], p[1])
	eac_total = tenth(p[2], p[3])
	time_total = tenth(p[4], p[5]) / 720
	epv1_today = tenth(p[6], p[7])
	epv1_total = tenth(p[8], p[9])
	epv2_today = tenth(p[10], p[11])
	epv2_total = tenth(p[12], p[13])
	epv3_today = tenth(p[14], p[15])
	epv3_total = tenth(p[16], p[17])

	print(f'	Summary')
	print(f'		PV1: today {epv1_today:5.1f} kWh, total {epv1_total:5.1f} kWh')
	print(f'		PV2: today {epv2_today:5.1f} kWh, total {epv2_total:5.1f} kWh')
	print(f'		PV3: today {epv3_today:5.1f} kWh, total {epv3_total:5.1f} kWh')
	
	print(f'		Today: {eac_today:5.1f} kWh, total: {eac_total:5.1f} kWh')
	print(f'		running for {time_total:1.1f} Hours')

	temp = temp2[0] / 10.0
	print(f'		Inverter temp: {temp:1.1f} °C')
	
	print()
	inverter.close()
	
def __every(delay, task):
	cont = True
	next_time = time.time() + delay
	while cont:
		time.sleep(max(0, next_time - time.time()))
		try:
			task()
		except Exception:
			cont = False
			print('Stopped')
			# in production code you might want to have this instead of course:
			# logger.exception("Problem while executing repetitive task.")
		# skip tasks if we are behind schedule:
		next_time += (time.time() - next_time) // delay * delay + delay

	
def repeat(times, interval):
	next_time = time.time() + interval
	while(times > 0):
		time.sleep(max(0, next_time - time.time()))
		try:
			read()
		except Exception:
			print('Failed to read')
		next_time += (time.time() - next_time) // interval * interval + interval
		times = times - 1