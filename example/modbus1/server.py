import yaml
import serial
import time
import io


def read_config():
    with open('config.yaml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        print(data)
        return data


def init_port(config):
    serial_port = serial.Serial(config["server_port"])
    print(serial_port)
    return serial_port


def main():
    config = read_config()
    serial_port = init_port(config)
    print("Start Server loop...")
    unicode_str = 'hello 世界\n'
    ascii_str = unicode_str.encode("utf-8")

    while True:
        serial_port.write(b'hello\n')
        serial_port.write(ascii_str)
        time.sleep(2)


if __name__ == "__main__":
    main()
