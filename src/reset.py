import pyvisa

rm = pyvisa.ResourceManager()
visa_tuple = rm.list_resources()
print(visa_tuple)
usb_1 = visa_tuple[0]
inst_1 = rm.open_resource(usb_1)

# 機器の情報を取得
inst_1.write("*IDN?")
out_1 = inst_1.read()
print("IDN: ", out_1)

# 機器の内部テストを実行
inst_1.write("*TST?")
out_2 = inst_1.read()
print("TST: ", out_2)

# TODO: 電圧かける
# リセット
inst_1.write("*RST")
print("RST")
