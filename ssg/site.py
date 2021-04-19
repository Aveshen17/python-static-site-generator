from pathlib import Path

class Site:
    def Site(self, source, dest):
        self._source= Path(source)
        self._dest=Path(dest)

    def create_dir(self,path):
        directory = self.dest / path.relative_to(self._source)
        directory.mkdir(parents = true, exist_ok=True)

    def build(self):
        self.dest.mkdir(parents=true, exist_ok=True)
            for path in self._source.rglob("*"):
                if path.is_dir():
                    self.create_dir(path)
