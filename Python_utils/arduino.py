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
import os
import sys


# Definición de la clase Arduino
class Arduino:
	"""Clase para gestionar la conexión de un arduino desde Python"""
	def __init__(self):
        self.serial = serial.Serial()
        self.port = ''
        self.baudrate = ''
		self.err = ''
		return

    def conectar(self,port,baudrate):

        if (self.serial.isOpen()):
            conectionCheck = False
            print("La conexión serial ya se encontraba abierta, cierrela antes")
        else:
            self.serial.port = port
            self.serial.baudrate = baudrate
            self.serial.open()

        if (self.serial.isOpen()):
            conectionCheck = True
            print("La conexión serial se ha realizado correctamente")
            self.baudrate = baudrate
            self.port = port
        else:
            conectionCheck = False
            print("La conexión serial no ha sido posible")

        return conectionCheck

    def desconectar(self):
        if (self.serial.isOpen()):
            self.serial.close()
            self.port = ''
            self.baudrate = ''
            print("La conexión serial se ha cerrado correctamente")
            disconectionCheck = True
        else:
            self.port = ''
            self.baudrate = ''
            print("No hay una conexión serial que cerrar")
            disconectionCheck = True
        return disconectionCheck

    def disponible(self):
        return

    def enviarDatos(self):
        return

    def recibirDatos(self):
        rawString = self.serial.readline()
        return

    def showInfo(self):
        return
