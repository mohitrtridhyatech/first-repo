vehicle_val = float(input('Enter vehicle value:'))

#n = int(input('Select option:\n1: Direct payment \n2: EMI\n'))

#if(n==1):
#premium = vehicle_val*5/100
#print('Premium rate:',premium)
premium_rate = 5
premium_amount = (vehicle_val*premium_rate)/100
print('\npremium amount:',premium_amount)

personal_acc_cover = 0
hospital_cash_cover = 0
loss_of_use = 0.25
#print('loss of use:',loss_of_use)

loss_of_use_cover_premium = (vehicle_val*loss_of_use)/100
print('loss of use cover premium:',loss_of_use_cover_premium)

excess_protector = 0.25
print('excess protector:',excess_protector)

excess_protector_premium = (vehicle_val*excess_protector)/100
print('excess protector premium:',excess_protector_premium)

premium_sum = premium_amount+personal_acc_cover+hospital_cash_cover+loss_of_use_cover_premium+excess_protector_premium
print('Premium sum:',premium_sum)

levies = 0.45
#print('levies:',levies)

levies_amount = vehicle_val*levies/100
print('levies amount:',levies_amount)

stamp_duty_amount = 50
print('stamp duty:',stamp_duty_amount)

premium_with_taxes = premium_sum+levies_amount+stamp_duty_amount
print('\npremium with taxes:',premium_with_taxes)


n = int(input('Select option:\n1: Direct payment \n2: EMI\n'))

if(n==1):
	print('Your total payable amount is:',premium_with_taxes)
elif(n==2):
	interest_rate = 5
	interest_charge = (premium_with_taxes*interest_rate)/100
	print('\nInterest charge:',interest_charge)

	facility_fees_amount = 500
	print('Facility fees amount:',facility_fees_amount)

	exise_duty = 2
	exice_duty_amount = (facility_fees_amount*exise_duty)/100
	print('Exice duty amount:',exice_duty_amount)

	total_payable = premium_with_taxes+interest_charge+facility_fees_amount+exice_duty_amount
	print('Total payable:',total_payable)

	downpayment_rate = 10
	downpayment = total_payable*downpayment_rate/100
	print('Downpayment:',downpayment)

	net_balance = total_payable-downpayment
	print('Net balance:',net_balance)

	no_of_installments = 21
	monthly_installments = net_balance/no_of_installments
	print('Monthly installments:',monthly_installments)

	commission_rate = 10
	commission_amount = premium_sum*commission_rate/100
	print('Commission amount:',commission_amount)


