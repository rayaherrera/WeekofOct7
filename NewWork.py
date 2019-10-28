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

print("When I switched %r with %s, there are no quotation marks around the words. That's the only difference that I could find.")


# Time for strange stuff in the world of printing...

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days: ", days)
print("Here are the months: ", months)

print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")

# What if I didnt like Jan being listed on the line with the rest of the
# text and away from the other months? How could I fix that?

# More escaping

tabbyCat = "\tI'm tabbed in."
persianCat = "I'm split\non a line."
backlashCat = "I'm \\ a \\ cat."
taskCat = """
Ill make a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabbyCat)
print(persianCat)
print(backlashCat)
print(taskCat)

# Escape Seq            What does it do
# \\                backslash
# \'                single quote
# \"
# \a
# \b                backspace
# \f                form feed
# \n                new line
# \N{name}
# \r                carriage return
# \t                tab
# \uxxxx
# \Uxxxxxxxx
# \v
# \ooo              octal value
# \xhh              hex value

# What does the following code do:
# while True:
#       for i in ["/", "-", "|", "\\","|"]:
#           print("%s\r" % i, end='')

# Can you replace """ with '''?


# Asking Questions

age = input("How old are you? ")
height = input("How tall are you? ")

print("So, you really %r old and %r tall?  Wow..." %(age, height))


color = input("So whats your favorite color? ")
color2 = input("What about your second favorite color? ")

print("So %r and %r are your favorite colors?  That's cool!" %(color, color2))

hobby = input("So what is your favorite hobby? ")
hobby2 = input("Why do you like that hobby? ")

print("The fact that you think %r is a great reason to like %r is great. That's awesome!" %(hobby2, hobby))

