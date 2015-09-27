#!/usr/bin/python3
import encryption as e

def main():
 print("Enter a string to encrypt: ")
 user_input = input()
 e.stringToIntBlocks(user_input)

main()