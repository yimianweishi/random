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
linux_status = 0
linux_r = []
def linux_srand(seed):
    """
    Args: 
        seed(int): Random numbers seed
    
    Returns: void

    Example:
        linux_srand(1)
        
    """
    if seed == 0:
        seed = 1
    word = seed
    seed = seed & 0xffffffff
    global linux_status
    global linux_r
    linux_status = 0
    linux_r = [0] * (344 + linux_status)
    linux_r[0] = seed
    for i in range(1, 31):
        if (word < 0):
            hi = (-word) // 127773
            hi = -hi
            lo = (-word) % 127773
            lo = -lo
        else:
            hi = word // 127773
            lo = word % 127773
        word = ((16807 * lo)) - ((2836 * hi))
        if word < 0:
            word = (2147483647 + word) & 0xffffffff
        linux_r[i] = word
    for i in range(31, 34):
        linux_r[i] = linux_r[i - 31]
    for i in range(34, 344):
        linux_r[i] = (((linux_r[i - 31] + linux_r[i - 3]) & 0xffffffff) % (1 << 32)) & 0xffffffff

def linux_rand():
    """
    Returns: 
        int: Random numbers

    Example:
        #seed must be set
        linux_rand()
    """
    global linux_status
    global linux_r
    linux_r.append(0)
    linux_r[344 + linux_status] = (((linux_r[344 + linux_status - 31] + linux_r[344 + linux_status - 3]) & 0xffffffff) % (1 << 32)) & 0xffffffff
    linux_status += 1
    return linux_r[344 + linux_status - 1] >> 1
#种子默认为1
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
#     int32_t word;
#     word = seed;
#     for (int i = 1; i < 31; i++)
#     {
#         long int hi = word / 127773;
#         long int lo = word % 127773;
#         word = 16807 * lo - 2836 * hi;
#         if (word < 0)
#             word += 2147483647;
#         r[i] = word;
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

