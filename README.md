<h1>Micropython-MakeCode compatible Radio</h1>
</br>
Class <code>make_radio</code> includes all the functionality of the
Micropyhton <code>radio</code> module, while being compatible with MakeCode
blocks. When you instansiate the <code>make_radio</code> all the parameters
of <code>radio.config</code> are available which make sense. Whilst keeping
the radio configured to work between Micropython and MakeCode. The radio can
be switched <code>.on()</code> and <code>.off()</code> with those methods. You
can send a number (integer or float) with method <code>.send_number(number)
</code>.
Send a value pair (a string with a number) with method
<code>.send_value(value, number)</code>. Or just send a string with the
<code>.send_string(message)</code> method. Unlike MakeCode blocks with which
in a single program you can only accept one of a number, value pair or a
string. Micropython provides the convenient <code>.receive_packet()</code>
method. The return values are:
<list>
<li>None - no data was read or the packet was of an unspecified type</li>
<li>a string - A message was received</li>
<li>a tuple - A value pair was received</li>
<li>an int or a float - A number was received</li>
</list>
</br>
if required use the python function <code>type</code> to determine the packet
type.
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
<h2>Note</h2>
</br>
For this to work both Micropython <code>make_radio</code> and MakeCode blocks
radio must use the same <code>group</code>. You must include the block <code>
radio.setGroup()</code>