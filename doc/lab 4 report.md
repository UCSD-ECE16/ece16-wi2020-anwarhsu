# ECE 16 Lab 4 report 
By: Anwar Hsu A15443752

Date: 02/13/2020

### Tutorial 

## MAX30105 Pulse Sensor:

> Q. Note that you can connect both the heart rate sensor and your OLED at the same time, both of which use the I2C SDA and SCL lines. Why does this work?

> A. The I2C protocol allows you to pick which slave device you want. Since we only have one SDA and SCL line we just need to wire each device SDA and SCL line in parallel. The SDA and SCL lines behave independtly. 

> Q. Notice the while(1) statement. What happens if the device is not connected? What happens if the error is printed and then you connect the device? Will the code proceed? Try it and describe the behavior.

> A. If the device is not connected it prints the error meesage "MAX30105 was not found. Please check wiring/power." If you try and connect the device after this error meassage, it wouldn't work because the while(1) statement is blocking from allowing other actions to happen. 

> Q. what would the settings look like if you were to: set the led brightness to 25mA, use only the Red + IR LED, Sample at 200Hz, and use an ADC range of 8192? 

> A. compared to the ledbirghtness 0x1F, it gets brighter as we increase the current, the voltage increases. We do't change the pulse width so having a faster sampleRate and higher ADC wouldn't have any effect becuase higher DC and sampling rate effect resoltuion rather than brightness. 

> Q. What are the units of the pulse width? Would the bigger the pulseWidth result in a more intense or less intense measurement? Why?

> A. The units of pulse width is the amount of time it takes to send each pulse signal(unit of seconds). the bigger pulseWidth would increase the intesity because the longer the voltage gets amplitfiled the brighter the led would be. 

> Q. How many bits are needed for an ADC range of 16384?

> A. 2^x = 16384. If we take log base two into a calculator, we get 14 bits. Therefore we need a 14 bit ADC. 

> Q. What is the peak wavelength of the R, IR, and G LEDs?

> A. For red its 670nm, IR is 900nm and Green is 545nm 

> Q. If you want to read the Green value, what Mode do you need the setting to be in and what function will you need to use to get the green signal?

> A. I need to be in mode 3 as it inclues RE+ IR + Green led. Instead of the getIR function, I would use getGreen instead. 

## Matplotlib

> Q. What was plotted? What does this tell you about how plt.plot interprets the input? Remember that a = [1, 2, 3, 4 ]
                                [1, 4, 9,16]

> A. The first array of [1,2,3,4] is the initale points as showed by the red line starting at 4 green at 3, orange at 2, blue at 1. The second array[1,4,9,16] plots the next point when x gets incremented by one and plots the y axis(as shown below). 
>![Image of two_array](images4/two_array.JPG)

> Q. Try your best to replicate the above plot by shaking your accelerometer. The above was sampled at 50Hz for 10 seconds. Make a gif of you running your program, shaking your accelerometer, and a plot showing up similar to the one above.

> A. ![Image of two_array](videos4/tutorial_graph.gif)


> Q. What is approximately the frequency of oscillation of the x axis signal in the plot above? 

> A. There about 4 cycles in the time frame around 2 seconds. Period would be 2 / 4 = .5 seconds. Frequency of oscillation would be 1/.5 = 2hz 

## Removing Mean Offset 

### Challenges

## Challenge 1:
> Q. Why do we plot the negative of the signal? This has to do with light absorption. We talked about it in class. 

> A. Since there is blood, it blocks the light, therefire there is less light. 

> Q. Try different sampleAverage parameters and plot them. What is the effect of sampleAverage on the smoothness of the signal? 

> A. As we increase the sampleAverage, we get less noise and a better image of what is expected. As we we can see the as we increase the n to around 20, it looks more like a heart rate reading that is expect vs the n = 5 which looks off. 
>
> Sample: n = 5
> ![Image of sample_5](images4/sample_5.JPG)
>
> Sample: n = 10
>![Image of sample_10](images4/sample_10.JPG)
>
> Sample: n = 20
>![Image of sample_20](images4/sample_20.JPG)