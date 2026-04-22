
#calculator mini project
# persons
# cleaning
# rent 
# electricity bill
# per unit charg
# total food order gor snacking

persons=int(input("enter total number of person ="))
rent=int(input("enter a total rent ="))
cleaning=int(input("enter a cleaning amount ="))
electicity_spend=int(input("enter a total electricity spente ="))
charg_pir_unit=int(input("input a amount of charg pir unit ="))
food=int(input("enter the amount of food order ="))

tatal_bill = electicity_spend * charg_pir_unit

output=(food+rent+cleaning+tatal_bill) / persons

print("each person will pay =" , output)
