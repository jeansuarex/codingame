name = input()
alphabet = "Alpha, Bravo, Charlie, Delta, Echo, Foxtrot, Golf, Hotel, India, Juliett, Kilo, Lima, Mike, November, Oscar, Papa, Quebec, Romeo, Sierra, Tango, Uniform, Victor, Whiskey, X-ray, Yankee, Zulu".split(", ")

l = []
for i in name.lower():
    l.append(alphabet[ord(i)-97])
print(*l)