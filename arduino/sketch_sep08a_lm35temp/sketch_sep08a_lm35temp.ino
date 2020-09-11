int tempPin = 1;
 
boolean newData = false;

void setup()
{
  Serial.begin(9600);
  Serial.println("<Arduino ready>");
}
void loop()
{
  recvWithEndMarker();
  float cel = getTemperature(tempPin);
  if (newData == true) {
    Serial.println(cel);
    newData = false;
  }
}

float getTemperature(int tempPin) {
  int val = analogRead(tempPin);
  float mv = ( val/1024.0)*5000;
  float cel = mv/10;
  return cel;
}

void recvWithEndMarker() {
  // an array to store the received data
   const byte numChars = 4;
   char receivedChars[numChars];

   static byte ndx = 0;
   char endMarker = '\n';
    char rc;
   
    while (Serial.available() > 0 && newData == false) {
        rc = Serial.read();

        if (rc != endMarker) {
            receivedChars[ndx] = rc;
            ndx++;
            if (ndx >= numChars) {
                ndx = numChars - 1;
            }
        }
        else {
            receivedChars[ndx] = '\0'; // terminate the string
            ndx = 0;
            newData = true;
        }
    }
}


