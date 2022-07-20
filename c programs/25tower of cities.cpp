#include <bits/stdc++.h>
using namespace std;

// Function to count the number of tower
int number_of_tower(int c[], int r, int n)
{
    int numOfTower = 0;
    if(r == 0){
        numOfTower = n;
    }
    else{
        sort(c, c + n);
        long long t;
        t = c[0] + (2*r);
        int x=0;
        while(c[n-1] != -1){
            int j= x;
            while(c[j] <= t){
                c[j] = -1;
                j++;
                x = j;

            }
            numOfTower += 1;

            t = c[x] +(2*r);
        }

    }
    return numOfTower;
}

  int main()
{
    // given elements
    int n,r;
    cin>>n;
    cin>>r;
    int c[n];
    for(int i =0;i<n;i++){
        cin>>c[i];
    }
    //int range = 2;
    //int n = sizeof(house) / sizeof(house[0]);

    // print number of towers
    cout << number_of_tower(c, r, n);
}
/*
// first we sort the house numbers
    sort(house, house + n);

    // for count number of twoers
    int numOfTower = 0;

    // for iterate all houses
    int i = 0;
    while (i < n) {

        // count number of towers
        numOfTower++;

        // find find the middle location
        int loc = house[i] + range;

        // traverse till middle location
        while (i < n && house[i] <= loc)
            i++;

        // this is point to middle
        // house where we insert the tower
        --i;

        // now find the last location
        loc = house[i] + range;

        // traverse till last house of the range
        while (i < n && house[i] <= loc)
            i++;
    }

    // return the number of tower
*/
