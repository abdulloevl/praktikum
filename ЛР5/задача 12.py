def is_product_name_palindrome(name: str) -> bool:
    cleaned = "".join(ch.lower() for ch in name if ch.isalnum())
    return cleaned == cleaned[::-1]
print(is_product_name_palindrome("Казак"))             
print(is_product_name_palindrome("Топот"))             
print(is_product_name_palindrome("Самокат"))           
print(is_product_name_palindrome("А роза упала на лапу Азора"))  
