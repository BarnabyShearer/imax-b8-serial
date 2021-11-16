#! /usr/bin/env python3
"""Entrypoint."""

import sys

import serial  # type: ignore

from . import read


def main(port: str) -> None:  # pragma: no cover
    """Entrypoint."""
    for packet in read(serial.Serial(port=port, baudrate=9600)):
        for attr in dir(packet):
            if not attr.startswith("_"):
                print(attr, "=", packet[attr])


if __name__ == "__main__":  # pragma: no cover
    main(sys.argv[1])
