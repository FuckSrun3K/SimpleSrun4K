import requests

column_key = [0,0,'d','c','j','i','h','g']
row_key = [
	['6','7','8','9',':',';','<','=','>','?','@','A','B','C','D','E'],
	['?','>','A','@','C','B','E','D','7','6','9','8',';',':','=','<'],
	['>','?','@','A','B','C','D','E','6','7','8','9',':',';','<','='],
	['=','<',';',':','9','8','7','6','E','D','C','B','A','@','?','>'],
	['<','=',':',';','8','9','6','7','D','E','B','C','@','A','>','?'],
	[';',':','=','<','7','6','9','8','C','B','E','D','?','>','A','@'],
	[':',';','<','=','6','7','8','9','B','C','D','E','>','?','@','A'],
	['9','8','7','6','=','<',';',':','A','@','?','>','E','D','B','C'],
	['8','9','6','7','<','=',':',';','@','A','>','?','D','E','B','C'],
	['7','6','8','9',';',':','=','<','?','>','A','@','C','B','D','E'],
]

def encrypt(string):
	i = 0;
	ret = ""
	for c in string:
		char_c = column_key[ord(c) >> 4]
		char_r = row_key[i%10][ord(c) & 0xf]
		if i%2:
			ret = ret + char_c + char_r
		else:
			ret = ret + char_r + char_c
		i = i + 1
	return ret

pwd='123456ab'
pwd = encrypt(pwd)
payload = {
		'action':'login',
		'username':1172201098,
		'password':pwd,
		'drop':0,
		'pop':0,
		'type':2,
		'n':117,
		'mbytes':0,
		'minutes':0,
		'ac_id':1
	}
header = {
		'user-agent':'pySrun4k'
	}
r = requests.post("http://202.204.67.15/cgi-bin/srun_portal",data=payload,headers=header)

