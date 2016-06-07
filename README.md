# Tc3_PcSpeaker

PC Speaker TwinCAT 3 Library for x86 based PLCs. Demo player included. Project based on Beckhoff's [IOPortWrite Example](https://infosys.beckhoff.com/content/1033/tcplclibsystem/html/tcplclibsys_f_ioportwrite.htm) and "PC INTERN 2.0", ISBN 3-89011-331-1, Data Becker.

- Tc3_PcSpeaker - the library.
- PcSpeaker_Player - demo ~~music~~ beep player with two melodies (Imperial March and Mario Theme).


## Installation of the library

TwinCAT 3.1 must be installed.

1. Right click "References" then choose "Library Repository...".
2. Press "Install..." button then choose "bin/Tc3_PcSpeaker.compiled-library".
3. After that you can find and add reference to the library under the "System" category.


## Examples

```pascal
FUNCTION_BLOCK FB_PcSpeaker
VAR_INPUT
    Freq	: DWORD	:= 10000;	// Frequency [Hz]
    Length	: TIME	:= T#500MS;	// Tone duration
    Delay	: TIME	:= T#0MS;	// Delay after the tone
    Execute	: BOOL;				// Rising edge starts function block execution
END_VAR
```


## Notes on demo player

You can link MAIN.START and MAIN.STOP variables with hardware inputs (or buttons) to start|stop playing music. Or may use that variables under the debug mode.


### Midi converter

Util folder contains necessary utilities that should help you convert .midi files into the TcGVL header files. Just drag'n'drop your .midi file on the convert.cmd. Python must be installed.

- Midicsv http://www.fourmilab.ch/webtools/midicsv/
- midi-to-beep https://github.com/dandroid88/midi-to-beep