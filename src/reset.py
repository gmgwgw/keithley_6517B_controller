import pyvisa

rm = pyvisa.ResourceManager()
inst = rm.open_resource("GPIB0::27::INSTR")

# 機器の情報を取得
inst.write("*IDN?")
out_1 = inst.read()
print("IDN: ", out_1)

# リセット
inst.write("*RST")
print("RST")
