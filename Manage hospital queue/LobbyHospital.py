# การเข้าคิวรับการรักษาในโรงพยาบาล
# - เข้ารับการรักษาแบบโดยใช้ ชื่อ และความอันตราย เเล้วชื่อจะไปอยู่ในคิวของความอันตรายนั้น
# - จะทำการเรียกคิวที่มีระดับความอันตรายมมากว่ามารับการรักษาก่อน เรียงจาก แดง -> เหลือง -> เขียว
# - มีฟังก์ชัน search ในการค้นหาว่ามีชื่ออยู่ในคิวไหม
# - มีฟังก์ชัน delete ในการลบคิวผู้ที่รับการรักษาให้ออกจากระบบ และ คิวที่เรียกเกิน3ครั้ง
# - มีฟังก์ชันในการเเสดงคิวที่มีอยู่ในตอนนี้
# - มีฟังก์ชันในการเเสดงจำนวนของคิวที่มีอยู่ในตอนนี้

from hospital import Hospital,HospitalAR,Node
RedC = Hospital()
YellowC = Hospital()
GreenC = Hospital()
ar = HospitalAR()
while True :
        #case = str(input("\n1.Red case\n2.Yellow case\n3.Green case\n\nChoose which case you would like. : ""))
        ans = str(input("\n1.Add queue\n2.Show queue\n3.User in queue\n4.Queue Next\nPlease Enter a number from the list\nchoose the list you want : "))
        print('\n')

        if ans in ar.AddQ : 
                #เพิ่มชื่อในคิว
                #เลือกระดับความอันตราย
                print('\n1.Red = Severe symptoms require urgent treatment.\n2.Yellow = Moderate severity can wait for treatment\n3.Green = The least severe symptoms can wait to be treated.')
                case = str(input("\nPlease choose the color according to user symptoms \nby Enter number front of list you want : "))
                if case in ar.STOP:
                        pass
                UserNamein = str(input("Please Enter User name : "))
                if case in ar.Red :
                        RedC.insertAtEnd(UserNamein)
                        print('\n ' + UserNamein +' '+' in queue red case\n')

                elif case in ar.Yellow :
                        YellowC.insertAtEnd(UserNamein)
                        print('\n ' + UserNamein +' '+' in queue yellow case\n')

                elif case in ar.Green :
                        GreenC.insertAtEnd(UserNamein)
                        print('\n ' + UserNamein +' '+' in queue green case\n')

                elif UserNamein in ar.STOP:
                        pass

                else :
                        print('invalid input\nPlease try again \n///////////////////\n\n')
                        continue

        elif ans in ar.ShowQ :
                #แสดงคิวทั้งหมด
                print("Red case -> "),RedC.printListLoop()

                print("Yellow case -> "),YellowC.printListLoop()

                print("Green case -> "),GreenC.printListLoop()

                #ขนานของคิว
                print("Red case queue is : "),print(RedC.numberQ())

                print("Yellow case queue is : "),print(YellowC.numberQ())

                print("Green case queue  is : "),print(GreenC.numberQ())

                print('All of queue is : '),print(GreenC.numberQ()+YellowC.numberQ()+RedC.numberQ())


        elif ans in ar.UserInQ :
                #ตรวจสอบว่ามีผู้ใช้ชื่อนั้นๆอยู่ในคิวหรือไม่
                SearchUserInQ = str(input("Please Enter User name : "))
                if RedC.search(SearchUserInQ) == True:
                        UserIndex = RedC.searchIndex(SearchUserInQ)
                        print('User name : '+ SearchUserInQ +' in red case queue')
                        print('At index : '+ str(UserIndex+1))

                elif YellowC.search(SearchUserInQ) == True:
                        UserIndex = YellowC.searchIndex(SearchUserInQ)
                        print('User name : '+ SearchUserInQ +' in yellow case queue')
                        print('At index : '+ str(UserIndex+1))

                elif GreenC.search(SearchUserInQ) == True:
                        UserIndex = YellowC.searchIndex(SearchUserInQ)
                        print('User name : '+ SearchUserInQ +' in green case queue')
                        print('At index : '+ str(UserIndex+1))
                
                elif SearchUserInQ in ar.STOP:
                        pass 

                elif GreenC.head == None and YellowC.head == None and RedC.head == None :
                        print("Dont hane queue")
                else :
                        print('Dont have user name : '+ SearchUserInQ +' in queue')
        
        elif ans in ar.QNext :
                #เรียกคิว
                if RedC.head != None:
                                UserSure1 = str(input("Please Enter User Sure Y/N: "))
                                if UserSure1 in ar.Y:
                                        RedC.printListHead(RedC.head)
                                        print('ได้รับการรักษาแล้ว')
                                        RedC.deleteHead()
                                #ถ้าเรียกคิวแล้ว3ครั้งไม่มาทำการลบออกจากคิว
                                elif UserSure1 in ar.N:
                                        #เรียกครั้งที่ 1
                                        RedC.printListHead(RedC.head)    
                                        UserSure2 = str(input("Please Enter User Sure Y/N: "))
                                        if UserSure2 in ar.Y:
                                                RedC.printListHead(RedC.head)
                                                print('ได้รับการรักษาแล้ว')
                                                RedC.deleteHead()
                                        elif UserSure2 in ar.N:
                                                #เรียกครั้งที่ 2
                                                RedC.printListHead(RedC.head)
                                                UserSure3 = str(input("Please Enter User Sure Y/N: "))
                                                if UserSure3 in ar.Y:
                                                        RedC.printListHead(RedC.head)
                                                        print('ได้รับการรักษาแล้ว')
                                                        RedC.deleteHead()
                                                elif UserSure3 in ar.N:
                                                        #เรียกครั้งที่ 3
                                                        RedC.printListHead(RedC.head)
                                                        RedC.deleteHead()
                                                else :
                                                        pass
                                        else :
                                                pass
                                else :
                                        pass

                
                elif RedC.head == None:
                        if YellowC.head != None:
                                UserSure1 = str(input("Please Enter User Sure Y/N: "))
                                if UserSure1 in ar.Y:
                                        YellowC.printListHead(YellowC.head)
                                        print('ได้รับการรักษาแล้ว')
                                        YellowC.deleteHead()
                                #ถ้าเรียกคิวแล้ว3ครั้งไม่มาทำการลบออกจากคิว
                                elif UserSure1 in ar.N:
                                        #เรียกครั้งที่ 1
                                        YellowC.printListHead(YellowC.head)    
                                        UserSure2 = str(input("Please Enter User Sure Y/N: "))
                                        if UserSure2 in ar.Y:
                                                YellowC.printListHead(YellowC.head)
                                                print('ได้รับการรักษาแล้ว')
                                                YellowC.deleteHead()
                                        elif UserSure2 in ar.N:
                                                #เรียกครั้งที่ 2
                                                YellowC.printListHead(YellowC.head)
                                                UserSure3 = str(input("Please Enter User Sure Y/N: "))
                                                if UserSure3 in ar.Y:
                                                        YellowC.printListHead(YellowC.head)
                                                        print('ได้รับการรักษาแล้ว')
                                                        YellowC.deleteHead()
                                                elif UserSure3 in ar.N:
                                                        #เรียกครั้งที่ 3
                                                        YellowC.printListHead(YellowC.head)
                                                        YellowC.deleteHead()
                                                else :
                                                        pass
                                        else :
                                                pass
                                else :
                                        pass   

                        elif YellowC.head == None:
                                if GreenC.head!= None:
                                        GreenC.printListHead(GreenC.head)
                                        UserSure1 = str(input("Please Enter User Sure Y/N: "))
                                        if UserSure1 in ar.Y:
                                                GreenC.printListHead(GreenC.head)
                                                print('ได้รับการรักษาแล้ว')
                                                GreenC.deleteHead()
                                        #ถ้าเรียกคิวแล้ว3ครั้งไม่มาทำการลบออกจากคิว
                                        elif UserSure1 in ar.N:
                                                #เรียกครั้งที่ 1
                                                GreenC.printListHead(GreenC.head)    
                                                UserSure2 = str(input("Please Enter User Sure Y/N: "))
                                                if UserSure2 in ar.Y:
                                                        GreenC.printListHead(GreenC.head)
                                                        print('ได้รับการรักษาแล้ว')
                                                        GreenC.deleteHead()
                                                elif UserSure2 in ar.N:
                                                        #เรียกครั้งที่ 2
                                                        GreenC.printListHead(GreenC.head)
                                                        UserSure3 = str(input("Please Enter User Sure Y/N: "))
                                                        if UserSure3 in ar.Y:
                                                                GreenC.printListHead(GreenC.head)
                                                                print('ได้รับการรักษาแล้ว')
                                                                GreenC.deleteHead()
                                                        elif UserSure3 in ar.N:
                                                                #เรียกครั้งที่ 3
                                                                GreenC.printListHead(GreenC.head)
                                                                GreenC.deleteHead()
                                                        else :
                                                                pass
                                                else :
                                                        pass
                                        else :
                                                pass

                                elif GreenC.head== None:
                                        print('Dont have queue')

        elif ans in ar.STOP : 
                print('Stop working')
                break

        else : 
                print('invalid input\nPlease try again \n///////////////////\n\n')
                continue