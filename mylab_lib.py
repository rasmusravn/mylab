#imports
import os

# parent class for all device-setup
class device:
    baudrate = 5800
    number_of_devices = 0

    def __init__(self,address,model) -> None:
        self.address = address
        self.model = model
        device.number_of_devices += 1

    @classmethod
    def get_number_of_devices(cls):
        return cls.number_of_devices

    @classmethod
    def add_number_of_devices(cls):
        cls.number_of_devices +=1

    def get_traces(self):
        pass

    def new_func():
        pass

#child class for oscilloscopes (parent:device)
class oscilloscope(device):
    def __init__(self, address, model) -> None:
        super().__init__(address, model)
        self.type = oscilloscope

    def get_trace(self):
        pass


# parent class for measurements

class measurement:

    def __init__(self) -> None:
        pass

    @staticmethod
    def find_s2p_in_path(path):
        for file in os.listdir(path):
            if file.endswith(".s2p"):
                print(os.path.join("\.data", file))


def main():
    measurement.find_s2p_in_path("./data")

if __name__ == "__main__":
    main()