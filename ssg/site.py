from pathlib import path 

class Site():
    def __init__(self,source,dest):
        self.source = source
        self.dest = dest
        self.source = path()
        self.dest = path()

    def create_dir(self,path):
        directory = self.dest / path.relativeto(self.source)
        directory.mkdir(parents=True, exist_ok=True)

    def build():
        self.dest.mkdir(parents=True , exist_ok=True)
        for path in self.source.rglob("*"):
            if path.isdir():
                self.create_dir(path)
            
         
