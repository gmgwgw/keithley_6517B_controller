import pyvisa

rm = pyvisa.ResourceManager()
visa_tuple = rm.list_resources()
inst = rm.open_resource(visa_tuple[0])

# 機器の情報を取得
inst.write("*IDN?")
out_1 = inst.read()
print("IDN: ", out_1)

# リセット
inst.write("*RST")
print("RST")
