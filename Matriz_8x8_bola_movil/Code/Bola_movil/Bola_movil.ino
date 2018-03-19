#include <LedControl.h>

#include <SPI.h>
#include <Wire.h>
#include <SparkFun_ADXL345.h> 

 
ADXL345 adxl = ADXL345();
LedControl lc=LedControl(12,11,10,1); 

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

   for (int row=0; row<8; row++)
  {
    for (int col=0; col<8; col++)
    {
      lc.setLed(0,col,row,true); // 
      delay(25);
    }
  }
 
  for (int row=0; row<8; row++)
  {
    for (int col=0; col<8; col++)
    {
      lc.setLed(0,col,row,false); // 
      delay(25);
    }
  }
  delay(1000);
}
