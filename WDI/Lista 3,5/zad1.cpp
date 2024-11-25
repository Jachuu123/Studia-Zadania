#include <iostream>
using namespace std;

int main()
{
    string a,b = "";

    cin >> a >> b;

    if (b.size() > a.size())
    {
        string pom = b;
        b = a;
        a = pom;
    }

    while(a.size() > b.size())
    {
        b = "0" + b;
    }

    //cout << a << endl << b << endl;

    string s = "";
    int carry = 0;

    for(int i = a.size()-1; i >= 0; i--)
    {
        int sum = (int(a[i]) - '0' + int(b[i]) - '0' ) + carry;
        //cout << int(a[i])-'0' << " " << int(b[i])-'0' << endl;

        if(sum == 2 || sum == 0)
            s += '0';
        else
            s += '1';
        if(sum >= 2)
            carry = 1;
        else
            carry = 0;
    }

    if (carry == 1)
        s = "1" + s;

    cout << s;


}
