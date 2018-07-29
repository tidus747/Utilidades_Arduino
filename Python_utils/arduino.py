#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Ivan Rodriguez - 2018
'''
# Módulos y utilidades importadas
import serial


# Definición de la clase Arduino
class Arduino:
	"""Clase para gestionar la conexión de un arduino desde Python"""
	def __init__(self):
        self.serial = ''
        self.port = ''
        self.baudrate = ''
		self.err = ''
		return

    def conectar(self,port,baudrate):
        self.baudrate = baudrate
        self.port = port
        self.serial = serial.Serial(port, baudrate)
        return

    def desconectar(self):
        return

    def disponible(self):
        return

    def enviarDatos(self):
        return

    def recibirDatos(self):
        rawString = self.serial.readline()
        return

    def showInfo(self):
        return
