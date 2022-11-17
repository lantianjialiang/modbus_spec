import time

import yaml
import serial
# import minimalmodbus


def read_config():
    with open('config.yaml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        print(data)
        return data


def init_port(config):
    serial_port = serial.Serial(config["client_port"])
    print(serial_port)
    return serial_port


def create_response(request):
    response = bytearray(7)
    # slave address
    response[0] = request[0]
    # function code
    response[1] = request[1]

    response[2] = 0x02
    response[3] = 0x03
    response[4] = 0xe8
    response[5] = 0xb8
    response[6] = 0xfa
    return bytes(response)


def main():
    config = read_config()
    serial_port = init_port(config)
    serial_port.reset_input_buffer()

    print("Start Client loop...")

    while True:
        # wait for first byte of data
        serial_port.timeout = None
        rx_raw = serial_port.read()

        # wait for next bytes of data until end of frame delay
        serial_port.timeout = config["client_timeout"]
        while True:
            rx_chunk = serial_port.read(256)  # assume the max length of one command is not bigger than that
            if not rx_chunk:
                break
            else:
                rx_raw += rx_chunk

        print("Client read line: ", rx_raw)
        # TODO check crc

        response = create_response(rx_raw)
        print("Give back: ", response)
        serial_port.write(response)
        time.sleep(1)


if __name__ == "__main__":
    main()
