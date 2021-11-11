"""
Philips Hue lamp
----------------

Very important:

It seems that the device needs to be connected to in the official Philips Hue Bluetooth app
and reset from there to be able to use with Bleak-type of BLE software. After that one needs to
do a encrypted pairing to enable reading and writing of characteristics.

ONLY TESTED IN WINDOWS BACKEND AS OF YET!

References:

- https://www.reddit.com/r/Hue/comments/eq0y3y/philips_hue_bluetooth_developer_documentation/
- https://gist.github.com/shinyquagsire23/f7907fdf6b470200702e75a30135caf3
- https://github.com/Mic92/hue-ble-ctl/blob/master/hue-ble-ctl.py
- https://github.com/npaun/philble/blob/master/philble/client.py
- https://github.com/eb3095/hue-sync/blob/main/huelib/HueDevice.py

Created on 2020-01-13 by hbldh <henrik.blidh@nedomkull.com>

"""

import sys
import asyncio

from bleak import BleakClient

import asyncio
from bleak import BleakScanner


def bright(valin):
    async with BleakClient(address) as client:
        print("bright: "+ str(valin))
        print(f"Connected: {client.is_connected}")

        paired = await client.pair(protection_level=2)
        print(f"Paired: {paired}")
        await client.write_gatt_char(
                    BRIGHTNESS_CHARACTERISTIC,
                    bytearray(
                        [
                            valin,
                        ]
                    ),
                )

async def light_on():
    await client.write_gatt_char(LIGHT_CHARACTERISTIC, b"\x01")
    await asyncio.sleep(1.0)

async def light_off():
    await client.write_gatt_char(LIGHT_CHARACTERISTIC, b"\x00")
    await asyncio.sleep(1.0)

async def hue(colorin):
    color = convert_rgb(colorin)
    await client.write_gatt_char(COLOR_CHARACTERISTIC, color)
    await asyncio.sleep(1.0)


async def wrapper(command, argument):
    commandlist = []

    brightness = lambda a: bright(a)
    color = lambda a: hue(a)
    on = lambda a: light_on()
    off = lambda a: light_off()

    commandlist.append(brightness)
    commandlist.append(color)
    commandlist.append(on)
    commandlist.append(off)
    if argument!=None:
        asyncio.run(commandlist[command](argument))
    else:
        asyncio.run(commandlist[command])
