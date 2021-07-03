global status
status = 1
def _srand(seed):
    global status
    status = seed
def _rand():
    global status
    status=(214013*status+2531011) & 0xffffffff
    return status>>16&((1<<15)-1)
print(_rand())

#include<iostream>
#include<cstdlib>

# using namespace std;

# unsigned int status=1;
# int seed = 1;

# int my_srand(unsigned int seed){
#     status=seed;
# }

# int my_rand(){
#     status=214013*status+2531011;
#     return status>>16&((1<<15)-1);
# }
# int main()
# {
#     int n = 1000;
#     srand(1);
#     while (n--)
#     {
#         cout << rand() << " "  << my_rand() << endl;
#     }
#     system("pause");
# }