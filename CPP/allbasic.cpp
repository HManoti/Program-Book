#include<iostream>
using namespace std;

void square(int side){
    cout<<"Perimeter of square is: "<<4*side<<endl;
    cout<<"Area of square is: "<<side*side<<endl;
}
void rectangle(int len, int breadth){
    cout<<"Perimeter of rectangle is: "<<(2*(len+breadth))<<endl;
    cout<<"Area of rectangle is: "<<len*breadth<<endl;
}
void circle(int rad){
    cout<<"Circumference of circle is: "<<2*3.14*rad<<endl;
    cout<<"Area of circle is: "<<3.14*rad*rad<<endl;
}
void rectangle(int base, int case){
        
}
int main(){
    int len, breadth;
    int side;
    int rad;
    
    cout<<"Enter the side of square: ";
    cin>>side;
    square(side);
    cout<<"\nEnter length and breadth of rectangle: ";
    cin>>len>>breadth;
    rectangle(len, breadth);
    cout<<"\nEnter the radius of circle: ";
    cin>>rad;
    circle (rad);
    
}

/*int main(){               //All possible subarray in the array
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    for(int i=0;i<n;i++){
        for(int j=i;j<n;j++){
            for(int k=i;k<=j;k++){
                cout<<arr[k]<<" ";
            }cout<<endl;
        }
    }
    return 0;
}

/*int main(){
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    for(int i= n-1;i>=0;i--){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    return 0;
}
/*int main()
{
    int month;
    cout<<"Enter the number: ";
    cin>>month;
    switch(month)
    {
        case 1 :cout<<"January";break;
        case 2 :cout<<"February";break;
        case 3 :cout<<"March";break;
        case 4 :cout<<"April";break;
        case 5 :cout<<"May";break;
        case 6 :cout<<"June";break;
        case 7 :cout<<"July";break;
        case 8 :cout<<"August";break;
        case 9 :cout<<"September";break;
        case 10:cout<<"October";break;
        case 11:cout<<"November";break;
        case 12:cout<<"December";break;
        default :cout<<"Invalid Number";
    }
    return 0;
}
/*int main()    Little Calculator
{
    int a,b;
    char op;
    cin>>a>>b>>op;
    switch(op)
    {
        case '+' : cout<<"The sum is "<<a+b;break;
        case '-' : cout<<"The diff is "<<a-b;break;
        case '*' : cout<<"The product is "<<a*b;break;
        case '/' : cout<<"The division is "<<a/b;break;
        case '%' : cout<<"The remainder is"<<a%b;break;
        default : cout<<"Invalid operator";
    }
    return 0;
}


/*int main()
{   
    int i,j;
    int row;
    int col;
    cout<<"Enter the number of rows: ";
    cin>>row;
    cout<<"Enter the number of column: ";
    cin>>col;
    for(i=1;i<=row;i++)
    {   
        for(j=1;j<=col;j++)
        cout<<" * ";
        cout<<endl;
    }
    return 0;
    
}
/*int lcs(string X, string Y, int m, int n) 
{ 
    if (m == 0 || n == 0) 
        return 0; 
    if (X[m - 1] == Y[n - 1]) 
        return 1 + lcs(X, Y, m - 1, n - 1); 
    else
        return max(lcs(X, Y, m, n - 1), 
                   lcs(X, Y, m - 1, n)); 
} 
  
int main() 
{ 
    string S1 = "Hitiksha";
    string S2 = "Suhani"; 
    int m = S1.size(); 
    int n = S2.size(); 
  
    cout << "Length of LCS is " << lcs(S1, S2, m, n); 
  
    return 0; 
}

/*int main()
{
    int a= 1; int b=99;
    int temp;
    cout<<"Before Swapping a="<<a<<"b="<<b<<endl;
    swap(a,b);
    cout<<"After Swapping a="<<a<<"b="<<b<<endl;
    return 0;
}
/*void merge(arr[], int[],) 
insertionSort(int arr[],int n)
{
    int i, key,j;
    for(i=1;i<n;i++){
        key= arr[i];
        j=i-1;
        while(j>=0 && arr[j]>key)
        {
            arr[j+1]=arr[j];
            j=j-1;
        }
        arr[j+1]=key;
    }
}
int main()
{
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++)
        cin>>arr[i];
    insertionSort(arr,n);
    for(int i=0;i<n;i++)
        cout<<arr[i]<<"";
    return 0;
}

// Function to solve the fainting Pokémon problem
/*int faintingPokemon(vector<int>& pokemons, int k) {
    int n = pokemons.size();
    vector<int> dp(n + 1, 0);

    for (int i = 1; i <= n; ++i) {
        dp[i] = dp[i - 1] + pokemons[i - 1];
        if (i >= k) {
            dp[i] -= pokemons[i - k];
        }
    }

    return *max_element(dp.begin(), dp.end());
}

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> pokemons(n);
    for (int i = 0; i < n; ++i) {
        cin >> pokemons[i];
    }
    int result = faintingPokemon(pokemons, k);
    cout << result << endl;
    return 0;
}

/*int main()
{
    int N;
    cin>>N;
    vector<int> arr(N);
    for(int i=0;i<N;i++)
        cin>>arr[i];
    int i =0;
    while(i<N-1 &&arr[i]<arr[i+1])//uphill
        i++;
    while(i<N-1 &&arr[i]==arr[i+1])//tophill
        i++;
    while(i<N-1 &&arr[i]>arr[i+1])//downhill
        i++;

    if(i==N-1)
        cout<<
    return 0;
}
/*int main()
{
    int l,b,c,d;
    int area, area_tile;
    int tile;
    cout<<"length of garden";
    cin>>l;
    cout<<"breadth of garden";
    cin>>b;
    cout<<"Area of garden=";
    cin>>area=l*b;

    tile= area/area_tile;
    cout<<"Number of tiles in the garden: ";
    cin>>tile;

    return 0;
}
/*int main()
{
    char N;
    cin>>N;
    switch(N)
    {
        case 'a' ...'z': cout<<"Small case...";break;
        case 'A' ...'Z': cout<<"Upper case...";break;
        
        default: cout<<"Something else...";
    }
    return 0;
}*/
// switch case in range (Range Declaration)