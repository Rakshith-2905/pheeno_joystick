void Pheeno_Move(int speed , float theta) {

if (speed <0){

  speed = speed * (-1)
  int speed_r = (2*speed+theta*b)/(2*r);
  int speed_l = (2*speed-theta*b)/(2*r);
      speed_r = speed_r/r;
      speed_l = speed_l/r;
    my_robot.PIDMotorControlLR(speed_r);
    my_robot.PIDMotorControlRL(speed_l);
}
else
if(speed>0){
  int speed_r = (2*speed+theta*b)/(2*r);
  int speed_l = (2*speed-theta*b)/(2*r);
      speed_r = speed_r/r;
      speed_l = speed_l/r;
    my_robot.PIDMotorControlLR(speed_l);
    my_robot.PIDMotorControlRL(speed_r);
}


}
