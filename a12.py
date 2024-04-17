class Author:
    def __init__(self, full_name, family_name, given_name, author_order):
        self.full_name = full_name
        self.family_name = family_name
        self.given_name = given_name
        self.author_order = author_order

    def __str__(self):
        return f"{self.full_name}\t{self.family_name}\t{self.given_name}\t{self.author_order}"


class Affiliation:
    def __init__(self, name, department, institution):
        self.name = name
        self.department = department
        self.institution = institution

    def __str__(self):
        return f"{self.name}\t{self.department}\t{self.institution}"


class Reference:
    def __init__(self, reference_id, title, year, journal):
        self.reference_id = reference_id
        self.title = title
        self.year = year
        self.journal = journal

    def __str__(self):
        return f"{self.reference_id}\t{self.title}\t{self.year}\t{self.journal}"


class PaperBasicInfo:
    def __init__(self, year, journal, issn, doi, issue, volume):
        self.year = year
        self.journal = journal
        self.issn = issn
        self.doi = doi
        self.issue = issue
        self.volume = volume

    def __str__(self):
        return f"{self.year}\t{self.journal}\t{self.issn}\t{self.doi}\t{self.issue}\t{self.volume}"


class PaperAbstract:
    def __init__(self, abstract_text):
        self.abstract_text = abstract_text

    def __str__(self):
        return self.abstract_text


class PaperTitle:
    def __init__(self, title_text):
        self.title_text = title_text

    def __str__(self):
        return self.title_text


class Paper:
    def __init__(self, ut):
        self.ut = ut
        self.basic_info = PaperBasicInfo(None, None, None, None, None, None)
        self.abstract = PaperAbstract(None)
        self.title = PaperTitle(None)
        self.authors = []
        self.affiliations = []
        self.references = []

    def add_author(self, author):
        self.authors.append(author)

    def add_affiliation(self, affiliation):
        self.affiliations.append(affiliation)

    def add_reference(self, reference):
        self.references.append(reference)

    def write_to_txt(self, file_path):
        with open(file_path, 'w') as file:
            file.write(f"UT: {self.ut}\n")
            file.write(f"Title: {self.title}\n")
            file.write(f"Abstract: {self.abstract}\n")
            file.write(f"BasicInfo: {self.basic_info}\n")
            file.write("Authors:\n")
            for author in self.authors:
                file.write(f"{author}\n")
            file.write("Affiliations:\n")
            for affiliation in self.affiliations:
                file.write(f"{affiliation}\n")
            file.write("References:\n")
            for reference in self.references:
                file.write(f"{reference}\n")

    @staticmethod
    def read_from_txt(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()

        ut = lines[0].strip