//Made by chkrr00k
//load on arduino

void setup() {
  Serial.begin(9600);
  analogReference(INTERNAL);
}

void loop() {
  int analog = analogRead(A0);
  Serial.println(analog);
  delay(100);
}
