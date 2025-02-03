#if __has_include("page1_html.h")
#include "page1_html.h"
#include "style1_css.h"
#else
#error "Missing generated files! Please modify your platform.local.txt according to the example in this repo's scripts directory, then restart Arduino IDE!"
#endif

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println(page1_html);
  Serial.println(style1_css);

}

void loop() {
  // put your main code here, to run repeatedly:

}
