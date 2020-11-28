<h1 align="center">Enigma</h1>

Enigma is a cryptography app built based on the German Enigma machine from World
War 2. It features a full alphabet of printable ASCII characters and ten rotors
to pick from. Additionally, it has an optional typex mode that enables more
detailed encryption as added by the British.

## Instructions

To encode a message, select the desired rotors from the dropdown and configure
their starting position. Optionally, the plugboard can be re-configured as well.

Once this is done, enter the desired message in the input text box and press
encode. This will encode the message and output the result in the output text
box, where it can be copied and sent along.

To decode a message, set the machine to the same settings that were used when
the machine was originally encoded. Then enter the encoded message in the input
box and again press encode. The decoded message will appear below.

## Config

The default path for the config file is in `Documents/Enigma/enigma.ini`. It is
a plain text .ini file that can be edited directly, although this is not
recommended. At any point, the app can be configured to point to a different
.ini file using the **Open config** action. This is useful in the case of having
multiple profiles. 
