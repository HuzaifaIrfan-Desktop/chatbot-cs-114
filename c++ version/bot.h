#include <string>

using  namespace std;


class bot{
    public:
     string botname="Bot";
    string dbfname="db.dat";
    string question;
    string answer;
    

    bot();
    bot(string dbname);
    void setup();
    void askquestion();
    void tolower();
    void searchanswer();
    void printanswer();
    string returnanswer();

};