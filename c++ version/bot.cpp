#include "bot.h"
#include <stdlib.h> 
#include<iostream>
#include <string>
#include <fstream>
#include <vector> 
#include <algorithm>







using  namespace std;




vector<string> notfound={"I don't know"};





void tokenize(string const &str, const char delim, vector<string> &out)
{
	size_t start;
	size_t end = 0;

	while ((start = str.find_first_not_of(delim, end)) != string::npos)
	{
		end = str.find(delim, start);
		out.push_back(str.substr(start, end - start));
	}
}





int getrand(int high){
int low=0;
 return ((rand() % (high-low + 1))+low);
}




void remove_duplicates(vector<string>& vec)
{
  sort(vec.begin(), vec.end());
  vec.erase(unique(vec.begin(), vec.end()), vec.end());
}






void LowerCase(string & str){
	int len = str.length();

	for( int i = 0; i < len; i++ ) 
	{
		if ( str[i] >= 'A' && str[i] <= 'Z' ) 
		{
			str[i] -= 'A' - 'a';
		}
	}
}



















bot::bot(){}


bot::bot(string dbname){

   bot::dbfname=dbname;
}





void bot::setup(){
cout<<"Initializing "<<"Bot"<<"\n";
}



void bot::askquestion(){
cout<<"\nYou: ";
getline(cin,bot::question);
}

void bot::tolower(){
LowerCase(bot::question);
}




void bot::searchanswer(){


string myques=bot::question;

string qdb, ansdb;

ifstream db(bot::dbfname);


while(!db.eof()){


    getline(db,qdb);
    getline(db,ansdb);


    vector<string> qvect;
    vector<string> ansvect;
    vector<string> myqvect;

	tokenize(qdb,'|', qvect);
    tokenize(ansdb,'|', ansvect);
    tokenize(myques,' ', myqvect);

remove_duplicates(myqvect);

        for (auto &adbques: qvect) {


vector<string> qwordsmatchvect;

tokenize(adbques,'&', qwordsmatchvect);


                int matched=0;

                for (auto &awordmatching: qwordsmatchvect) {

            for (auto &amyques: myqvect) {


                if(amyques==awordmatching){
                    matched++;
                }

                if(matched>=qwordsmatchvect.size()){

                    db.close();
                    bot::answer=ansvect[getrand(ansvect.size()-1)];
                    
                    return ;
                }
                
            }

                }

        }

    }//end  while eof


db.close();



bot::answer=notfound[getrand(notfound.size()-1)];
    return ;

}


 void bot::printanswer(){
     cout<<"Bot "<<": "<<bot::answer<<endl;
 }

string bot::returnanswer(){
    return  bot::answer;
 }










