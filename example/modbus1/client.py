import yaml
import serial


def read_config():
    with open('config.yaml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        print(data)
        return data


def init_port(config):
    serial_port = serial.Serial(config["client_port"])
    print(serial_port)
    return serial_port


def main():
    config = read_config()
    serial_port = init_port(config)
    print("Start Client loop...")

    while True:
        line = serial_port.readline()
        line2 = serial_port.readline()

        print("Client read line: ", line)
        print("Client read line: ", line2.decode("utf-8"))


if __name__ == "__main__":
    main()
