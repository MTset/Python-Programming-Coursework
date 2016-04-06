**Here are your instructions:**
Make a FileHandling_Homework project and assign it to your Python2_Homework working set. In that project, write a module containing a function to examine the contents of the current working directory and print out a count of how many files have each extension (".txt", ".doc", etc.)

Write a separate module to verify by testing that the function gives correct results.

**Your Comment:**
Hi Pat,

Well spotted about no file extension.  At least I did remember to exclude directories.

Cheers,

Mark

**Items Handed In**
Open Project Handed In

**Overall Comments:**
Hi Mark,

Thanks a lot for taking another look at this. You have amped up its transparency by a couple of orders of magnitude. It now reads like a Tom Clancy novel.

Please don't take my comments as hyper-critical. You will find your own style and you'll probably find that as you interact with your teammates that your collective coding styles will blend as a form of technical social norming takes place. As a mentor, my job is to share my honest, best opinions with you. But at the end of the day, it's up to you to decide which of my comments/opinions work well with your coding practices, cognitive processes, etc.

Is only one improvement I would suggest to the current incarnation of your project. It would be more readable if you move the file creation logic right next to the statement of the expected outcome:

   for file in ["test1.doc", "test2.doc", "long.file.ext.tz", "no_ext", "joe.zip"]:
       open(file, 'w').close()
   expected = {"doc":2, "tz":1, "":1, "zip":1}

... This sort of side-by-side comparison is easy on the eyes and requires zero bandwidth hunting stuff down.

Overall: awesome work.

Best wishes for a great weekend.

-Pat

**Grade:**
Great
