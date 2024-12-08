import pyvisa
import time
import numpy as np


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
        return

    def close_channel(self, ch_num: int):
        """close channel of 6522 scan card.

        Args:
            ch_num (int): number of the channel to be closed.
        """
        self.inst.write("ROUT:CLOS (@{})".format(ch_num))
        cros = self.inst.query("ROUT:CLOS:STAT?")
        return cros

    def set_func_and_range(self, nplc):
        """set measuring mode and range

        Args:
            func (str): measuring mode to be set (e.g. CURR)
            urim (str): the upper limit for the measurement
        """

        self.inst.write(":SENS:FUNC 'CURR'")
        self.inst.write("SENS:CURR:NPLC {}".format(nplc))
        self.inst.write(":SENS:CURR:RANG:AUTO 1")

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
        opc = self.inst.query("*OPC?")
        print("OPC", opc)
        return

    def run_staircase_sweep(self):
        # :TSEQ:ARM: arms the selected test sequence
        self.inst.write(":TSEQ:ARM")
        return

    def run_bi_staircase_sweep(
        self, start: float, end: float, step: int, delay: float
    ):
        voltages_forward = np.arange(start, stop, step)
        voltages_backward = np.arange(stop, start, -step)
        voltages = np.concatenate(voltages_forward, voltages_backward)
        meas_results = []

        self.inst.write("*CLS")
        for v in voltages:
            # apply voltage
            self.inst.write()
            time.sleep(delay)
            # measure current
            res = self.inst.write(":MEAS:CURR:DC?")
            print(res)
            # meas_results.append(res)
            time.sleep(0.1)
        # with open(out_path, 'w') as f:
        #     f.write(meas_results)

    def trace_data(self) -> str:
        # TRACE:DATA?: reads all readings in the buffer
        data = self.inst.query("TRACE:DATA?")
        return data
