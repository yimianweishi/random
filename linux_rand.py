# global seed
# seed = 1

# def mysrand(seed1):
#     global seed
#     seed = seed1
# def myrand():
#     global seed
#     seed = (seed * 1103515245 + 12345) & 0x7fffffff
#     return (seed // 65536) % 32768 & 0xffffffff
# print(myrand())
n = 0
global status
status = 1

def myrand(seed):
    global status
    r = [0] * (344 + status)
    r[0] = seed
    for i in range(1, 31):
        r[i] = (((16807 * (0xffffffff & r[i - 1])) % 2147483647)) & 0xffffffff
    for i in range(31, 34):
        r[i] = r[i - 31]
    for i in range(34, 344 + status):
        r[i] = ((r[i - 31] + r[i - 3]) % (1 << 32))& 0xffffffff
    status += 1
    return r[343 + status - 1] >> 1
print(myrand(1)) #种子默认为1
#第二种LCG线性同余发生器不常用 seed 为种子上次结果作为下次结果种子使用
#seed = 1103515245 * seed + 12345
#下面是C版本
#include<iostream>

# using namespace std;

# int main()
# {
#     const int SEED = 1; 
#     const unsigned int MOD = 0x7ffffffff; 
#     const long long MOD_MAX = (1LL << 32);
#     unsigned int r[700];
#     r[0] = 2; //种子
#     for (int i = 1; i < 31; i++)
#     {
#         r[i] = (16807LL * (signed int)r[i - 1]) % 2147483647; 
#     } 
#     for(int i = 31; i < 34; i++) 
#         r[i] = r[i - 31]; 
#     for(int i = 34; i < 700; i++) { 
#         r[i] = (r[i - 3] + r[i - 31]) % MOD_MAX; 
#     }
#     for (int i = 344; i < 644; i++) //r[344]为第一个随机数,之后为随机数列,要得到更多的随机数,加长数组长度和循环次数就行
#         cout << (r[i] >> 1) << endl;
#     system("pause");
# }

