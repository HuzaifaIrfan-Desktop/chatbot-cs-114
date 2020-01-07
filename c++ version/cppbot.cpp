#include "cppbot.h"

using  namespace std;


cppbot::cppbot(){}


cppbot::cppbot(string dbname){
   cppbot::dbfname=dbname;
}


 void cppbot::printanswer(){
     cout<<"cpp-bot "<<": "<<bot::answer<<endl;
 }