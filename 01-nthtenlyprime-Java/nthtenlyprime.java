// # Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
// # and returns the nth Additive Prime, which is a prime number such that 
// # the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
// # is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2


class nthtenlyprime {

	public boolean isprime(int n){
		if (n <= 1){
			return false;
		}
		if ( n % 2 == 0 || n % 3 == 0){
			return false;
		}
		for (int i = 5; i* i <= n; i = i + 6 ){
			if(n % i == 0 || n % (i + 2) == 0){
				return false;
			}
		}
		return true;
	}
	
	public boolean istenly(int n){
		int sum = 0;
		while(n != 0) {
			sum = sum + n % 10;
			n = n / 10;
		}
		if (sum == 10) {
			return true;
		}
		else {
			return false;
		}
	}

	public int fun_nthtenlyprime(int n){
		int count = 0;
		int i = 2;

		while ( count <= n){
			if (istenly(i) && isprime(i)){
				count++;

			}
			i++;
		}
		return (i-1);
	}
	public static void main(String[] args) {
		
	}
}