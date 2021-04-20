from pathlib import Path

class Site:


    def __init__(self, source, dest, parsers=None):
        self._source= Path(source)
        self._dest=Path(dest)
        self.parsers=parsers or []

    def create_dir(self,path):
        directory = self.dest / path.relative_to(self._source)
        directory.mkdir(parents = true, exist_ok=True)

    def build(self):
        self.dest.mkdir(parents=true, exist_ok=True)
        for path in self._source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)
            if path.is_file():
                self.run_parser(path)


    def load_parser(extension):
        for parser in self.parsers:
            if parser.valid_extension(extension):
                return parser

    def run_parser(self, path):
        parser = self.load_parser(path.suffix)
        if parser is not None:
            parser.parse(Path,self.source, self.dest)
        else:
            print ( "not implemented")
