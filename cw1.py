def progression_outcome():
    cont="y"
    credit=[0,20,40,60,80,100,120]
    progress_count=(0)
    trailer_count=(0)
    retriever_count=(0)
    exclude_count=(0)
    while cont=="y":

        try:
            while True:
                
                global pass_credit
                pass_credit=int(input("please eneter you credits at pass:"))
                
                if pass_credit not in credit:
                    print("out of range")
                    break
            
                    
                global defer_credit
                defer_credit=int(input("please eneter you credits at defer:"))
               
                if defer_credit not in credit:
                    print("out of range")
                    break

                global fail_credit
                fail_credit=int(input("please eneter you credits at fail:"))
                print()
               
                if fail_credit not in credit:
                    print("out of range")
                    break
    
                break
                
            
        except ValueError:
            print("integer required")
            
        
        try:

            if (pass_credit)+(defer_credit)+(fail_credit)==120:
                            
                if pass_credit==120:
                    print("progress")
                    progress_count=progress_count+1
                    print()
                    
                    
                            
                while pass_credit==100:
                    print("progress(module trailer)")
                    trailer_count=trailer_count+1
                    print()
                    break
                    
                
                while (pass_credit>40 and pass_credit<100) and pass_credit>=(defer_credit+fail_credit):
                    print("do not progress-module retriever")
                    retriever_count=retriever_count+1
                    print()
                    break
                    
                   
                    
                while pass_credit<=40:
                    if fail_credit>=80:
                        print("exclude")
                        exclude_count=exclude_count+1
                        print()
                        break
                       
                    
                    else:
                        print("do not prgoress-module retriever")
                        retriever_count=retriever_count+1
                        print()
                        break
                        
                        
            else:       
                print("total incorrect")
                print()
                
                

        except NameError:
            print()
                    
                

        while True:
            
            next_set=input("Would you like to enter another set of data?\n" "enter 'y' for yes or 'q' to quit and view results:")
            print()
            if next_set=="y":
                break
        
            
                    
            elif next_set=="q":
                
                print()
                print("-"*60)   
                print("histogram\n")
                print("progress " , progress_count,":", (progress_count*"*"))
                print("trailer  ", trailer_count, ":", (trailer_count*"*"))
                print("retriever", retriever_count,":", (retriever_count*"*"))
                print("progress ", exclude_count,":", (exclude_count*"*"))
                total=(progress_count)+(trailer_count)+(retriever_count)+(exclude_count)
                print()
                print(total, "outcomes in total")
                print("-"*60)
                cont="n"
                
                break
                        
                    
            else:
                print("please enter valid choice")
                print()
        
        
                

progression_outcome()
                    
            
                  

    
