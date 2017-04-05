#include <Wire.h>

int pinDHL69 = 0;

float valorDHL = 0;
 
#define SLAVE_ADDRESS 0x04

void setup() {
  Serial.begin(9600);

  Wire.begin(SLAVE_ADDRESS);
  
  Wire.onRequest(sendData);
}

void read_moist() {
  Serial.println("Humedad Terra Sensor DHL69");  
  valorDHL = analogRead(pinDHL69) / 10;
  valorDHL = 100 - valorDHL;
  
  Serial.println("Sensor de Humedad valor: ");  
  Serial.print(valorDHL);  
  Serial.print(" %");
  
  if (valorDHL >= 70)  
     Serial.println(" Encharcado");  
  if ((valorDHL < 70) and (valorDHL > 30))  
      Serial.println(" Humedo, no regar");   
  if (valorDHL <= 30)  
      Serial.println(" Seco, necesitas regar");  
  delay(1000);   
}

// callback for sending data
void sendData(){
  Serial.println("I2C SEND");
  int data = valorDHL;
  Serial.println(data);
  Wire.write(data);
}

void loop() {
  delay(2000);
  
  read_moist();
}
