# Create2DTextureArray
Concatenates individual image textures into into a 2D texture array. Useful for creating animated textures in Unity. 

## Usage ##
<b>CreateTexArray.py</b> is best for concatenating all textures into a single texture array. <br><br>
`python3 CreateTexArray.py IMGs/1.png IMGs/2.png IMGs/3.png IMGs/4.png output.png` <br><br>
The result is a new image <i>output.png</i> which contains all images 1 through 4 in a vertically arranged sequence. <br>

<b>Main.py</b> batches the texture array creation process by grouping the provided images based on their shared prefixes. Given the following file structure...<br><br>
textures -> <br>
&emsp;-> eyes1.png <br>
&emsp;-> eyes2.png <br>
&emsp;-> eyes3.png <br>
&emsp;-> face1.png <br>
&emsp;-> face2.png <br>
&emsp;-> face3.png <br><br>
...and a JSON file containing the prefixes "eyes" and "face", the following script will create 2 texture arrays, one for the eyes and one for the face. <br><br>
`python3 Main.py <PATH TO YOUR TEXTURES> <YOUR PREFIXES JSON FILE> <OUTPUT PATH>`
