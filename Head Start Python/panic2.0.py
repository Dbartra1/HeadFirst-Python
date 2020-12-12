phrase = "don't panic!"
#change phrase into a list 
plist = list(phrase)
#print phrase and list
print (phrase)
print (plist)

#new and improved code using slicing and join
#slice out the word "on" and assign it to new_phrase
new_phrase = ''.join(plist[1:3])
#combine what is already in new_phrase and add " tap"
new_phrase = new_phrase +''.join([plist[5], plist[4], plist[7], plist[6]])

print (plist)
print (new_phrase)