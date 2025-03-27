#!/usr/bin/env python3
import sys
from calc import add2

def main():
    if len(sys.argv) != 3:
        print("Usage: add2vals <value1> <value2>")
        sys.exit(1)
    
    val1 = sys.argv[1]
    val2 = sys.argv[2]
    
    result = add2(val1, val2)
    print(result)

if __name__ == "__main__":
    main() 