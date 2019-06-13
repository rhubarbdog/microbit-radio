# This work is loosley based on work by Barry Byford,
# https://github.com/ukBaz  the document I read
# https://ukbaz.github.io/howto/ubit_radio.html had a Creative Commons
# Attribution-ShareAlike 4.0 International License.
# (https://creativecommons.org/licenses/by-sa/4.0/)
#
# This piece of work has completed the psuedo-python and Barry Byford has
# given me his permission to license this code seperately in communication
# https://github.com/ukBaz/ukBaz.github.io/issues/29
#
# Author          - Phil Hall - https://github.com/rhubarbdog
#                 - Barry Byford - https://github.com/ukBaz 
# License         - MIT March 2019 - see file LICENSE in this repository
# First Published - 2019-03-22
#
# Modifications
# Phil Hall 
# 2018-12-20
#   1) Added broadcast rate and channel and others to radio.config
#   2) added endian to .to_bytes() method
#   3) changed some variable names
#   4) Added receive_packet method
#   5) Added support for packet type 4 float
#   6) Limit message length to 19
#   7) Limit send_value: name length to 8
#   8) Added support for packet type 5 value with float
#   9) Added on() and off() methods for completeness

import radio
import microbit
import ustruct

class MakeRadio:
    def __init__(self, group, power = 6, queue = 3):
        radio.config(group = group, data_rate = radio.RATE_1MBIT,\
                     channel = 7, power = power, queue = queue)
        radio.on()
        self.dal_header = b'\x01' + group.to_bytes(1, 'little') + b'\x01'

    def on(self):
        radio.on()

    def off(self):
        radio.off()
        
    def send_number(self, number):
        time_stamp = microbit.running_time().to_bytes(4, 'little')
        serial_num = int(0).to_bytes(4, 'little')
        if number <= 2147483647 and number >= -2147483648 and\
           type(number) is int:
            number_bytes = number.to_bytes(4, 'little')
            packet_type = int(0).to_bytes(1, 'little')
        else:
            number_bytes = ustruct.pack('<d',number)
            packet_type = int(4).to_bytes(1, 'little')

        raw_bytes = (self.dal_header +
                     packet_type +
                     time_stamp +
                     serial_num +
                     number_bytes)
        radio.send_bytes(raw_bytes)
     
    def send_value(self, name, value):
        if len(name) > 8:
            name = name[:8]
        time_stamp = microbit.running_time().to_bytes(4, 'little')
        serial_num = int(0).to_bytes(4, 'little')
        if value <= 2147483647 and value >= -2147483648 and\
           type(value) is int:
            number = int(value).to_bytes(4, 'little')
            packet_type = int(1).to_bytes(1, 'little')
        else:
            number = ustruct.pack('<d', value)
            packet_type = int(5).to_bytes(1, 'little')
            
        name_bytes = bytes(str(name), 'utf8')
        name_length = len(name_bytes).to_bytes(1, 'little')
        raw_bytes = (self.dal_header +
                     packet_type +
                     time_stamp +
                     serial_num +
                     number +
                     name_length +
                     name_bytes)
        radio.send_bytes(raw_bytes)
     
    def send_string(self, message):
        if len(message) > 19:
            message = message[:19]
        packet_type = int(2).to_bytes(1, 'little')
        time_stamp = microbit.running_time().to_bytes(4, 'little')
        serial_num = int(0).to_bytes(4, 'little')
        message_bytes = bytes(str(message), 'utf8')
        message_length = len(message_bytes).to_bytes(1, 'little')
        raw_bytes = (self.dal_header +
                     packet_type +
                     time_stamp +
                     serial_num +
                     message_length +
                     message_bytes)
        radio.send_bytes(raw_bytes)
     
    def receive_packet(self):
        data = radio.receive_bytes()
        return self._parse_packet(data)

    def _parse_packet(self, data):
        if data is None:
            return None

        if data[:3] != self.dal_header:
            pass
            #raise Exception('Bad header on this channel. ' + str(data[:3]))

        packet_type = int.from_bytes(data[3:4], 'little')

        if packet_type == 0: # number
            number = ustruct.unpack('<i', data[-4:])[0]
            return number
        elif packet_type == 1: # value
            value = ustruct.unpack('<i', data[12:16])[0]
            name = str(data[17:], 'utf8') 
            return (name, value)
        elif packet_type == 2: # string
            message = str(data[13:], 'utf8') 
            return message
        elif packet_type == 4: # floating point number
            float_ = ustruct.unpack('<d',data[-8:])[0]
            return float_
        elif packet_type == 5: # value with float
            float_ = ustruct.unpack('<d',data[12:20])[0]
            l = len(data)
            if l > 29:
                l = 29
            name = str(data[21:l], 'ascii') 
            return (name, float_)
        
        return None # raise Exception('Unknown packet type')

    def _sniff(self):
        data = radio.receive_bytes()

        if data is None:
            return None

        packet_type = int.from_bytes(data[3:4], 'little')
        packet_type = ustruct.unpack('<B', data[3:4])[0]
        print("packet id\t:",packet_type)
        time_stamp = int.from_bytes(data[4:8], 'little')
        print('time stamp\t:',time_stamp)
        serial = int.from_bytes(data[8:12], 'little')
        print('serial    \t:', serial)
        if packet_type == 0:
            number = ustruct.unpack('<i',data[-4:])
            print("number   \t:",number)
        if packet_type == 1:
            number = ustruct.unpack('<i',data[12:16])
            print("number   \t:",number)
        if packet_type == 4:
            print('decimal \t', ustruct.unpack('<d',data[-8:]))
        if packet_type == 5:
            print('decimal \t', ustruct.unpack('<d',data[12:20]))

        print("received\t:", self._parse_packet(data))
                
        return data
        
