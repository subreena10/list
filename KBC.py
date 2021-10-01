question_list=["1.Taj Mahal is the symbol of ----?",
                "2.what is the capital of india?",
                "3.which course is teaching in NG?"
]
option_list=[["love","laathe","honour","respect"],
             ["kashmir","mumbai","delhi","gujarat"],
             ["tourism","cultural","software engineering","agricultural"]]
solution_list=["1","3","3"]
answere_list=[["1.love","2.laathe"],
               ["1.kashmir","3.delhi"],
               ["3.softaware engineering","2.tourism"]]

print("***🙏welcome to kon banaga codepati🙏***")
question=input("Do u want to participate? ")
if question=="yes":
    print("Let's start the KBC.🙂WISH U BEST LUCK🙂")
    print()
i=0
count=0
prize=1000
while i<len(question_list):
    print(question_list[i])
    j=0
    k=1
    
    while j<len(option_list[i]):
        print(k,".",option_list[i][j])
        j+=1
        k=k+1
       
    lfln=input("Do you want to use 50 50 lifeline? ")
    if lfln=="yes":
        print("50 50 lifeline: ")
        if count<1:
            print(answere_list[i])
            user=input("Choose the option given above: ")
            if user==solution_list[i]:
                
                print("Right answere,YOUR account is credited rs",prize)
                
    
            else:
                print("WRONG answere😞")
                break
            
            count=count+1
            print()
        else:
            print()
            print("you have already used lifeline.🤫")
            print()
            user1=input("choose the option: ")
            if user1==solution_list[i]:
                print("RIGHT ans,YOUR aacount is credited  rupees.",prize)
                
            else:
                print("WRONG ANS😞")
                print("😕YOU LOST THE CHANCE!!!")
                break
            print()
    else:
        print("")
        user2=input("Choose the option: ")
        if user2==solution_list[i]:
            print("RIGHT ANS,YOUR account is credited rupees.",prize)
            print(" 🎉 YOU ARE  WINNER OF THE  KBC GAME 🎉 ***CONGRATULATIONS***")
        else:
            print("😞YOU MISS THE CHANCE!!! WRONG ANS...WISH YOU BEST LUCK  NEXT TIME👍")
            break
    prize=prize+1000
    i+=1
    print()
candiate_user=input("do you want to add a question? ")
if candiate_user=="yes":
    print("you can add a quetion")
    question1=input("Add a question: ")
    question_list.append ([question1])
    print(question_list)
    print()
    option1=input("Enter the 4 option:")
    option_list.append([option1])
    print(option_list)
    solution1=input("Enter your solution:")
    solution_list.append(solution1)
    print(solution_list)
    ans=input("enter ur answere: ")
    answere_list.append([ans])
    print(answere_list)
