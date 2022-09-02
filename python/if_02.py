a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a : print("python") # "python" 단어는 있지만 "you" 단어는 a 문자열에 없으므로 거짓
elif "shirt" not in a : print("shirt")
elif "need" in a : print("need")
else: print("none") # 먼저 참이 되는 세 번째 조건 "shirt" 출력