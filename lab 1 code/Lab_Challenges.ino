


void setup() {
  // put your setup code here, to run once:
  setupLED();
  setupButton();
  setupMessage();

}

void Lab1_C2(){
  
  
  if(getButton() == LOW){
    //add one second to the timer
    addTimer();
    delay(100);
  }
  else {
    runTimer();
  }
}


void loop() {
  // put your main code here, to run repeatedly:
  //condition1();
  //condition2();
  //condition3();
  //condition4();
  //condition5();
  //condition6();
  Lab1_C2(); //call the Lab1 Challenge function
  
            



  

}
