def isPalindrome(str):
  str = str.lower()
  if (str == str[::-1]):
    return True
  else:
    return False


# Solicitar ao usuário que introduza a sentença
def main():
  userInput = input("Digite uma PALAVRA a ser testada como palíndromo: ")

  if (isPalindrome(userInput)):
    print(userInput + " Esta palavra é palindrome!")
  else:
    print(userInput + " Esta palavra não é palindrome!")
    
if __name__ == "__main__":
    main()
