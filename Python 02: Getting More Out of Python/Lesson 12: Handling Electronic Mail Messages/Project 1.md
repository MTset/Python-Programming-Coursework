**Here are your instructions:**
Write a function that takes an email address, a string, and a list argument. It should return an email message addressed to the email address passed as the first argument, with the second argument as the message body. If the list is non-empty, then each list item should be treated as the name of a file and the corresponding file should be attached (with an appropriate MIME type) to the message.

Please include any files to attach in the same folder as your program. There is no need to send it as an email with smtp, though you may wish to print it as a string as a part of testing.

**Your Comment:**

**Items Handed In**
Open Project Handed In

**Overall Comments:**
Hi Mark,

You've done a terrific job with this project and with the associated tests. Just one thing I would point out... 

If you ever have a file with an unguessable mime type, your code will fail at this line:

maintype, subtype = contenttype.split('/', 1) 

... Because mytypes.guess_type() returns a None object if you can't figure out what kind of file you have given it.

When this happens, you can use a generic encoding to bundle it up and send it on its way. The recipients client won't be able to choose the right app to open it, of course, but at least it will arrive safely. You can make this happen by including code something like:

        for fn in attachments:  
            ctype, encoding = mimetypes.guess_type(fn)
            if not ctype:
                ctype = 'application/octet-stream'  #  if we're heading to else suite
                
            maintype, subtype = ctype.split('/', 1)

A good example is in the Python docs:

http://docs.python.org/3.2/library/email-examples.html

Scroll down to the example of emailing all the files in a given directory.  Note the stack of if / elif / elif /elif /... ending in else, which is where a catchall base64 encoding is applied.

The key challenge here is to squeeze content through a pipe that's only comfortable with the first 127 ASCII characters. Optimally, you can do that with the right encoder, but you can always resort to a default.

-Pat

**Grade:**
Great
