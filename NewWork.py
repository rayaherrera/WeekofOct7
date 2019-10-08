#
x = "There are %d types of people. " % 10
#
doNot = "don't"
#
binary = "binary"
#
y = "Those who know %s and those who %s. " % (binary, doNot)


#
print(x)
#
print(y)


#
print("I said: %r" % x)
#
print("I also said: '%s'." % y)


#
hilarious = False
#
joke_evaluation = "Isn't that joke so funny?! %r"
#
print(joke_evaluation % hilarious)


#
w = "This is the left side of..."
#
e = "a string with a right side."


#
print(w+e)

#October 8th

print("Mary had a little lamb.")
print("Its fleece was what as %s." % 'snow')
print("And everywhere that Mary went")
print("." * 10)

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print(end1 + end2 + end3 + end4 + end5 + end6 + end7 + end8 + end9 + end10 + end11 + end12)

# More Formatting
formatter = "%r %r %r %r"
print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two","three", "four"))
print(formatter % (True, False, True, False))
print(formatter % (formatter, formatter, formatter, formatter))

# Why did Mr.Black use %r instead of %s?

print("When I switched %r with %s, there are no quotation marks around the words. Thats the only difference that I could find.")