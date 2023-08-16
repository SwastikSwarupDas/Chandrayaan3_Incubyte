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
           

     
                


        i += 1  # Move to the next command


    return([x,y,z],inDir)


if __name__ == "__main__":
    inPos = [0,0,0]
    inDir = "N"
    commands  = ['f','r','u','b','l']
    
    chandrayaanFunc(inPos,inDir,commands) 