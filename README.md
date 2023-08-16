# Chandrayaan3_Incubyte - Swastik Swarup Das
<h3 align="left">Chandrayaan 3 Code Python</h3>
<p align="Left">
  
### Brief Summary :
  The laws of Test-Driven-Development were followed to the best of my capabilities in this problem. The concepts of Test-Driven-Development brought about a sharp change to the process in which I would usually code this without TDD.
### Experience 
Familiarizing myself with the concepts of Unit Testing in Python, Test Driven Development, The syntax and the techniques to achieve the following in Visual Studio Code, were quite challenging. <br/> The Blogs and articles from  <a href="https://blog.incubyte.co/tags/software-craftsmanship/">Incubyte Blogs</a> were a rather helpful source to gain insights about TDD and kickstart the process for me to learn and familiarize the concepts.
<br/>
</div>

## About The Code, Screenshots, Experience, and Thought Processes
![screenshot](Screenshots/Chandrayaan3_Incubyte.png)

The process begins with the learnings from <a href="https://www.youtube.com/watch?v=qkblc5WRn-U">Uncle Bob's Video </a> <br/>

### The three laws of TDD state : 
1. Write production code only to pass a failing unit test.
2. Write no more of a unit test than sufficient to fail (compilation failures are failures).
3. Write no more production code than necessary to pass the one failing unit test.   

#### Following the rules of TDD, 
1. Test cases were made to be failed, code was refactored to pass only those test cases
2. Test cases were updated for the unit tests to fail again
3. Code was refactored again to pass those tests
4. Finally the required standard and quality was reached and a huge test case check passed

### Upon examining the code, and following TDD standards, the first Test Case was formed for a basic Forward/Backward movement functionality. This was a failing test case.

##### <i> NOTE : Although I believe two assertions are usually Bad practice according to Uncle Bob, I couldnt figure out how to do it inside one argument in the given time </i>

![screenshot](Screenshots/TestCase%231FailingBasicForwardBackwardCommit.png)

### Then the production code was refactored only sufficient enough to pass the failing unit test :

![screenshot](Screenshots/TestCase%231ForwardBackwardCommit.png)

### The processes was restarted and another unit test case was designed just enough to fail the production code again. 

![screenshot](Screenshots/TestCase%232FailingRotationCommit.png)

### The production code was refactored to pass the test case by adding the rotational parameters

![screenshot](Screenshots/TestCase%232RefactoringRotationCommit.png)

### The processes was restarted and another unit test case was designed just enough to fail the production code again. 

![screenshot](Screenshots/TestCase%233FailingUpDownCommit.png)

### The production code was refactored to pass the test case by adding Up and Down command parameters.

![screenshot](Screenshots/TestCase%233RefactoringCodeUpDownCommit.png)
