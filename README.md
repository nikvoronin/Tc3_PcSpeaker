# Tc3_PcSpeaker

PC Speaker TwinCAT 3 Library for x86 based PLCs. Demo player included. Project based on Beckhoff's [IOPortWrite Example](https://infosys.beckhoff.com/content/1033/tcplclibsystem/html/tcplclibsys_f_ioportwrite.htm) and "PC INTERN 2.0", ISBN 3-89011-331-1, Data Becker.

- Tc3_PcSpeaker - Library.
- PcSpeaker_Player - demo ~~music~~ beep player with two melodies (Imperial March and Mario Theme).


## Installation of the library

TwinCAT 3.1 must be installed.

1. Right click "References" then choose "Library Repository...".
2. Press "Install..." button then choose "bin/Tc3_PcSpeaker.compiled-library".
3. After that you can find and add reference to the library under the "System" category.


## Examples

```delphi
FUNCTION_BLOCK FB_PcSpeaker
VAR_INPUT
    Freq	: DWORD	:= 10000;	// Frequency [Hz]
    Length	: TIME	:= T#500MS;	// Tone duration
    Delay	: TIME	:= T#0MS;	// Delay after the tone
    Execute	: BOOL;				// Rising edge starts function block execution
END_VAR
```


## Notes on the demo player

You can link MAIN.START and MAIN.STOP variables with hardware inputs (or buttons) to start|stop playing music. Or may use that variables under the debug mode.