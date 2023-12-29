#import will be included once
import GCDfunction
def main():
    a,b=map(int,input().split())
    print("GCD of {} and {} is {}".format(a,b,GCDfunction.gcd(a,b)))
    
main()
