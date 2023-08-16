def chandrayaanFunc(inPos,inDir,commands):
    i = 0
    x, y, z = inPos
    prevDir=inDir

    while i < len(commands):

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
           

        elif commands[i] in ('r','l'):
            if inDir in ('N','E','W','S'):
                prevDir = inDir  # Left Right Rotation commands
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