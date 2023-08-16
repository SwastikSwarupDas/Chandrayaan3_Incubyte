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

##### <i> NOTE : To my limited knowledge of TDD, I believe two assertions are usually bad practice according to Uncle Bob, I couldnt figure out how to do it inside one argument in the given time. I would like to learn and improve, and master test driven development</i>

![screenshot](Screenshots/TestCase%231FailingBasicForwardBackwardCommit.png)

### Then the production code was refactored only sufficient enough to pass the failing unit test

![screenshot](Screenshots/TestCase%231ForwardBackwardCommit.png)

### The processes was restarted and another unit test case was designed just enough to fail the production code again

![screenshot](Screenshots/TestCase%232FailingRotationCommit.png)

### The production code was refactored to pass the test case by adding the rotational parameters

![screenshot](Screenshots/TestCase%232RefactoringRotationCommit.png)

### The processes was restarted and another unit test case was designed just enough to fail the production code again

![screenshot](Screenshots/TestCase%233FailingUpDownCommit.png)

### The production code was refactored to pass the test case by adding Up and Down command parameters

![screenshot](Screenshots/TestCase%233RefactoringCodeUpDownCommit.png)

### For a final run, a new test case was designed to stress test the code, and it performed as required, confirming the quality of production code and hence concluding the development process

#### STRESS TEST PASSED ✅

![screenshot](Screenshots/Test%20Commit%20%23%20Final%20Huge%20Testcase%20Check%20PASSED.png)

### What I learnt ? 

1. Learnt a lot about Test Driven Development Techniques
2. Introduced myself to a new way of pipeline the development process
3. Understood how to utilize the testing functionality present in python's unittest

### Honorary Mentions 

These were the links that I used to refer to learn TDD : 
1. <a href="https://blog.incubyte.co/tags/software-craftsmanship/">Incubyte Blogs: Software Craftsmanship</a>
2. <a href="https://www.freecodecamp.org/news/an-introduction-to-testing-in-python/">Freecodecamp : An Introduction to testing in Python</a>
3. <a href="https://code.visualstudio.com/docs/python/testing">VS Code Unittesting Documentation</a>
