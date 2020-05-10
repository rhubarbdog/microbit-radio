from microbit import *
import make_radio

radio = make_radio.MakeRadio(group=1)
radio.off()
radio.on()

while True:

    if button_a.is_pressed():
        radio.send_number(99.9)
        display.scroll('{99.9}')
    elif button_b.is_pressed():
        name = 'abcdefghi'
        number = 77
        radio.send_value(name,number)
        display.scroll('{' + name + '=' + str(number) + '}')
    elif pin8.read_digital():
        name = 'abcdefghijklm'
        number = -77.7
        radio.send_value(name,number)
        display.scroll('{' + name + '=' + str(number) + '}')
    elif pin16.read_digital():
        msg = 'abcdefghijklmonpqrst'
        radio.send_string(msg)
        display.scroll('{' + msg + '}')
    else:
        data = radio.receive_packet()
        if data is None:
            display.show('+')
        else:
            if type(data) is int or type(data) is float:
                display.scroll('[' + str(data) + ']')
            elif type(data) is str:
                display.scroll('[' + data + ']')
            else:
                label,value = data
                display.scroll( '[' + label +  '=' + str(value) + ']')
            

    sleep(100)
