#include<iostream>
#include <string>
#include "cppbot.cpp"
  
using namespace std;

int main(){
	cout << "Hi there! Hope you would be fine!\n";
	cout << "I am your personal chatbot"<< endl;

cppbot newbot("db.dat");


while(true){


newbot.askquestion();
newbot.tolower();
newbot.searchanswer();
newbot.printanswer();


}


    return 0;
}