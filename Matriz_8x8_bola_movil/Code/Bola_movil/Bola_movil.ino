#include <LedControl.h>

#include <SPI.h>
#include <Wire.h>
#include <SparkFun_ADXL345.h> 

 
ADXL345 adxl = ADXL345();
LedControl lc=LedControl(12,11,10,1); 

// Definimos las variables globales de nuestro programa

int pos_x = 0;
int pos_y = 0;

void setup() 
{
   Serial.begin(9600);             
   Serial.println("Iniciar");
   Serial.println();
 
   adxl.powerOn();            
   adxl.setRangeSetting(16);       //Definir el rango, valores 2, 4, 8 o 16

   // El numero que colocamos como argumento de la funcion se refiere a la direccion del decodificador
  lc.shutdown(0,false);
  lc.setIntensity(0,8);// La valores estan entre 1 y 15 
  lc.clearDisplay(0);

  lc.setLed(0,pos_x,pos_y,true);
}
 
void loop() 
{
   //leer los valores e imprimirlos
   int x, y, z;
   adxl.readAccel(&x, &y, &z);  
   Serial.print(x);
   Serial.print(", ");
   Serial.print(y);
   Serial.print(", ");
   Serial.println(z); 

   if (( x > -20) && (pos_x < 7)){ // Recordemos que aunque la matriz tiene 8 posiciones, comenzamos a contar en 0
    lc.setLed(0,pos_x,pos_y,false);
    pos_x++;
    lc.setLed(0,pos_x,pos_y,true);
    }

   if (( x < -20) && (pos_x > 0)){ // Recordemos que aunque la matriz tiene 8 posiciones, comenzamos a contar en 0
    lc.setLed(0,pos_x,pos_y,false);
    pos_x--;
    lc.setLed(0,pos_x,pos_y,true);
    }

    if (( z < 34) && (pos_y < 7)){ // Recordemos que aunque la matriz tiene 8 posiciones, comenzamos a contar en 0
    lc.setLed(0,pos_x,pos_y,false);
    pos_y++;
    lc.setLed(0,pos_x,pos_y,true);
    }

    if (( z > 34) && (pos_y > 0)){ // Recordemos que aunque la matriz tiene 8 posiciones, comenzamos a contar en 0
    lc.setLed(0,pos_x,pos_y,false);
    pos_y--;
    lc.setLed(0,pos_x,pos_y,true);
    }


    
   delay(50);
}
