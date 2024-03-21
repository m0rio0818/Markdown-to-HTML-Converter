import sys
import markdown

inputCommand = sys.argv
if (len(inputCommand) < 4):
    print("引数を入力してください.\n Ex) python3 file-converter.py markdown sample.md index.html")
else:
    inputfile = inputCommand[2]
    outputfile = inputCommand[3]
    print(inputfile)
    print(outputfile)