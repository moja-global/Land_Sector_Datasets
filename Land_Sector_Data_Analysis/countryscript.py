#Script to to create file structure based on lists
#Sy SimpleShell

import os
from countries import * # Imports the list of folders from countries.py file


main_dir = [Africa, Asia, Australia, Europe, NorthAmerica, SouthAmerica]			# Loading the list of sub-directories
root_dir = 'Continents'
main_dir_names = ['Africa', 'Asia', 'Australia', 'Europe', 'North America', 'South America'] # Name of the sub-directories
def main():
    # Create directory
    for i in range(0,len(main_dir)):
        for j in range(0,len(main_dir[i])):
            global main_dir_names
            dirName = str(root_dir) + '/' + str(main_dir_names[i]) +'/' + str(main_dir[i][j])
            
            try:
                # Create target Directory
                os.makedirs(dirName)
                print("Directory " , dirName ,  " Created ") 
            except FileExistsError:
                print("Directory " , dirName ,  " already exists")        
            
            # Create target Directory if don't exist
            if not os.path.exists(dirName):
                os.makedirs(dirName)
                print("Directory " , dirName ,  " Created ")
            else:    
                print("Directory " , dirName ,  " already exists")
            for filename in main_dir_names:
                filename=str(root_dir) + '/' + str(main_dir_names[i]) +'/' + str(main_dir_names[i])+'.md'
                p = open( filename,'w')
                p.write("Add "+ str(main_dir_names[i]) +"'s Land Sector Data Analysis")
                p.close

            for j in range(0,len(main_dir[i])):
                filename1=str(root_dir) + '/' + str(main_dir_names[i]) +'/' + str(main_dir[i][j])+ '/' +str(main_dir[i][j])+'.md'
                f=open( filename1,'w')
                f.write("Add "+ str(main_dir[i][j]) +"'s Land Sector Data Analysis")
                f.close

         
if __name__ == '__main__':
    main()