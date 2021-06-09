reader = open('p059_cipher.txt')
file_lines = reader.readlines()
reader.close()

cipher = [int(i) for i in file_lines[0].split(",")]
print("start trial")

# for i in range(97,123):
#     for j in range(97,123):
#         for k in range(97,123):
#             text = ""
#             for idx in range(0,len(cipher),3):
#                 text += chr(cipher[idx] ^ i) + chr(cipher[idx+1] ^ j) + chr(cipher[idx+2] ^ k)
#             if "extract" in text and "and" in text:
#                 print(i,j,k)
#                 print(text)
#                 print ("-----------------")

#i,j,k = 101,120,112

i = 101
j = 120
k = 112
text = ""
for idx in range(0,len(cipher),3):
        text += chr(cipher[idx] ^ i) + chr(cipher[idx+1] ^ j) + chr(cipher[idx+2] ^ k)

result = sum(ord(c) for c in text)
print(result)