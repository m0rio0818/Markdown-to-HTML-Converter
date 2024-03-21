import sys
import markdown
import os


class FileConverter:
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
            print(outputfile[outputfile.find("."):])
        
            if convertType == "markdown":
                try:
                    with open(inputfile, "r") as f:
                        mdData = f.read()
                        htmlData = FileConverter.md.convert(mdData)
                    if os.path.exists(outputfile):
                        print("outputファイルが既に存在しているので、上書きしました")            
                    with open(outputfile, "w") as f:
                        f.write(htmlData)
                except FileNotFoundError as f:
                    print("指定したファイルは存在しません. ファイルのpathを確認してください.", f)
                
            else:
                print("変換方法タイプ")
                
                
def main():
    FileConverter.convert()
    
if __name__ == "__main__":
    main()