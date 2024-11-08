class Project:
    def __init__(self, name, description,authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, items):
        multistring = "\n"

        for item in items:
            multistring += f"- {item}\n"

        return multistring if len(items) > 0 else "-"
    
    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\n\nAuthors: {self._stringify_dependencies(self.authors)}"
            f"\nDependencies: {self._stringify_dependencies(self.dependencies)}"
            f"\nDevelopment dependencies: {self._stringify_dependencies(self.dev_dependencies)}"
        )