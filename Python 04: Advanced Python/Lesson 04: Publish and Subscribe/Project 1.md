**Here are your instructions:**
Modify the Subscriber.process() method so that the instance counts the number of times the method has been called.

If, after processing the current message, it has processed three messages, it should unsubscribe itself. 

Remove the unsubscribe code from the loop at the end of the main program, since it should no longer be necessary.

Insert print() statements in your modified program until you think you have worked out why it no longer operates correctly, and see if you can suggest a way to fix it (whether or not you are able to implement your suggestion).

**Your Comment:**
Hi Pat,

So, to the current project:

Two issues encountered:
Issue:
1. The original code relied on FIFO, by always removing the [0] element of subscribers, so both
the multiplier registerd function and the simple subscribers could be tracked in terms of number
of calls and removed after the maximum was reached.  Moving the tracking of the number of calls
to the SimpleSubsciber.process() method, works if you are an instance of that class, which the
function isn't.
Solutions:
1. Remove the registered function as there is no requirement for it in the project. (To easy?)
2. Give the function a method to track it's calls like SimpleSubsriber now has. (Best?)
3. Track the calls in the Publisher itself instead of relying on the subscriber(s).  (Not to spec)
4. Take advantage of being able to register a function and make it do something useful for subscribers.
Went with the last one, to see how you can use this.

Issue:
2. Skipping of elements in subscriber list when unsubscribing, e.g.

Input 0: pub
Sub0 : PUB
Input 1: and
Sub0 : AND
Sub1 : AND
Input 2: sub
Sub0 : SUB
Sub2 : SUB
Input 3: and
Sub1 : AND
Sub2 : AND
Sub3 : AND
Input 4: dub
Sub1 : DUB
Sub3 : DUB
Sub4 : DUB
Input 5: and
Sub2 : AND
Sub4 : AND
Sub5 : AND

Solution:
Fix just using the specific element name as opposed to subscript didn't work.  Searching
on the web indicated that using a 'copy' of the list solves this problem.  Seems to work.
Not sure what causes the problem or why the 'copy' solution works.  Slice option used for
speed.  Starting at one i.e. [1:] not zero i.e.[:], because zero is the registed function.

**Items Handed In**
Open Project Handed In

**Overall Comments:**
Hi Mark,

Your project now works and works well. Your thinking is good, but maybe a little bit more complicated than it needs to be. The fundamental issue is that you should never remove items from an iterable object while you're iterating.

The simplest way around it is to make a copy of the original object and delete from that. You might go something like:

    def publish(self, s):
        for subscriber in self.subscribers[:]:  # "slice with everything" means a copy
            subscriber(s)

As an aside, there's a big difference between making a copy of a list and working with slices or copies. The [:] idiom is what is referred to as a "deep copy". Check out this short terminal session in you'll see what I mean (the id() method grabs the memory location of the object - guaranteed to be unique).

&gt;&gt;&gt; lst=[1,2,3]
&gt;&gt;&gt; id(lst)
58619208

&gt;&gt;&gt; new_lst=lst
&gt;&gt;&gt; id(new_lst)
58619208

&gt;&gt;&gt; deep_copied_new_list = lst[:]
&gt;&gt;&gt; id(deep_copied_new_list)
58619656

You might play around little bit and make sure you understand this well. It's exactly the can a thing that can drive you insane if you don't.

-Pat

**Grade:**
Great
