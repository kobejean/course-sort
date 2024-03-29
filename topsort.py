EDIT_MODE = False
info = {
    # Foundation Courses (All required)
    # "CSCI 1000" : {
    #     "name" : "Computer Science as a Field of Work and Study",
    #     "credits" : 1,
    #     "prequisites" : [],
    #     "corequisites" : [],
    #     "completed" : False,
    # },
    "CSCI 1300" : {
        "name" : "Computer Science 1: Starting Computing",
        "credits" : 3,
        "prequisites" : [],
        "corequisites" : ["MATH 1300"], # ...
        "completed" : True,
    },
    "CSCI 2270" : {
        "name" : "Computer Science 2: Data Structures",
        "credits" : 4,
        "prequisites" : ["CSCI 1300", "MATH 1300"], # ...
        "corequisites" : [],
        "completed" : False,
    },
    "CSCI 2400" : {
        "name" : "Computer Systems",
        "credits" : 4,
        "prequisites" : ["CSCI 2270"], # ...
        "corequisites" : ["APPM 3170"], # ...
        "completed" : False,
    },
    "CSCI 3104" : {
        "name" : "Algorithms",
        "credits" : 4,
        "prequisites" : ["CSCI 2270", "MATH 2300", "APPM 3170"], # ...
        "corequisites" : [],
        "completed" : False,
    },
    "CSCI 3155" : {
        "name" : "Principles of Programming Languages",
        "credits" : 4,
        "prequisites" : ["CSCI 2270", "APPM 3170"], # ...
        "corequisites" : [],
        "completed" : False,
    },
    "CSCI 3308" : {
        "name" : "Software Development Methods and Tools",
        "credits" : 3,
        "prequisites" : ["CSCI 2270"], # ...
        "corequisites" : [],
        "completed" : False,
    },


    # Core Courses (Six of the following courses are required)

    # "CSCI 3002" : {
    #     "name" : "Human-Centered Computing Foundations/User-Centered Design & Development",
    #     "credits" : 1, # repeated up to 3 times
    #     "prequisites" : [], # 27-180 credits
    #     "corequisites" : [],
    #     "completed" : False,
    # },
    "CSCI 3202" : {
        "name" : "Introduction to Artificial Intelligence",
        "credits" : 3,
        "prequisites" : ["CSCI 2270", "MATH 4510", "APPM 3170"], # ...
        "corequisites" : [],
        "completed" : False,
    },
    "CSCI 3287" : {
        "name" : "Design and Analysis of Data Systems",
        "credits" : 3,
        "prequisites" : ["CSCI 3104"],
        "corequisites" : [],
        "completed" : False,
    },
    "CSCI 3302" : {
        "name" : "Introduction to Robotics",
        "credits" : 3,
        "prequisites" : ["CSCI 2270", "APPM 3170"], # ...
        "corequisites" : [],
        "completed" : False,
    },
    "CSCI 3434" : {
        "name" : "Theory of Computation",
        "credits" : 3,
        "prequisites" : ["CSCI 3104", "CSCI 3155"], # ...
        "corequisites" : [],
        "completed" : False,
    },
    "CSCI 3656" : {
        "name" : "Numerical Computation",
        "credits" : 3,
        "prequisites" : ["CSCI 1300", "MATH 1300", "MATH 2300", "MATH 2130"], # ...
        "corequisites" : [],
        "completed" : False,
    },
    # "CSCI 3702" : {
    #     "name" : "Cognitive Science",
    #     "credits" : 3,
    #     "prequisites" : ["PHIL 2440", "CSCI 1300"], # ...
    #     "corequisites" : [],
    #     "completed" : False,
    # },
    "CSCI 3753" : {
        "name" : "Design and Analysis of Operating Systems",
        "credits" : 4,
        "prequisites" : ["CSCI 2270", "CSCI 2400"], # ...
        "corequisites" : [],
        "completed" : False,
    },
    "CSCI 4229" : {
        "name" : "Computer Graphics",
        "credits" : 3,
        "prequisites" : ["CSCI 2270"], # ...
        "corequisites" : [],
        "completed" : False,
    },
    # "CSCI 4239" : {
    #     "name" : "Advanced Computer Graphics",
    #     "credits" : 3,
    #     "prequisites" : ["CSCI 4229"], # ...
    #     "corequisites" : [],
    #     "completed" : False,
    # },
    # "CSCI 4253" : {
    #     "name" : "Datacenter Scale Computing - Methods, Systems and Techniques",
    #     "credits" : 3,
    #     "prequisites" : ["CSCI 3753"], # 57-180 credits
    #     "corequisites" : [],
    #     "completed" : False,
    # },
    # "CSCI 4273" : {
    #     "name" : "Network Systems",
    #     "credits" : 3,
    #     "prequisites" : ["CSCI 3753"],
    #     "corequisites" : [],
    #     "completed" : False,
    # },
    "CSCI 4302" : {
        "name" : "Advanced Robotics",
        "credits" : 3,
        "prequisites" : ["CSCI 3302"],
        "corequisites" : [],
        "completed" : False,
    },
    # "CSCI 4413" : {
    #     "name" : "Computer Security and Ethical Hacking",
    #     "credits" : 3,
    #     "prequisites" : ["CSCI 2400", "CSCI 4273"],
    #     "corequisites" : [],
    #     "completed" : False,
    # },
    "CSCI 4446" : {
        "name" : "Chaotic Dynamics",
        "credits" : 3,
        "prequisites" : ["CSCI 1300", "MATH 2400"],
        "corequisites" : [],
        "completed" : False,
    },
    "CSCI 4448" : {
        "name" : "Object-Oriented Analysis and Design",
        "credits" : 3,
        "prequisites" : ["CSCI 3155", "CSCI 3308"],
        "corequisites" : [],
        "completed" : False,
    },
    # "CSCI 4502" : {
    #     "name" : "Data Mining",
    #     "credits" : 3,
    #     "prequisites" : ["CSCI 2270"],
    #     "corequisites" : [],
    #     "completed" : False,
    # },
    # "CSCI 4555" : {
    #     "name" : "Compiler Construction",
    #     "credits" : 3,
    #     "prequisites" : ["CSCI 3155", "CSCI 2400"],
    #     "corequisites" : [],
    #     "completed" : False,
    # },
    "CSCI 4576" : {
        "name" : "High-Performance Scientific Computing",
        "credits" : 4,
        "prequisites" : [],
        "corequisites" : [],
        "completed" : False,
    },
    # "CSCI 4586" : {
    #     "name" : "High-Performance Scientific Computing 2",
    #     "credits" : 4,
    #     "prequisites" : ["CSCI 4576"],
    #     "corequisites" : [],
    #     "completed" : False,
    # },
    # "CSCI 4586" : {
    #     "name" : "Computer Organization",
    #     "credits" : 3,
    #     "prequisites" : ["CSCI 2400"],
    #     "corequisites" : [],
    #     "completed" : False,
    # },
    "CSCI 4753" : {
        "name" : "Computer Performance Modeling",
        "credits" : 3,
        "prequisites" : ["CSCI 3753"],
        "corequisites" : [],
        "completed" : False,
    },
    # "CSCI 4809" : {
    #     "name" : "Computer Animation",
    #     "credits" : 3,
    #     "prequisites" : ["CSCI 3753"],
    #     "corequisites" : [],
    #     "completed" : False,
    # },
    # "CSCI 4830" : {
    #     "name" : "Special Topics in Computer Science",
    #     "credits" : 1,
    #     "prequisites" : ["CSCI 2400"],
    #     "corequisites" : [],
    #     "completed" : False,
    # },
    # "ECEN 2350" : {
    #     "name" : "Digital Logic",
    #     "credits" : 3,
    #     "prequisites" : ["CSCI 1300"],
    #     "corequisites" : [],
    #     "completed" : False,
    # },
# 62

    # Mathematics
    "APPM 3170" : {
        "name" : "Discrete Structures",
        "credits" : 3,
        "prequisites" : [],
        "corequisites" : ["MATH 2400"],
        "completed" : False,
    },
    "MATH 1300" : {
        "name" : "Calculus 1",
        "credits" : 4,
        "prequisites" : [],
        "corequisites" : [],
        "completed" : True,
    },
    "MATH 2300" : {
        "name" : "Calculus 2",
        "credits" : 4,
        "prequisites" : ["MATH 1300"],
        "corequisites" : [],
        "completed" : True,
    },
    # "MATH 2001" : {
    #     "name" : "Introduction to Discrete Mathematics",
    #     "credits" : 3,
    #     "prequisites" : ["MATH 1300"],
    #     "corequisites" : [],
    #     "completed" : False,
    # },
    "MATH 2130" : {
        "name" : "Introduction to Linear Algebra",
        "credits" : 3,
        "prequisites" : ["MATH 2300"],
        "corequisites" : [],
        "completed" : False,
    },
    # "MATH 3510" : {
    #     "name" : "Introduction to Probability and Statistics",
    #     "credits" : 3,
    #     "prequisites" : ["MATH 2001", "MATH 2300"],
    #     "corequisites" : [],
    #     "completed" : False,
    # },
    "MATH 4510" : {
        "name" : "Introduction to Probability Theory",
        "credits" : 3,
        "prequisites" : ["MATH 2400", "MATH 2130"],
        "corequisites" : [],
        "completed" : False,
    },

    # for math minor
    "MATH 2400" : {
        "name" : "Calculus 3",
        "credits" : 5,
        "prequisites" : ["MATH 2300"],
        "corequisites" : [],
        "completed" : False,
    },
    # "MATH 4650" : {
    #     "name" : "Intermediate Numerical Analysis 1",
    #     "credits" : 3,
    #     "prequisites" : ["MATH 2130"],
    #     "corequisites" : [],
    #     "completed" : False,
    # },

    # for math major
    # "MATH 3430" : {
    #     "name" : "Ordinary Differential Equations",
    #     "credits" : 3,
    #     "prequisites" : ["MATH 2400", "MATH 2130"],
    #     "corequisites" : [],
    #     "completed" : False,
    # },
    # "MATH 3001" : {
    #     "name" : "Analysis 1",
    #     "credits" : 3,
    #     "prequisites" : ["MATH 2001"],
    #     "corequisites" : [],
    #     "completed" : False,
    # },
    # "MATH 3140" : {
    #     "name" : "Abstract Algebra 1",
    #     "credits" : 3,
    #     "prequisites" : ["MATH 2001", "MATH 2130"],
    #     "corequisites" : [],
    #     "completed" : False,
    # },
    # "MATH 4140" : {
    #     "name" : "Abstract Algebra 2",
    #     "credits" : 3,
    #     "prequisites" : ["MATH 3140"],
    #     "corequisites" : [],
    #     "completed" : False,
    # },


    # Humanities and Social Sciences (24 credits)
    "HIST 1015" : {
        "name" : "American History to 1865",
        "credits" : 3,
        "prequisites" : [],
        "corequisites" : [],
        "completed" : True,
    },
    "ANTH 1999TC" : {
        "name" : "Intro to Cultural Anthropology",
        "credits" : 3,
        "prequisites" : [],
        "corequisites" : [],
        "completed" : True,
    },
    "PHIL 1000" : {
        "name" : "Introduction to Philosophy",
        "credits" : 3,
        "prequisites" : [],
        "corequisites" : [],
        "completed" : True,
    },
    # "PHIL 2440" : {
    #     "name" : "Symbolic Logic",
    #     "credits" : 3,
    #     "prequisites" : [],
    #     "corequisites" : [],
    #     "completed" : False,
    # },
    "ECON 2010" : {
        "name" : "Principles of Microeconomics",
        "credits" : 4,
        "prequisites" : [],
        "corequisites" : [],
        "completed" : False,
    },
    "ECON 2020" : {
        "name" : "Principles of Microeconomics",
        "credits" : 4,
        "prequisites" : ["ECON 2010"],
        "corequisites" : [],
        "completed" : False,
    },
    "CSCI 4250" : {
        "name" : "Computer Science: the Canon",
        "credits" : 3,
        "prequisites" : [], # 57-180 credits
        "corequisites" : [],
        "completed" : False,
    },
    "WRTG 3030" : {
        "name" : "Writing on Science and Society",
        "credits" : 3,
        "prequisites" : ["WRTG 1150"], # 57-180 credits
        "corequisites" : [],
        "completed" : False,
    },
    # "MATH 4820" : {
    #     "name" : "History of Mathematical Ideas",
    #     "credits" : 3,
    #     "prequisites" : ["MATH 2001", "MATH 2130"],
    #     "corequisites" : [],
    #     "completed" : False,
    # },

    # Computer Science Electives


    # Free electives (12 credits)
    "CSCI 4999TC" : {
        "name" : "Algorithms and Data Structures",
        "credits" : 3,
        "prequisites" : [],
        "corequisites" : [],
        "completed" : True,
    },
    "CSCI 2999" : {
        "name" : "Intro to Computer Science",
        "credits" : 3,
        "prequisites" : [],
        "corequisites" : [],
        "completed" : True,
    },
    "WRTG 1150" : {
        "name" : "First-Year Writing and Rhetoric",
        "credits" : 3,
        "prequisites" : [],
        "corequisites" : [],
        "completed" : True,
    },

    # Natural Science Requirements
    "PHYS 1110" : {
        "name" : "General Physics 1",
        "credits" : 4,
        "prequisites" : [],
        "corequisites" : ["MATH 1300"],
        "completed" : False,
    },
    "PHYS 1120" : {
        "name" : "General Physics 2",
        "credits" : 4,
        "prequisites" : ["PHYS 1110"],
        "corequisites" : ["MATH 2300"],
        "completed" : False,
    },
    "CHEM 1113" : {
        "name" : "General Chemistry 1",
        "credits" : 4,
        "prequisites" : [],
        "corequisites" : ["CHEM 1114"],
        "completed" : True,
    },
    "CHEM 1114" : {
        "name" : "Laboratory in General Chemistry 1",
        "credits" : 1,
        "prequisites" : [],
        "corequisites" : ["CHEM 1113"],
        "completed" : True,
    },
    "CHEM 1133" : {
        "name" : "General Chemistry 2",
        "credits" : 4,
        "prequisites" : ["CHEM 1113", "CHEM 1114"],
        "corequisites" : ["CHEM 1134"],
        "completed" : True,
    },
    "CHEM 1134" : {
        "name" : "Laboratory in General Chemistry 2",
        "credits" : 1,
        "prequisites" : ["CHEM 1113", "CHEM 1114"],
        "corequisites" : ["CHEM 1133"],
        "completed" : True,
    },

    # Senior Capstone
    "CSCI 3100" : {
        "name" : "Software and Society",
        "credits" : 1,
        "prequisites" : ["CSCI 3308"],
        "corequisites" : [],
        "completed" : False,
    },
    "CSCI 4950" : {
        "name" : "Senior Thesis",
        "credits" : 4,
        "prequisites" : ["WRTG 3030"], # Senior Year
        "corequisites" : ["CSCI 3100"],
        "completed" : False,
    },
}

