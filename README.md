# lib8relay

Python library for [Sequent Microsystems](https://sequentmicrosystems.com) 8-RELAY card.

## Overview

With lib8relay you can: 
 
 - Write one relay state.
 - Write all 8 relays state (on the same card) at one time.
 - Read one relay state
 - Read all 8 relays state (on the same card) at one time.
 
 
## Install 

To download lib8relay, either fork this github repo or simply use Pypi via pip.

```bash
$ pip install lib8relay
```

## Usage 

Now you can import the lib8relay library and use its functions. To test, read relays status from the board with stack level 0:

```bash
~$ python
Python 2.7.9 (default, Sep 17 2016, 20:26:04)
[GCC 4.9.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import lib8relay
>>> lib8relay.get_all(0)
0
>>>
```

## Functions

### set(stack, relay, value)
Set one relay state.

stack - stack level of the 8-Relay card (selectable from address jumpers [0..7])

relay - relay number (id) [1..8]

value - relay state 1: turn ON, 0: turn OFF[0..1]


### set_all(stack, value)
Set all relays state.

stack - stack level of the 8-Relay card (selectable from address jumpers [0..7])

value - 8 bit value of all relays (ex: 255: turn on all relays, 0: turn off all relays, 1:turn on relay #1 and off the rest)

### get(stack, relay)
Get one relay state.

stack - stack level of the 8-Relay card (selectable from address jumpers [0..7])

relay - relay number (id) [1..8]

return 0 == relay off; 1 - relay on

### get_all(stack)
Return the state of all relays.

stack - stack level of the 8-Relay card (selectable from address jumpers [0..7])

return - [0..255]
