# Search Function    
def search(self, rn):
    for i in range(ls.__len__()):
        # iterate through the list containing
        # student object and checks through
        # roll no of each object
        if(ls[i].rollno == rn):
            # returns the object with matching 
            # roll number
            return i 