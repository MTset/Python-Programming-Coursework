**Here are your instructions:**
Extend the final definition of the composable object to allow it to be raised to positive integer powers. This will require defining the __pow__ method.

For the purposes of this exercise, assume that f* *2 is the same as f*f, f* *3 is the same as f*f*f, and so on. So (f**3)(x) is f(f(f(x))).

If the argument is not an integer, the method should raise a TypeError exception; if the argument's value is non-positive, the method should raise a ValueError.

**Your Comment:**
Hi Pat,

Thank you very much for all the feedback on the last project.  It will take me a while to come to grips 
with it, but it's good to know such things as 'mock' exist.

I must admit I found this (Lesson 1) module quite challenging in concept.
The last two test in tests_exceptions, I simply could not get to work with 'with'.  It would raise a
TypeError straight away without ever getting to the __pow__  method in composable, so I did it
another way.  Have a great weekend.

Cheers,

Mark

**Items Handed In**
Open Project Handed In

**Overall Comments:**
Hi Mark,

I'm happy that you're struggling with this (a little bit, anyway). Not that I want you to suffer in any way, but that is the best way to learn.

I do not experience the problems using with that you did. In fact, I was able to get these tests to work just fine:

        with self.assertRaises(ValueError):
            test= fc.__pow__(0)
            test=fc.__pow__(-1)

But I would point out that is not typically the way you would call this function - you do it more as you did here:

        with self.assertRaises(TypeError):
            fc = square ** 1.1

So, in fact I got these tests to work:

        with self.assertRaises(ValueError):
            test = fc**0
            test = fc ** -1

.... no need to use the "magic method" call directly. Under the hood, Python will know what to do.

This project is more "computer sciency" then ordinary, which is appropriate by Python 4. The topic of decorators (@) will have some overlap with the abstract algebra idea of composition.

Here's an alternative solution, for your inspection -  you'll note it uses a recursive approach:

 def __pow__(self, power):
        if type(power) != int:
            raise TypeError('%s is not an integer' % power)
        if not power &gt; 0:
            raise ValueError('%s is not greater than zero' % power)
        
        if power == 1:
            return self
        else:
            return self ** (power - 1) * self

You have a good weekend, too.

-Pat

**Grade:**
Great
