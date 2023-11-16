import pyvisa as visa


class Oscilloscope:
    def __init__(self, ip: str) -> None:
        """ " Connect to instrument, create new Oscilloscope object"""
        self.rm = visa.ResourceManager()
        # self.inst = self.rm.open_resource(self.rm.list_resources()[0], read_termination='\n') # for testing purposes
        self.inst = self.rm.open_resource("TCPIP0::192.168.0." + str(ip) + "::INSTR")
        self.idn = self.inst.query("*IDN?")
        print("connection successful \n" + "IDN: \n" + self.idn + "\n\n")

    def autoscale(self) -> None:
        """ " Let the instrument set its parameters automatically"""
        self.inst.write("AUToscale")
        print("autosc")

    def get_channel_state(self, ch: int) -> int:
        """ " Check if channel is displayed"""
        return int(self.inst.query(":CHANnel" + str(ch) + ":DISPlay?"))

    def toggle_channel_state(self, ch: int) -> None:
        """ " Change whether channel is displayed or not"""
        self.inst.write(
            ":CHANnel" + str(ch) + ":DISPlay " + str(not self.get_channel_state(ch))
        )

    def get_vertical_amplification(self, ch: int) -> float:
        """ " Get vertical amplification value for given channel"""
        return float(self.inst.query(":CHANnel" + str(ch) + ":SCALe?"))

    def set_vertical_amplification(self, op: str, ch: int) -> None:
        """ " Set vertical amplification value for given channel
        up - increase amplification
        down - decrease amplification
        """
        if op == "up":
            self.inst.write(
                ":CHANnel"
                + str(ch)
                + ":SCALe "
                + str(self.get_vertical_amplification(ch) * 1.5)
            )
        elif op == "down":
            self.inst.write(
                ":CHANnel"
                + str(ch)
                + ":SCALe "
                + str(self.get_vertical_amplification(ch) / 1.5)
            )

    def get_vertical_offset(self, ch: int) -> float:
        return float(self.inst.query(":CHANnel" + str(ch) + ":OFFSet?"))

    def set_vertical_offset(self, op: str, ch: int) -> None:
        if op == "up":
            self.inst.write(
                ":CHANnel"
                + str(ch)
                + ":OFFSet "
                + str(self.get_vertical_offset(ch) * 1.5)
            )
        elif op == "down":
            self.inst.write(
                ":CHANnel"
                + str(ch)
                + ":OFFSet "
                + str(self.get_vertical_offset(ch) / 1.5)
            )

    def get_timebase(self) -> float:
        """ " Get timebase value"""
        return float(self.inst.query(":TIMebase:RANGe?"))

    def set_timebase(self, op: str) -> None:
        """ " Set timebase value
        right - decrease
        left - increase
        """
        if op == "left":
            self.inst.write(":TIMebase:RANGe " + str(self.get_timebase() * 2))
        elif op == "right":
            self.inst.write(":TIMebase:RANGe " + str(self.get_timebase() / 2))

    def get_horizontal_offset(self) -> float:
        """ " Get value of timebase offset"""
        return float(self.inst.query(":TIMebase:WINDow:POSition?"))

    def set_horizontal_offset(self, op: str) -> None:
        """ " Set value of timebase offset"""
        if op == "left":
            self.inst.write(
                ":TIMebase:WINDow:POSition " + str(self.get_horizontal_offset() / 1.5)
            )
        elif op == "right":
            self.inst.write(
                ":TIMebase:WINDow:POSition " + str(self.get_horizontal_offset() * 1.5)
            )

    def close(self) -> None:
        """ " Terminate connection with instrument"""
        self.inst.close()
