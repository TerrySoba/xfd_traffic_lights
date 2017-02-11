from subprocess import check_output


class TrafficLights:
    def __init__(self, clewarecontrolPath, serialNumber):
        """
        :param clewarecontrolPath: Path to the clewarecontrol executable. You can get this at https://www.vanheusden.com/clewarecontrol/
        :param serialNumber: The serial number of the device
        """
        self._serialNumber = serialNumber
        self._clewarecontrolPath = clewarecontrolPath

    def setLights(self, red, yellow, green):
        """
        Sets the traffic lights to the given state.

        :param serial: The serial number of the device
        :param red: If True, red light will be enabled. Otherwise it will be disabled.
        :param yellow: If True, yellow light will be enabled. Otherwise it will be disabled.
        :param green: If True, green light will be enabled. Otherwise it will be disabled.
        """
        redState = "1" if red else "0"
        yellowState = "1" if yellow else "0"
        greenState = "1" if green else "0"

        commandLine = [self._clewarecontrolPath, '-c', '1', '-d', self._serialNumber, '-as', '0', redState, '-as', '1', yellowState, '-as', '2', greenState]

        output = check_output(commandLine)


if __name__ == "__main__":
    # execute only if run as a script
    traffic = TrafficLights("clewarecontrol", "902971")
    traffic.setLights(False, False, False)
    pass

