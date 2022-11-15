![](../../workflows/gds/badge.svg) ![](../../workflows/docs/badge.svg) ![](../../workflows/tests/badge.svg)

# Character LCD test

TinyTapeout 2 submission. This is me experimenting with sending data to a character LCD in 4-bit mode. The actual design is relatively dumb, using a internal ROM of 76 7-bit words to hold some text to print out, though it does also use LCD commands for moving the cursor to improve the "presentation" of the text.
Also my first time using pure Verilog, instead of exporting a design from Logisim Evolution.

It’ll print my name and a link to my website. Will probably do something a bit more interesting with a character LCD in a future submission.
