<h1>Micropython-MakeCode compatible Radio</h1>
</br>
</br>
Class `make_radio` includes all the functionality of the Micropyhton `radio`
module, while being compatible with MakeCode blocks. When you instansiate the
`make_radio` all the parameters of `radio.config` are available which make
sense. Whilst keeping the radio configured to work between Micropython and
MakeCode. The radio can be switched `.on()` and `.off()` with those methods.
You can send a number (integer or float) with method `.send_number(number)`.
Send a value pair (a string with a number) with method
`.send_value(value, number)`. Or just send a string with the
`.send_string(message)` method. Unlike MakeCode blocks with which in a single
program you can only accept one of a number, value pair or a string.
Micropython provides the convenient `.receive_packet()` method. The return
values are:
<list>
<li>None - no data was read or the packet was of an unspecified type</li>
<li>a string - A message was received</li>
<li>a tuple - A value pair was received</li>
<li>an int or a float - A number was received</li>
</list>
</br>
if required use the python function `type` to determine the packet type.
</br>
<h2>Some MakeCode Test Programs</h2>
<a href="https://makecode.microbit.org/_JCJhjaP5dUzv">Blocks radio producer
</a></br>
<a href="https://makecode.microbit.org/_AHjL8LDmdFLU">Blocks radio consumer
(receive messages)</a>
</br>
<a href="https://makecode.microbit.org/_EVELdi6iFhcu">Blocks radio consumer
(receive values)</a>
</br>
<a href="https://makecode.microbit.org/_R6gLJJHpDeUY">Blocks radio consumer
(receive numbers)</a>
</br>
