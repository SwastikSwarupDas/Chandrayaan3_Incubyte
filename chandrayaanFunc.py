#The chandrayaanFunc is the function I've chosen for solving the problem statement. 
#Following the rules of TDD, 
#a. Test cases were made to be failed, code was refactored to pass only those test cases
#b. Test cases were updated for the unit tests to fail again
#c. Code was refactored again to pass those tests
#d. Finally the required standard and quality was reached and a huge test case check passed


def chandrayaanFunc(inPos,inDir,commands):
    
    i = 0
    x, y, z = inPos
    
    #Initially, this variable wasnt a part, but it had to be made a part because While switchin from the up and down directions, the "belly facing" direction mattered a lot, we will get to that part

    prevDir=inDir

    while i < len(commands):

    #The basic axis updations during the forward and backward movements 

        if commands[i] in ('f', 'b'):
            
            if commands[i] == 'f':
                if inDir == "N":
                    y += 1
     
                elif inDir == "E":
                    x += 1
 
                elif inDir == "W":
                    x -= 1
  
                elif inDir == "U":
                    z += 1    
   
                elif inDir == "D":
                    z -= 1            

                else:
                    y -= 1
    

            else:  # 'b' command
                if inDir == "N":
                    y -= 1

                elif inDir == "E":
                    x -= 1
       
                elif inDir == "W":
                    x += 1

                elif inDir == "U":
                    z -= 1    
          
                elif inDir == "D":
                    z += 1       
    
                else:
                    y += 1
           
    #Rotation Command updations

        elif commands[i] in ('r','l'): # Left Right Rotation commands

    # Other than when it is in Up or Down Position, we note where it was faced before that change
            if inDir in ('N','E','W','S'):
                prevDir = inDir  # this later becomes the "Belly Facing" direction

    #Basic Clockwise rotations
            if inDir == "N":
                if commands[i] == "r":
                    inDir = "E"
  
                else:
                    inDir = "W"
      
            elif inDir == "E":
                if commands[i] == "r":
                    inDir = "S"
            
                else:
                    inDir = "N"
            
            elif inDir == "S":
                if commands[i] == "r":
                    inDir = "W"
          
                else:
                    inDir = "E"
           
            elif inDir == "W":
                if commands[i] == "r":
                    inDir = "N"
         
                else:
                    inDir = "S"
          
    #This is where the Previous Direction variable prevDir comes into play 
    
    #So The belly direction is flipped everytime it goes from Up or Down or vice versa

            elif inDir == "U":
                if commands[i] == "r":
                    if prevDir == "N":
                        inDir = "E"
                    elif prevDir == "W":
                        inDir = "N"
                    elif prevDir == "E":
                        inDir = "S"
                    else:
                        inDir = "W"
                else:
                    if prevDir == "N":
                        inDir = "W"
                    elif prevDir == "W":
                        inDir = "S"
                    elif prevDir == "E":
                        inDir = "N"
                    else:
                        inDir = "E"
               
            
        elif commands[i] in ('u','d'):
            if inDir in ('N','E','W','S'):
                prevDir = inDir

            if commands[i] == "u":
                if inDir in ('D'):
                    if prevDir == "N":
                        prevDir = "S"
                    elif prevDir == "E":
                        prevDir = "W"
                    elif prevDir == "W":
                        prevDir = "E"
                    else:
                        prevDir == "N"

                inDir = "U"


            else:
                if prevDir in ('U','N','E','W','S'):
                    if prevDir == "N":
                        prevDir = "S"
                    elif prevDir == "E":
                        prevDir = "W"
                    elif prevDir == "W":
                        prevDir = "E"
                    else:
                        prevDir == "N"
                
                inDir = "D"
               
                


        i += 1  # Move to the next command


    return([x,y,z],inDir)


if __name__ == "__main__":
    inPos = [0,0,0]
    inDir = "N"
    commands  = ['f','r','u','b','l']
    
    chandrayaanFunc(inPos,inDir,commands) 