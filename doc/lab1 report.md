# ECE 16 Lab 1 report 
By: Anwar Hsu A15443752

Date: 01/06/2020

## Tutorial:

> Q. What is the frequency of the blink rate in this example? Note that frequency is the inverse of the time it takes for a cycle. A cycle is the time it takes to go HIGH to LOW to HIGH again. Record a video of your FireBeetle blinking.  Make a note of the answer for now, in the next GIT tutorial, you will get a copy of a sample lab report.

> A. It takes 1.5 sec to make a cycle(period) go from HIGH to LOW to HIGH. If we take the inverse of the period we get the frequency, which will give us 2/3 hz or .66667 hz. 
>
![Image of challenge](images/blink_led.gif)

> Q. What is the limit for the GPIO? You can find this on the ESP32_WROOM datasheet: https://www.espressif.com/sites/default/files/documentation/esp32-wroom-32_datasheet_en.pdf . Look under IOH.

> A. The max current allowed for the input/output ports is 1,100mA
