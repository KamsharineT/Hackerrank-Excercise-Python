
class hash_func():
    def hash_func():
       # Step 1: Take the integer input for the number of elements
        n = int(input())

        # Step 2: Take n space-separated integers as input and create a tuple
        elements = tuple(map(int, input().split()))

        # Step 3: Compute the hash of the tuple and print it
        return (hash(elements))
    
def main():
    output = hash_func.hash_func()
    print(output)

if __name__ == '__main__':
    main()