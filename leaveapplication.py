date=(input("enter today date:"))
place=(input("enter the place:"))
name=(input("enter your name:"))
classname=(input("enter your classname:"))
section=(input("enter your section:"))
schoolname=(input("enter your schoolname:"))
classteachername=(input("enter your class teacher name:"))
subject=(input("enter the subject:"))
reason=(input("enter the reason for leave:"))
noofleavedays=(input("enter no of leave days:"))
dateofleave=(input("enter the date of leave:"))
leaveletter=f'''
                 
                                     Leave Letter

From                                                                                 Date:{date} 
        {name}
        {classname}{section}
        {schoolname}
        {place}

To
        {classteachername}
        {classname}{section}
        {schoolname}
        {place}

Respected Sir/Madam  
             sub:{subject}
                      I am {name}. Studying in {classname} {section}. I am unable to attend my class  
due to {reason}.I want the permission to take a leave for {noofleavedays} days {dateofleave} . please 
accept my leave application and grant me a leave.
                              Thankyou
                                                                         your's faithfully
                                                                             {name}                                                                         
'''
print(leaveletter)

