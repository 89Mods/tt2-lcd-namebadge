import cocotb
import random
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer, ClockCycles

async def test_lcd_data(dut, RS, dout):
	await ClockCycles(dut.CLK, 1)
	assert dut.E.value == 0
	assert dut.RS.value == RS
	assert dut.dout.value == dout
	await ClockCycles(dut.CLK, 1)
	assert dut.E.value == 1
	assert dut.RS.value == RS
	assert dut.dout.value == dout
	assert dut.LED1.value == dout & 1

async def test_lcd_string(dut, str):
	dut._log.info("Testing for string: %s" % str)
	for c in str:
		i = ord(c)
		await test_lcd_data(dut, 1, i >> 4)
		await test_lcd_data(dut, 1, i & 15)

@cocotb.test()
async def test_lcd(dut):
	dut._log.info("start")
	clock = Clock(dut.CLK, 1, units="ms")
	cocotb.start_soon(clock.start())
	dut.EF0.value = 0
	dut.EF1.value = 0
	
	dut._log.info("reset")
	dut.RST.value = 1
	await ClockCycles(dut.CLK, 5)
	dut.RST.value = 0
	
	await ClockCycles(dut.CLK, 2)
	
	for itt in range(0, 16):
		ef_0 = random.randint(0, 1)
		ef_1 = random.randint(0, 1)
		dut.EF0.value = ef_0
		dut.EF1.value = ef_1

		await test_lcd_data(dut, 0, 0b0011)
		await test_lcd_data(dut, 0, 0b0010)
		await test_lcd_data(dut, 0, 0b0000)
		await test_lcd_data(dut, 0, 0b1111)
		await test_lcd_data(dut, 0, 0b0000)
		await test_lcd_data(dut, 0, 0b0001)
		assert dut.LED0.value == 0
		
		await ClockCycles(dut.CLK, 4)
		await test_lcd_string(dut, "Hi, I'm Tholin :3")
		assert dut.LED0.value == 0
		for i in range(0, 11):
			await test_lcd_data(dut, 0, 0b1101)
			await test_lcd_data(dut, 0, 0b0100)
		await test_lcd_string(dut, "www.tholin.dev   ")
		await test_lcd_data(dut, 1, 3)
		await test_lcd_data(dut, 1, (ef_0 + ef_1) & 1)
		await test_lcd_data(dut, 1, 3)
		await test_lcd_data(dut, 1, (ef_0 + ef_1) >> 1)
		assert dut.LED0.value == 0
		for i in range(0, 154):
			await test_lcd_data(dut, 0, 0b0011)
		await test_lcd_data(dut, 0, 0b0011)
		await test_lcd_data(dut, 0, 0b0010)
		await test_lcd_data(dut, 0, 0b0000)
		await test_lcd_data(dut, 0, 0b1111)
		await test_lcd_data(dut, 0, 0b1100)
		await test_lcd_data(dut, 0, 0b0111)
		
		await test_lcd_string(dut, "Avali")
		assert dut.LED0.value == 1
		for i in range(0, 28):
			await test_lcd_data(dut, 0, 0b0000)
		for i in range(0, 2):
			await test_lcd_data(dut, 0, 0b1001)
			assert dut.LED1.value == 1
			await test_lcd_data(dut, 0, 0b1000)
		await test_lcd_string(dut, "Software Dev")
		for i in range(0, 28):
			await test_lcd_data(dut, 0, 0b0000)
		for i in range(0, 2):
			await test_lcd_data(dut, 0, 0b1100)
			await test_lcd_data(dut, 0, 0b0100)
		await test_lcd_string(dut, "Hardware Dev")
		assert dut.LED0.value == 1
		for i in range(0, 28):
			await test_lcd_data(dut, 0, 0b0000)
		for i in range(0, 2):
			await test_lcd_data(dut, 0, 0b1001)
			await test_lcd_data(dut, 0, 0b0110)
		await test_lcd_string(dut, "VRC World Maker")
		assert dut.LED0.value == 1
		for i in range(0, 66):
			await test_lcd_data(dut, 0, 0b0011)

		await test_lcd_data(dut, 0, 0b0011)
		await test_lcd_data(dut, 0, 0b0010)
		await test_lcd_data(dut, 0, 0b0000)
		await test_lcd_data(dut, 0, 0b1111)
		await test_lcd_data(dut, 0, 0b0000)
		await test_lcd_data(dut, 0, 0b0001)

		await test_lcd_string(dut, "Big thanks to Matt  ")
		for i in range(0, 2):
			await test_lcd_data(dut, 0, 0b01100)
			assert dut.LED1.value == 0
			await test_lcd_data(dut, 0, 0b0000)
		await test_lcd_string(dut, "Venn and TinyTapeout<3 <3 <3")
		for i in range(0, 89):
			await test_lcd_data(dut, 0, 0b0011)
		
		await test_lcd_data(dut, 0, 0b0011)
		assert dut.LED1.value == 1
		await test_lcd_data(dut, 0, 0b0010)
		await test_lcd_data(dut, 0, 0b0000)
		await test_lcd_data(dut, 0, 0b1111)
		await test_lcd_data(dut, 0, 0b0000)
		assert dut.LED1.value == 0
		await test_lcd_data(dut, 0, 0b0001)
		
		await test_lcd_string(dut, " Hi, I'm Tholin :3")
		assert dut.LED0.value == 0
		
		for i in range(0, 11):
			await test_lcd_data(dut, 0, 0b1101)
			await test_lcd_data(dut, 0, 0b0100)
		await test_lcd_string(dut, "www.tholin.dev   ")
		await test_lcd_data(dut, 1, 3)
		await test_lcd_data(dut, 1, (ef_0 + ef_1) & 1)
		await test_lcd_data(dut, 1, 3)
		await test_lcd_data(dut, 1, (ef_0 + ef_1) >> 1)
		for i in range(0, 154):
			await test_lcd_data(dut, 0, 0b0011)
			
		await test_lcd_data(dut, 0, 0b0011)
		await test_lcd_data(dut, 0, 0b0010)
		await test_lcd_data(dut, 0, 0b0000)
		await test_lcd_data(dut, 0, 0b1111)
		await test_lcd_data(dut, 0, 0b1100)
		await test_lcd_data(dut, 0, 0b0111)
		
		await test_lcd_string(dut, "Avali")
		for i in range(0, 28):
			await test_lcd_data(dut, 0, 0b0000)
			assert dut.LED1.value == 0
		for i in range(0, 2):
			await test_lcd_data(dut, 0, 0b1001)
			await test_lcd_data(dut, 0, 0b1000)
		await test_lcd_string(dut, "Software Dev")
		assert dut.LED0.value == 0
		for i in range(0, 28):
			await test_lcd_data(dut, 0, 0b0000)
		for i in range(0, 2):
			await test_lcd_data(dut, 0, 0b1100)
			await test_lcd_data(dut, 0, 0b0100)
		await test_lcd_string(dut, "Hardware Dev")
		for i in range(0, 28):
			await test_lcd_data(dut, 0, 0b0000)
		for i in range(0, 2):
			await test_lcd_data(dut, 0, 0b1001)
			await test_lcd_data(dut, 0, 0b0110)
		await test_lcd_string(dut, "VRC World Maker")
		for i in range(0, 66):
			await test_lcd_data(dut, 0, 0b0011)

		await test_lcd_data(dut, 0, 0b0011)
		assert dut.LED1.value == 1
		await test_lcd_data(dut, 0, 0b0010)
		await test_lcd_data(dut, 0, 0b0000)
		await test_lcd_data(dut, 0, 0b1111)
		await test_lcd_data(dut, 0, 0b0000)
		await test_lcd_data(dut, 0, 0b0001)

		await test_lcd_string(dut, "Big thanks to Matt  ")
		for i in range(0, 2):
			await test_lcd_data(dut, 0, 0b01100)
			await test_lcd_data(dut, 0, 0b0000)
		await test_lcd_string(dut, "Venn and TinyTapeout<3 <3 <3")
		for i in range(0, 89):
			await test_lcd_data(dut, 0, 0b0011)
