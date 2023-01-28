class Class():
    def __init__(self, code = "", title = "", pre_req = "") -> None:
        self.code = code
        self.title = title
        self.pre_req = pre_req


    ##############  Getters and Setters ###################
    def add_pre_req(self, class_code) -> None:
        """
        Parameter: str
        Return: None
        This function adds to the list of pre-reqs this
        specific class needs
        """
        self.pre_req.append(class_code)

    def set_title(self, title) -> None:
        """
        Parameter: str
        Return: None
        This function sets this instances class title.
        """
        self.title = title

    def set_code(self, class_code):
        """
        Parameter: str
        Return: None
        This function sets this instances class code.
        """
        self.code = class_code

    def class_code(self):
        """
        Parameter: None
        Return: None
        This function returns this instances class code.
        """
        return self.code

    def class_title(self):
        """
        Parameter: None
        Return: None
        This function returns this instances class title.
        """
        return self.title

    def class_reqs(self):
        """
        Parameter: None
        Return: None
        This function returns this instances class reqs.
        """
        return self.pre_req

class Semester(Class):
    def __init__(self) -> None:
        self.schedule = []

    def sched(self) -> list:
        """
        Parameters: None
        Return: list
        Tthis function returns a list containing classes for this semester
        """
        return self.schedule

    def add_class(self, new_class) -> None:
        """
        Parameters: Class instance
        Return: None
        This function updates this semesters classes
        """

        if isinstance(new_class, Class) == False:
            raise Exception("Must be an instance of class 'Class'")

        self.schedule.append(new_class)

class Total_Required(Semester):

    def __init__(self) -> None:
        self.classes_needed = []
        self.classes_have = []
        self.all_semesters = []
        self.total_Required_Creds = 0
        self.creds_Possesed = 0

    ##############  Getters and Setters ###################

    def set_total_creds(self, val) -> None:
        """
        Parameters: int
        Return: None
        This function sets the total required credits you need
        to graduate
        """
        self.total_Required_Creds = val

    def set_creds_possesed(self, val) -> None:
        """
        Parameters: int
        Return: None
        This function sets the number of credits you posses in your
        schedule
        """
        self.creds_Possesed = val

    def need_to_have(self, class_code) -> bool:
        """
        Parameter: str
        Return: bool
        This function moves a class from the "need to schedule" group
        to the "scheduled" group. It returns True based off its success
        """
        if self.classes_needed.index(class_code):
            self.classes_needed.remove(self.classes_needed.index(class_code))
            self.class_have.append(class_code)
            return True

        return False

    def classes_need(self) -> list:
        """
        Parameters: None
        Return: list
        This function is simply a helper function to acquire which classes 
        that still need to be scheduled
        """
        return self.classes_needed
    
    def class_have(self) -> list:
        """
        Parameters: None
        Return: list
        This function is simply a helper function to acquire which
        classes that have already been scheduled
        """
        return self.classes_have

    def creds_needed(self) -> int:
        """
        Parameters: None
        Return: int
        This function calculates the amount of credits you still
        need to schedule
        """
        return self.total_Required_Creds - self.creds_Possesed

    def tot_creds(self) -> int:
        """
        Parameters: None
        Return: int
        This function returns the total credits you need for your major.
        """
        return self.total_Required_Creds

    def pos_creds(self) -> int:
        """
        Parameters: None
        Return: int
        This function returns the amount of credits you have scheduled
        """
        return self.creds_Possesed

    def add_sem_to_total(self, semester) -> None:
        """
        Parameter: Semester instance
        Return: None
        This function adds semesters to the overarching schedule
        """

        if isinstance(semester, Semester) == False:
            raise Exception("Input must be an instance of 'Semester'")

        self.all_semesters.append(semester)

    ############      Helper Functions       ################
    def req_met(self, class_code) -> bool:
        """
        Paramters: str
        Return: bool
        This function will iterate through all semesters to find if 
        a class was already in the scheduled and return a bool based off success. 
        Ideally used for search of pre-reqs. 
        """
        for semester in self.all_semesters:
            for v in semester.sched():
                if v.class_code() == class_code:
                    return True
        
        return False

all = Total_Required()
s1 = Semester()
c1 = Class("CSE 331", "Data Structures")
c2 = Class("CSE 232", "Intro to Programming II")
all.add_sem_to_total(s1)
s1.add_class(c1)
s1.add_class(c2)

print(all.req_met("CSE 232"))
print("finish")