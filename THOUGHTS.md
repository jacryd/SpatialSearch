Storing spatial data
--------------------
In a real world application we would most likley use a database which is prebuild to handel 
spatial queries such as Geospatial indexes in MongoDB och PostGIS but since the purpose of this
project is to demonstrate that I did not waste my time going to engineering school I will 
refrain from using them and instead use SQLLite.

If the dataset is relativly small then we could start by filtering on cheap operations such as the 
tags, abs(ourLng - shopLng) > dist, abs(ourLat-shotLat) > dist. The resulting dataset could then be 
chosen by checking the distance with pythagoran and sort by review and then return with a 
'top x'. 

This aproch is simple to implement and understand and is as such a nice starting point. If you
on the other hand have a large dataset or you're simple trying to impress your future empoler with
you can instread use a R-tree. 

R-trees
-------


Note on Quality Assurance 
-------------------------
As someone who is currently responsible for the technical development of a software within the
medical field where software need to adhear to guidlines regarding and uphold a strict standard
of testing to recieve a ER mark i.e. approved as medical device I am all for writing testable code. 
Not only can unit testing make sure our program functions the way we want it can also help new
developers understand the expected functionality and as such serve as a form of documentation. Further
employing patterns such as inversion of control will lead to more modulare code and ties in well
in a event-driven infrastructure. This being said the code in this project could use a refactoring of 
before it could live up to and sort of QA standard that I would feel proud about. 

Final thoughts
--------------
This is the first time I've written and Python code in a long while and it has been fun discovering
the language again. It has also been fun trying out Flask which I have never before used. Since I havnt
had the chance to do any coding myself lately in my current position outside of testing out new SaaS 
and FaaS features on my spare time this exercise has been rewarding. Feel free to skip the next
section if you wish to end on a happy note.

The new "Extreme programming"
----------------------------
Short story. I recieved this assignment sometime in the middle of last week, read the instructions
and figured, no problem, I'll to it this Saturday. Well, Saturday comes and I sit down and get going. Since I
had never used flask before I started by quickly reading up on how to get going. Now straight away
I get a small set back as I try to set everythin up, when my pip installer for some reason will not work. 
Okey, I think to myself,
not a big deal, we can fix this. But it was a big deal, because I had 6 days earlier decided I would
quit snus (tobacco product). But I manage to pull through when I find that my PATH variable
was all messed up. Ok, breath. Then when I try to get flask my internet goes down. You see, 
I live in probably the only appartment in Stockholm where there is no land line and 
my 4G modem only allows 200 GB of data per month, which I had used for MIT open courses. Fine, it was mostly Netflix.
Anyhow, my baby is now screaming as try to get the mobile hot spot on my phone up. 
As the web page I use for instructions slowly, slowly, loads I 
realize as I am hammering away on the refresh button that I am in the middle of a snus related breakdown.
So I simply close the computer and walk away, trying not give reviel to my wife the emotional trauma I
had just been through. Luckily, the next day I went and bought some snus and here we are. 
All well in the end.

