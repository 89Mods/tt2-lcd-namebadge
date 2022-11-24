![](../../workflows/gds/badge.svg) ![](../../workflows/docs/badge.svg) ![](../../workflows/tests/badge.svg)

# Character LCD test

TinyTapeout 2 submission. This is me experimenting with sending data to a character LCD in 4-bit mode. The actual design is relatively dumb, using a internal ROM of 124 7-bit words to hold some text to print out, though it does also use LCD commands for moving the cursor to improve the "presentation" of the text.
Also my first time using pure Verilog, instead of exporting a design from Logisim Evolution.

It’ll print my name and a link to my website, as well as a thank you to TinyTapeout.
The LED0 and LED1 outputs provide some blinkenlights. As a test, the EF0 - EF2 inputs influence part of the display. The circuit will add all three input values together, and display the result as a 2-bit binary number next to the link to my website.

I’ll probably be doing something a bit more interesting with a character LCD in a future submission.
