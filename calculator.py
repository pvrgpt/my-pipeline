#!/bin/bash
def add(a,b):
    return a + b
if __name__ == "__main__":
    result = add(2,2)
    assert result == 4, "Math is broken!"
    print(f"Success 2 + 2 is {result}")
