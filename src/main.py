import pyvisa

if __name__ == "__main__":
    rm = pyvisa.ResourceManager()
    visa_tuple = rm.list_resources()
    inst = rm.open_resource(visa_tuple[0])

    # 機器の情報を取得
    inst_1.write("*IDN?")
    out_1 = inst_1.read()
    print("IDN: ", out_1)

    # 機器の内部テストを実行
    inst_1.write("*TST?")
    out_2 = inst_1.read()
    print("TST: ", out_2)