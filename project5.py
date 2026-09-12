temprutre=int(input("inter todays temprutre"))
if temprutre <18:
    activty=" some hot choclte"
    print("its cold out there use your jaket.")
    print("And do",activty)
else :
    activty="play outside with your frinds and stay cool"
    print("its a nice weather")
    print("go and",activty)


is_raing =input("is it raing?(yes/no):")
if is_raing=="yes":
    print("do some indoor activity")
    print("or use an umbrella and go outside")
else:
    print("thats way better")
    print("do an activity from your choice")


homwork_time=int(input("inter homwork time in minutes: "))

if homwork_time > 30:
    needs_break="yes"
    print("you have a long homwork today")
    print("take a short break before your",activty)
else:
    needs_break="no"
    print("you have a short homwork today")
    print("you dont need a break before your",activty)


has_free_time=input("do you have free time?(yes/no):")


if has_free_time=="yes":
    final_task="hobby time"
    print("you have free time today")
    print("enjoy your", final_task)
else:
    final_task="planning time"
    print("you dont have much free time today")
    print("use some time for",final_task)


    print("")
    print("daily activity check  complete for today!")

 
print("===== DAILY ACTIVITY PLANNER =====")
print("Study Break Needed:", needs_break)
print("Final Task:", final_task)
print("==================================")


     