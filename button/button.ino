/* --- Spyderbot button ---

You will need the RedBear's Device ID and the Access Token. These are accessible as environment variables on the Pi

REDBEAR_DEVICE_ID
REDBEAR_ACCESS_TOKEN

Query the status of this button by running the following command:

curl "https://api.particle.io/v1/devices/REDBEAR_DEVICE_ID/spyderbutton?access_token=REDBEAR_ACCESS_TOKEN"

*/

const int onboardLED = D7;
const int buttonLED = D0;
const int buttonPin = D1;
boolean LED_on = false;
byte current_button = LOW;
byte old_button = LOW;

int buttonStatus = 0;


void setup () {
    Serial.begin(9600);
    pinMode(onboardLED, OUTPUT);
    pinMode(buttonLED, OUTPUT);
    pinMode(buttonPin, INPUT);
    Particle.variable("spyderbutton", &buttonStatus, INT);
    }


void blink () {
    digitalWrite(onboardLED,HIGH);
    delay(500);
    digitalWrite(onboardLED,LOW);
    delay(500);
}


byte simple_read_button(byte pin)
{
  byte current_button = digitalRead(pin);
  return(current_button);
}

byte read_button(byte pin, byte ref_value)
{
  byte current_button = digitalRead(pin);
  if (((ref_value == LOW)
       && (current_button == HIGH))
      || ((ref_value == HIGH)
          && (current_button == LOW)))
  {
    delay(100);
    current_button = digitalRead(pin);
  }
  return(current_button);
}


void loop()
{
  current_button = read_button(buttonPin, old_button);
  if ((old_button == LOW) && (current_button == HIGH))
    {
      LED_on = !LED_on;
    }
  old_button = current_button;

  if (LED_on == true)
  {
    digitalWrite(buttonLED, HIGH);
    Serial.println("Button Turned On");
    buttonStatus = 1;
  }
  else
  {
    digitalWrite(buttonLED, LOW);
    Serial.println("Button Turned Off");
    buttonStatus = 0;
  }
}
