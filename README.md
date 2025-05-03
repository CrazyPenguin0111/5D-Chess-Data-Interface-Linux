# About the Project
This is a set of python scripts that download, install, and run several different 5D Chess Utilities previously only available on windows. 
This project heavily uses proton on linux to run the windows executables.  
# Requirments

Proton >9.04

# instalation
You can grab the latest release by going to the releases page on this github repo and downloading the tar.gz file  

Once you downloaded and extracted the tar.gz file you should make both the install.py and run.py scripts executable by doing  
```chmod +x install.py```  
```chmod +x run.py``` 
  
Go to the startup command window for 5D Chess in your Steam Library and enter the following command.  
```/path/to/protonhax init %COMMAND%```

Alternativly you can add /path/to/protonhax to your PATH variable and just add  
```protonhax init %COMMAND%``` 

![image](https://github.com/user-attachments/assets/8d776bba-7554-44b0-a18b-41aacd292291)

   

To download all the applications you can execute the install.py script.  
After downloading all the executables via the install script, you can execute the run.py script to select a program to run.  
When specifiying launch options make sure to add the full path to the protonhax script. 
Keep in mind that the steam game client has to be running before starting any of the programs.  

# Acknowledgements
GHXX - [5D Chess Data Interface](https://github.com/GHXX/FiveDChessDataInterface)  
Tesseract [5D PGN Recorder](https://github.com/penteract/5D-PGN-Recorder)  
Mauer01 [GUI For Data Interface](https://github.com/mauer01/gui-for-5dchess-datainterface)  
jcnils [Protonhax](https://github.com/jcnils/protonhax)

