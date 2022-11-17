import yaml
import minimalmodbus
import time


def read_config():
    with open('config.yaml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        print(data)
        return data


def init_port(config):
    serial_port = minimalmodbus.Instrument(config["server_port"], config["client_id"])
    serial_port.serial.timeout = 0.5
    print(serial_port)
    return serial_port


def main():
    config = read_config()
    serial_port = init_port(config)
    print("Start Server loop...")

    while True:
        temperature = serial_port.read_register(0x14, 1)  # Register number, number of decimals
        print("Read value from slave: ", temperature)

        time.sleep(2)


if __name__ == "__main__":
    main()
