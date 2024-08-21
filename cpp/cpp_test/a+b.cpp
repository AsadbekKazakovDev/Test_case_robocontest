#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
  ios_base::sync_with_stdio(0);cin.tie(NULL);cout.tie(NULL); // kiritish va chiqarish uchun katadigan vaqtni olib tashlaydi
    
    srand(time(0));// random time to'g'ri ishlashi uchun
  
  
  for(int i = 1; i <= 10; i ++){// 50ta file ochadi va yopadi
    string in="",out="";
    
    if(i < 10){
      in += "0" + to_string(i) + ".in";//yandexda kiruvchi file kengaytmasi yo'q . Robocontestda .in yozilish kk
      out += "0" + to_string(i) + ".out";//yandexda kiruvchi file kengaytmasi .a . Robocontestda .out yozilish kk
    }
    else{
      in += "" + to_string(i) + ".in";
      out += "" + to_string(i) + ".out";
    }
    ofstream input(in);
    ofstream output(out);
    int a, b;
    a = rand()%1000 + 1;//a sonini 1 va 1000 orasidan tasodifiy random aosida tanlaydi 
    b = rand()%1000 + 1;//b sonini 1 va 1000 orasidan tasodifiy random aosida tanlaydi 
    input << a << " " << b << endl;// bir qatorda ikkita sonni filega yozish uchun
    int s;
    s = a + b;// har doimgidek hisob kitoblar
    
  output << s;// natijani output filega yozadi
    
    input.close();
    output.close();
  }
}