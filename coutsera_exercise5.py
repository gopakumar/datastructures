text = "X-DSPAM-Confidence:    0.8475";
pos = text.find("0")
print (pos)
print(float(text[pos:]))


