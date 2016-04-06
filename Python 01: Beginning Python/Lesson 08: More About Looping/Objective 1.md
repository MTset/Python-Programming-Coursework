**Objective:**
This project tests your ability to use more sophisticated loops.

Create a new Python source file named para_breaker.py.
Write a program to break up a paragraph into sentences and phrases. Sentences are delineated by periods and phrases are delineated by commas.
Print the results to the screen. You will need to use a loop within a loop.
Use the text from the second paragraph of the United States Declaration of Independence (provided below).
United States Declaration of Independence to be used in the example:

We hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness. - That to secure these rights, Governments are instituted among Men, deriving their just powers from the consent of the governed, - That whenever any Form of Government becomes destructive of these ends, it is the Right of the People to alter or to abolish it, and to institute new Government, laying its foundation on such principles and organizing its powers in such form, as to them shall seem most likely to effect their Safety and Happiness. Prudence, indeed, will dictate that Governments long established should not be changed for light and transient causes; and accordingly all experience hath shewn that mankind are more disposed to suffer, while evils are sufferable than to right themselves by abolishing the forms to which they are accustomed. But when a long train of abuses and usurpations, pursuing invariably the same Object evinces a design to reduce them under absolute Despotism, it is their right, it is their duty, to throw off such Government, and to provide new Guards for their future security.  - Such has been the patient sufferance of these Colonies; and such is now the necessity which constrains them to alter their former Systems of Government. The history of the present King of Great Britain is a history of repeated injuries and usurpations, all having in direct object the establishment of an absolute Tyranny over these States. To prove this, let Facts be submitted to a candid world.

Below is an example of output from running the program.

**************************************************
Sentence #1
Phrase 1: We hold these truths to be self-evident
Phrase 2: that all men are created equal
Phrase 3: that they are endowed by their Creator with certain unalienable Rights
Phrase 4: that among these are Life
Phrase 5: Liberty and the pursuit of Happiness
**************************************************
Sentence #2
Phrase 1: - That to secure these rights
Phrase 2: Governments are instituted among Men
Phrase 3: deriving their just powers from the consent of the governed
Phrase 4: -
 That whenever any Form of Government becomes destructive of these ends
Phrase 5: it is the Right of the People
 to alter or to abolish it
Phrase 6: and to institute new Government
Phrase 7: laying its foundation on such principles
 and organizing its powers in such form
Phrase 8: as to them shall seem most likely to effect their Safety and
 Happiness
**************************************************
Sentence #3
Phrase 1: Prudence
Phrase 2: indeed
Phrase 3: will dictate that Governments long established should not be changed for
 light and transient causes; and accordingly all experience hath shewn that mankind are more disposed
 to suffer
Phrase 4: while evils are sufferable than to right themselves by abolishing the forms to which they
 are accustomed
**************************************************
Sentence #4
Phrase 1: But when a long train of abuses and usurpations
Phrase 2: pursuing invariably the same Object
 evinces a design to reduce them under absolute Despotism
Phrase 3: it is their right
Phrase 4: it is their duty
Phrase 5: to
 throw off such Government

**Here are the files you handed in:**
python1Homework/para_breaker.py

**Overall Comments:**
 Hi Mark,

You've done a terrific job on this project. Your output is very nicely formatted and quite readable. Really terrific job finding and applying the textwrap library.

Here are some tips might help you for future projects:

-Since you're using an imported library called textwrap, you invite confusion by naming a variable textWrap. While this is syntactically-correct, it does put a little bit of extra cognitive load on anyone reading your code to keep these straight.

-FYI, enumerate () has an optional "start" argument:

for _ in enumerate(['a', 'b', 'c'], start=666):
    print(_)

(666, 'a')
(667, 'b')
(668, 'c')

-Note you can print 30 stars using multiplication:

print ( 30 * "*")  # prints 30 stars

-In Python, we typically use all_lower_case words for variable names, CamelCase for classes and ALLCAPS for constants per the Python styling guidelines.

If you're interested, you can pick up your own copy of "PEP-8" at:

https://www.python.org/dev/peps/pep-0008

-Pat

**GRADE: Great**
 You have passed this objective.
