import os
import matplotlib.pyplot as plt

vowels = "аеіиоуюяєАЕІИОУЮЯЄ"

if not os.path.exists("text.txt"):
    with open("text.txt", "w", encoding="utf-8") as f:
       f.write("Куць Софія цілий день нічого не робила, і почала вчитись тільки вночі")
    print("Створено text.txt.")

with open("text.txt", "r", encoding="utf-8") as f:
   text = f.read()

counter = {v: 0 for v in vowels}

for ch in text:
        if ch in counter:
                  counter[ch] += 1

plt.bar(counter.keys(), counter.values())
plt.title("Частота голосних у тексті")
plt.xlabel("Голосні")
plt.ylabel("Кількість")

plt.savefig("hist.png")
plt.close()

print("Готово! hist.png збережено.")
