# this is really good!  I mean in the sense that you wrote your own mini logger.
# I didn't recognize the package `logger` so I traced it back.
# but anyhow, yes, writing your own functions helps tremendously in learning.
# Of course, you could have gotten familiar with the logging module in python, and you'll see it is pretty easy and sturdy
# however, I circle back to the good part here.  Often I see people bring in a whole giant package just to use 1%, like one function
# of that package. That gets to be a heavy toll in versioning and just extra code, PLUS the security issue.  The more
# external packages the bigger the hole.
# One thing I've done is write a comment to the tune of...
#  # writing one off code based off of package XYZ to keep code light.  Will include larger package if we need more.
# or
# # Wrote one off function to avoid bringing in larger package to keep down dependencies
# 
# that way you can discuss as a group/team. 
#
#
# But again, this is great practice for your own software development, may not always fly in a work environment,
# but I definitely use it a lot.
# This is a little package I wrote for my own personal use https://github.com/Niarfe/stoic-args/blob/main/stoicargs/parser.py.
# I got tired of bringing in the entire argparse module and having to remember all the details... this adds just a little bit of 
# code to pass in arguments like key=value.  It started just like your file here, a utility that I built that I kept writing over and over...
#
def write_log(choice, message):
    try:
        with open('gainers.log', 'a') as errorfile:
            errorfile.write(choice.upper() + ' ' + message + '\n')
    except FileNotFoundError:
        with open(f'gainers.log', 'w') as errorfile:
            errorfile.write(choice.upper() + ' ' + message + '\n')

