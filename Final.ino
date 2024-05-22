const int buzzer = 4;

void setup() {
  Serial.begin(9600);
  pinMode(9, OUTPUT); // LED 1
  pinMode(8, OUTPUT); // LED 2
  pinMode(7, OUTPUT); // LED 3
  pinMode(6, OUTPUT); // LED 4
  pinMode(5, OUTPUT); // LED 5
  pinMode(buzzer, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    char data = Serial.read();

    if (data == 'A') {
      digitalWrite(9, HIGH); // LED 1 on
      digitalWrite(8, LOW);
      digitalWrite(7, LOW);
      digitalWrite(6, LOW);
      digitalWrite(5, LOW);
      noTone(buzzer);
      delay(500);
      turnOffLEDs();
    } else if (data == 'B') {
      digitalWrite(9, LOW);
      digitalWrite(8, HIGH); // LED 2 on
      digitalWrite(7, LOW);
      digitalWrite(6, LOW);
      digitalWrite(5, LOW);
      noTone(buzzer);
      delay(500);
      turnOffLEDs();
    } else if (data == 'C') {
      digitalWrite(9, LOW);
      digitalWrite(8, LOW);
      digitalWrite(7, HIGH); // LED 3 on
      digitalWrite(6, LOW);
      digitalWrite(5, LOW);
      noTone(buzzer);
      delay(500);
      turnOffLEDs();
    } else if (data == 'D') {
      digitalWrite(9, LOW);
      digitalWrite(8, LOW);
      digitalWrite(7, LOW);
      digitalWrite(6, HIGH); // LED 4 on
      digitalWrite(5, LOW);
      noTone(buzzer);
      delay(500);
      turnOffLEDs();
    } else if (data == 'E') {
      digitalWrite(9, HIGH); // All LEDs on
      digitalWrite(8, HIGH);
      digitalWrite(7, HIGH);
      digitalWrite(6, HIGH);
      digitalWrite(5, HIGH);
      tone(buzzer, 1000); // Send 1KHz sound signal...
      delay(500);       // ...for 2 seconds
      noTone(buzzer);    // Stop sound
      turnOffLEDs();
    } else if (data == 'F') {
      digitalWrite(9, LOW);
      digitalWrite(8, LOW);
      digitalWrite(7, LOW);
      digitalWrite(6, LOW);
      digitalWrite(5, HIGH); // LED 5 on
      noTone(buzzer);
      delay(500);
      turnOffLEDs();
    } else {
      turnOffLEDs();
    }
  }
}

void turnOffLEDs() {
  digitalWrite(9, LOW);
  digitalWrite(8, LOW);
  digitalWrite(7, LOW);
  digitalWrite(6, LOW);
  digitalWrite(5, LOW);
  noTone(buzzer);
}
