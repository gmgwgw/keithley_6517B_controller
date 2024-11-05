import pyvisa
import time

class Keithley6517B:
    def __init__(self, inst: pyvisa.resources.Resource):
        self.inst = inst

    def get_idn(self) -> str:
        # *IDN?: return the identification string of the instrument
        idn = self.inst.query("*IDN?")
        return idn

    def internal_test(self) -> str:
        # *TST?: runs self test of the instrument and reads the result
        tst = self.inst.query("*TST?")
        return tst

    def reset(self):
        # *RST: resets the instrument
        self.inst.write("*RST")
        # *CLS: clears the event registers and queues
        self.inst.write("*CLS")
        return

    def conf_stat_model(self):
        # STAT:MEAS:ENAB:
        self.inst.write("STAT:MEAS:ENAB 512")
        # *SRE: sets or clears the bits of the service request enabe register
        # 1: Set MSB(most significant bit) (bit 0)
        self.inst.write("*SRE 1")

    def close_channel(self, ch_num: int):
        """close channel of 6522 scan card.

        Args:
            ch_num (int): number of the channel to be closed.
        """
        self.inst.write("ROUT:CLOS {}".format(ch_num))
        cros = self.inst.query("ROUT:CLOS?")
        return cros

    def set_func_and_range(self, func: str, urim: str):
        """set measuring mode and range

        Args:
            func (str): measuring mode to be set (e.g. CURR)
            urim (str): the upper limit for the measurement
        """

        self.inst.write(":SENS:FUNC '{}'".format(func))
        self.inst.write(":SENS:CURR:RANG AUTO")
        return

    def conf_staircase_sweep(
        self, star: float, stop: float, step: float, stim: float
    ) -> str:
        self.inst.write(":TSEQ:TYPE STSW")
        self.inst.write(":TSEQ:STSW:STAR {}".format(star))
        self.inst.write(":TSEQ:STSW:STOP {}".format(stop))
        self.inst.write(":TSEQ:STSW:STEP {}".format(step))
        # STIM: step time, the delay between steps
        self.inst.write(":TSEQ:STSW:STIM {}".format(stim))
        # TSO: selects the control source that starts the test sequence
        # IMM: immediate control source
        self.inst.write(":TSEQ:TSO IMM")
        # *OPC?: returns 1 after all pending operations are completed
        opc = self.inst.query("*OPC?")
        return opc

    def run_staircase_sweep(self):
        # :TSEQ:ARM: arms the selected test sequence
        self.inst.write(":TSEQ:ARM")
        time.sleep(1)
        self.inst.write("*TRG")
        try:
            self.inst.wait_for_srq(timeout=None)
        except KeyboardInterrupt:
            print("interrupted")
        return

    def trace_data(self) -> str:
        # TRACE:DATA?: reads all readings in the buffer
        data = self.inst.query("TRACE:DATA?")
        return data


if __name__ == "__main__":
    rm = pyvisa.ResourceManager()
    visa_tuple = rm.list_resources()
    inst = rm.open_resource(visa_tuple[0])

    keithley = Keithley6517B(inst)

    print(keithley.get_idn())

    print(keithley.internal_test())

    keithley.conf_stat_model()

    print(keithley.close_channel(0))

    keithley.set_func_and_range("CURR", 1e-6)
    # minimum step size is 5 mV
    keithley.conf_staircase_sweep(0, -0.5, 0.005, 1)

    keithley.run_staircase_sweep()

    print(keithley.trace_data())

    # TODO: プロット機能の実装
    # TODO: エラー処理
    # TODO: ログ出力
