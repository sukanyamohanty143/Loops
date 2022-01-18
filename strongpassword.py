password=input("enter your password:-")
c_l="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s_l="abcdefghijklmnopqrstuvwxyz"
num="0123456789"
sp_ch="@#₹&!*$%¢€£©®"
if len(password)>=8:
	i=0
	a=0
	b=0
	c=0
	d=0
	while i<len(password):
			if password[i] in c_l:
				a+=1
			elif password[i] in s_l:
				b+=1
			elif password[i] in num:
				c+=1
			elif password[i] in sp_ch:
				d+=1
			i+=1
	if a>=1 and b>=1 and c>=1 and d>=1:
		print("password is a strong password")
	else:
		print("password is not a strong password")
else:
	print("please enter 8 digit password")