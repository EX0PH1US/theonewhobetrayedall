<img width="1600" height="1264" alt="image" src="https://github.com/user-attachments/assets/37b299c9-b7cf-41ef-abf1-1867ca632e30" />

This is a puzzle made to test someone's skills in decoding and steganography.
To test how someone uses a given information and how far they can enumerate something to get the answer.

The answer to the puzzle is 'judas is placed headfirst inside lucifers
central mouth, with his back skinned by the devils claws streaker'

The Flask app is deployed using Render

<a href="https://theonewhobetrayedall.onrender.com/">Flask App</a>

The puzzle has a direct reference from the book Dante's Inferno.
used:
steganography
morse code
ROT13
Flask

How to solve this puzzle?

First, you will be given the [561.png](./561.png), which is an 8-bit grayscale image. It contains byte-encoded text. When you decode the text, you will see this text.

"Problems and Answers. Humans asks problems and humans give answers. 
Some problems have the answer hidden inside them while other problems require deep research.
Sometimes you find a answer that needs to be converted into the real answer like adding x00 in a binary.
Some answers are just Problems themselves that lead to more problems. The most important thing
to answer a problem is to count every bit of the problem to understand whats going on and what is      
avilable to you to answer that problems. Put your answer here theonewhobetrayedall.onrender.com"

When you will open <a href="https://theonewhobetrayedall.onrender.com/">TheOneWhoBetrayedAll</a>

You will be greeted to a page which has a form input that requires a passphrase. There is a hint saying count every bit or pixels or atoms.

Now, if you go back to the image and look at its size, you will see that the width is 111 and the  height is 11. This is binary. 
If you look at the decoded file, I have hinted "add x00". 

To get the answer, you will have to add 00 at the start and then one in the middle to make it an 8-bit binary. 00110111 -> this decodes to <b>seven</b> which is the answer to the form. 
You will have to convert it into ASCII and not hexadecimal, which corresponds to 37 or the decimal number 55, but the answer is in ASCII. 

</i>7 refrences the seven sins</i>

After you enter the answer into the form, you will get a .zip file named <b>theonewithdante</b>. The .zip file is password-protected. The one with Dante was <b>Virgil</b>, which is the passphrase.

<i>Dante cannot descend without Virgil; you cannot progress without him either</i>

You will now get two files. A PDF named dante.pdf and a JPG named TheOneInTheMouthOfTheLightBringer.jpg

The PDF has the answer, and the image is a very famous illustration made by <b>Gustave Doré from his illustrations of Dante's Divine Comedy</b>
<img width="2020" height="1588" alt="image" src="https://github.com/user-attachments/assets/3f60faf7-f839-464d-b2f2-7dc2d95d301f" />

This is an image showing Judas in the mouth of Lucifer (The Light Bringer) in the innermost Pit of the ninth circle of hell <b>Judecca</b>

This image is hiding a .wav file in it (hinted in decoded text "Some problems have the answer hidden inside them"). the passphrase for extraction is <b>judas</b>

Now you will get a .wav file named notriangleisthepassphrase. No triangle actually means the number of Triangles. The .wav file contains Morse code, which, when decoded, gives you the coordinates of a specific place in the Nevada Desert. 

37°24'05.2"N 116°52'04.6"W -> this is in the form of 37,24,05.2 NORTH 116,52,04.6 WEST

<img width="640" height="463" alt="image" src="https://github.com/user-attachments/assets/8a25ecc5-b753-4be3-ae22-6d38cb58de08" />

As you can see, there are six triangles in this image. So, the passphrase is 6, not in words but in numbers.

</i>6 Triangles -> Hexagon = imperfection, fragmentation (stepping further from divine order)</i>

Now you will extract the final file named Cocytus.txt. 

"your answer lies in va whqrppn gur qrrcrfg cneg bs gur avagu pvepyr bs uryy" 

So here you get the final hint! "va whqrppn gur qrrcrfg cneg bs gur avagu pvepyr bs uryy" is encoded using the ROT13 algorithm. If you convert it, you will get this message:

<i>in judecca, the deepest part of the ninth circle of hell</i>

This is a reference to Judecca.

<i>Judecca is the deepest and final zone of the Ninth Circle of Hell, named for Judas Iscariot, who betrayed Jesus Christ</i>

This is the hint you need to finally find the answer hidden in the vast, random words of the PDF dante.pdf. 

You have to search for the word Judas, and you will see the answer.

<i>judas is placed headfirst inside lucifers central mouth, with his back skinned by the devils claws streaker</i>

So, this is how you solve the puzzle "TheOneWhoBetrayedAll". 

<i>The title of the landing page of the Flask app is 0011011100001111, which, when separated with a space after 8 characters, reads 7(and an unprintable character), so the answer (to the form) was always there in front of you.</i>

GGs

