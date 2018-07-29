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
        self.port = ''
		self.err = ''
		return

    def conectar(self):
        return

    def desconectar(self):
        return

    def disponible(self):
        return

    def show_info(self):
        return

	def parametros(self):
		self.h = self.image_h*self.tam_pix/self.tam_cuadrado
		self.w = self.image_w*self.tam_pix/self.tam_cuadrado
		self.focal = np.mean((self.mtx[0,0],self.mtx[1,1]))*self.tam_pix/self.tam_cuadrado
		return
