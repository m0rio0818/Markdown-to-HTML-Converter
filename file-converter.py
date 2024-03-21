import sys
import markdown
import os


class FileConverter:
    filepath = "./files/"
    md = markdown.Markdown()
    inputCommand = sys.argv
    
    @staticmethod
    def convert():
        if (len(FileConverter.inputCommand) < 4):
            print("引数を入力してください.\n Ex) python3 file-converter.py markdown sample.md index.html")
        else:
            convertType = FileConverter.inputCommand[1]
            inputfile = FileConverter.inputCommand[2]
            outputfile = FileConverter.inputCommand[3]
            ouput_extentions = (outputfile[outputfile.find(".")+1:])
            
            full_inputfile = FileConverter.filepath + inputfile
            full_outpufile = FileConverter.filepath + outputfile
            print(full_inputfile, full_outpufile)
            
            if (ouput_extentions != "html"):
                print("outputはhtmlファイルでないと、変換できません", outputfile)
            else:
                try:
                    with open(full_inputfile, "r") as f:
                        mdData = f.read()
                        htmlData = FileConverter.md.convert(mdData)
                    flag = os.path.exists(full_outpufile)
                    print(os.path.exists(full_outpufile), full_outpufile)
                    
                    while flag:
                        print("output先に、ファイルは既に存在している")
                        fileOverwrite = input("<< outputファイルが既に存在しているので、上書きしますか？>> y or n\n")
                        if fileOverwrite == "y":        
                            FileConverter.writeFile(full_outpufile, htmlData)
                            break
                        else:
                            newoutput = input("もう一度、output filenameを入力してください")
                            full_outpufile = FileConverter.filepath + newoutput 
                            flag = os.path.exists(full_outpufile)
                    else:
                        FileConverter.writeFile(full_outpufile, htmlData)
                    
                except FileNotFoundError as f:
                    print("指定したファイルは存在しません. ファイルのpathを確認してください.", f)
    
    @staticmethod       
    def writeFile(output_path,data):
        with open(output_path, "w") as f:
            f.write(data)
                 
def main():
    FileConverter.convert()
    
if __name__ == "__main__":
    main()