class Appearance:
    """
    Represents the appearance of a term in a given document, along with the
    frequency of appearances in the same one.
    """
    def __init__(self, docId, frequency):
        self.docId = docId
        self.frequency = frequency
    def __repr__(self):
        """
        String representation of the Appearance object
        """
        return str(self.__dict__)