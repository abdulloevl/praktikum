from collections import Counter
weather = ["sunny", "sunny", "cloudy", "rain", "sunny",
"rain"]
counter = Counter(weather)
most_common_weather = counter.most_common(1)[0][0]
total = len(weather)
percentages = {w: (count / total) *100 for w, count in counter.items()}
print("Самый частый т ип погоды:")
print("/n Доля каждого типа:")
for w, p in percentages.items(): print(f"{w} - {round(p)}%")
