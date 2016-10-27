Warning
-------
This is a test given to a person seeking the role of backend engineer. I have virtually no prior experience with Python and I have never used Flask. 
The code in this project does not up to even minimal standard one would expect. 
For me it was still interesting as it gave me a chance to try out Python but I am still feeling uneasy releasing this to foreign eyes. 
My hope is that the project could still serve as a talking point where I can try and discuss how I would have wanted a proper solution to look.

Storing spatial data
--------------------
In a real world application we would most likley use a database which is prebuild to handle 
spatial queries such as Geospatial indexes in MongoDB and PostGIS.

If the dataset is fairly small we and the distance is small then we can project the (lng,lat) in to
a different space and use (x,y,z) which allows for the calculation of the distance by taking the
euclidean norm sqrt(x^2 + y^2 + z^2) where x,y,z are the distance between us and the shop in each direction.

This aproch is simple to implement and understand and is as such a nice starting point. If you
on the other hand have a large dataset or you're simple trying to impress your future empoler with
you can instread use a R-tree. In this project I have not implemented a R-tree or R*-tree but I can give the
algorithm for one if it is of interest.

Note on Quality Assurance 
-------------------------
As someone who is currently responsible for the technical development of a software within the
medical field where software need to adhear to guidlines regarding and uphold a strict standard
of testing to recieve a ER mark i.e. approved as medical device I am all for writing testable code. 
Not only can unit testing make sure our program functions the way we want it can also help new
developers understand the expected functionality and as such serve as a form of documentation. Further
employing patterns such as inversion of control will lead to more modulare code and ties in well
in a event-driven infrastructure. None of this is reflected in the code. In fact, you will find that the database query is open for sql-injection to name just one of many gaping wholes in quality.

Final thoughts
--------------
This is the first time I've written any Python code in a long, long while and it has been fun discovering
the language again. It has also been fun trying out Flask which I have never before used. Since I havnt
had the chance to do any coding myself lately in my current position outside of testing out new SaaS 
and FaaS features on my spare time this exercise has been rewarding. That being said it is somewhat painful having to submit something of this quality to the outside world. 