cs_electives = []
cs_elective_credits = 0
for k, v in info.items():
    print(k, v["credits"], v["name"])
    if "CSCI" in k:
        cs_electives.append(k)

print("\n\n")

print("CS ELECTIVES:")
for course in cs_electives[:-5]:
    cs_elective_credits += info[course]["credits"]
    print(course, info[course]["credits"], info[course]["name"])
print("TOTAL CS ELECTIVE CREDITS:", cs_elective_credits)


print("\n\n")

def showSemester(info, courses):
    completed_credits = 0
    total_credits = 0
    unlocked_courses = []
    corequisites = set([])
    for k, v in info.items():
        total_credits += v["credits"]
        if v["completed"]:
            completed_credits += v["credits"]
        elif v["prequisites"]:
            if all([info[p]["completed"] for p in v["prequisites"]]):
                unlocked_courses.append(k)
                corequisites.update(v["corequisites"])
        else:
            unlocked_courses.append(k)
            corequisites.update(v["corequisites"])

    if EDIT_MODE:
        print("COMPLETED CREDITS:", completed_credits)
        print("TOTAL CREDITS:", total_credits)
        print("UNLOCKED COURSES:", unlocked_courses)
        print("COREQUISITES:", corequisites)
        print()

    semester_credits = 0
    for course in courses:
        if course in unlocked_courses or info[course]["completed"]:
            info[course]["completed"] = True
            semester_credits += info[course]["credits"]
            print(course, info[course]["credits"], info[course]["name"])
        else:
            raise Exception(course, "is not unlocked")
    print("SEMESTER CREDITS:", semester_credits)


    print("\n\n")

