# GreekFamilyTree
Easily generate family trees for your sorority or fraternity. Each family will have its own .svg genderated showing their family. 

This project was generated using code from: http://matthiaseisen.com/articles/graphviz/

## Purpose
This project was created to generate greek family trees for Alpha Sigma Kappa - Zeta. The master branch is intended to be more general for others to use. 

## CSV Instructions
The intension is to make adding new members easier. 
Simply add new members to the file (csv in this case) in any order. The family name will group the families as needed in the code. The order that matters is the row Big and Little pair must be accurate. 

### Bigs can have multiple littles but they must be represented in individual rows:
For example:
[Family 1, Jane Smith, Sarah Kelley]
[Family 1, Jane Smith, Rachel Green]

### Littles can have multiple bigs but again they must be represented in individual rows:
For example:
[Family 1, Jane Smith, Sarah Kelly]
[Family 1, Meghan Road, Sarah Kelly]

## Code Instructions:
Input is a .csv file. You can easily change the input file type to json or excel or whatever with simple python knowledgdge. The script uses pandas and graphviz to generate .svg images. 

Must have [Family, Big, Little] fields. The Family is the group field that decides the tree to make. If a name is repeated it is assumed to be the same person. Meaning each name must be unique. 

Consider adding years to the name (for example Jane Smith [2000-2003]) to show their active years, or a single graduation year. This could minimize duplicate named nodes. 