def showRemainder(info):
    for k, v in info.items():
        if not v["completed"]:
            print(k, v["credits"], v["name"])

print("- FALL 2016 -")
showSemester(info, ["WRTG 1150", "CSCI 2999", "ANTH 1999TC", "PHIL 1000"])

print("- SPRING 2017 -")
showSemester(info, ["CSCI 1300", "MATH 1300", "MATH 2300", "HIST 1015", "CSCI 4999TC"])

print("- SUMMER 2017 -")
showSemester(info, ["CHEM 1113", "CHEM 1114", "CHEM 1133", "CHEM 1134"])

print("- FALL 2017 -")
showSemester(info, ["APPM 3170", "CSCI 2270", "MATH 2130", "MATH 2400"])

print("- SPRING 2018 -")
showSemester(info, ["CSCI 2400", "CSCI 3104", "CSCI 3155", "CSCI 3308", "MATH 4510"])

print("- SUMMER 2018 -")
showSemester(info, ["ECON 2010"])

print("- FALL 2018 -")
showSemester(info, ["PHYS 1110", "CSCI 3434", "CSCI 3202", "CSCI 3287", "CSCI 3302"])

print("- SPRING 2019 -")
showSemester(info, ["WRTG 3030", "PHYS 1120", "CSCI 3753", "CSCI 3656", "CSCI 4446"])

print("- SUMMER 2019 -")
showSemester(info, ["ECON 2020"])

print("- FALL 2019 -")
showSemester(info, ["CSCI 4950", "CSCI 4250", "CSCI 4576", "CSCI 3100", "CSCI 4229"])

print("- SPRING 2020 -")
showSemester(info, ["CSCI 4950", "CSCI 4302", "CSCI 4753", "CSCI 4448"])

if EDIT_MODE:
    print("- REMAINDER -")
    showSemester(info, [])
    showRemainder(info)
