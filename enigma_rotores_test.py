#Enigma Encoder - www.101computing.net/enigma-encoder/

# ----------------- Enigma Settings -----------------
rotors = ("I","II","III")
reflector = "UKW-B"
ringSettings ="AAA"
ringPositions = "AAA" 
plugboard = "AB CD"
# ---------------------------------------------------

def caesarShift(str, amount):
	output = ""

	for i in range(0,len(str)):
		c = str[i]
		code = ord(c)
		if ((code >= 65) and (code <= 90)):
			c = chr(((code - 65 + amount) % 26) + 65)
		output = output + c
	
	return output

def encode(plaintext):
  global rotors, reflector,ringSettings,ringPositions,plugboard
  #Enigma Rotors and reflectors
  rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
  rotor1Notch = "Q"
  rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
  rotor2Notch = "E"
  rotor3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
  rotor3Notch = "V"
  rotor4 = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
  rotor4Notch = "J"
  rotor5 = "VZBRGITYUPSDNHLXAWMJQOFECK"
  rotor5Notch = "Z" 
  
  rotorDict = {"I":rotor1,"II":rotor2,"III":rotor3,"IV":rotor4,"V":rotor5}
  rotorNotchDict = {"I":rotor1Notch,"II":rotor2Notch,"III":rotor3Notch,"IV":rotor4Notch,"V":rotor5Notch}  
  
  reflectorB = {"A":"Y","Y":"A","B":"R","R":"B","C":"U","U":"C","D":"H","H":"D","E":"Q","Q":"E","F":"S","S":"F","G":"L","L":"G","I":"P","P":"I","J":"X","X":"J","K":"N","N":"K","M":"O","O":"M","T":"Z","Z":"T","V":"W","W":"V"}
  reflectorC = {"A":"F","F":"A","B":"V","V":"B","C":"P","P":"C","D":"J","J":"D","E":"I","I":"E","G":"O","O":"G","H":"Y","Y":"H","K":"R","R":"K","L":"Z","Z":"L","M":"X","X":"M","N":"W","W":"N","Q":"T","T":"Q","S":"U","U":"S"}
  
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  rotorANotch = False
  rotorBNotch = False
  rotorCNotch = False
  
  if reflector=="UKW-C":
    reflectorDict = reflectorB
  else:
    reflectorDict = reflectorC
  
  #A = Left,  B = Mid,  C=Right 
  rotorA = rotorDict[rotors[0]]
  rotorB = rotorDict[rotors[1]]
  rotorC = rotorDict[rotors[2]]
  rotorANotch = rotorNotchDict[rotors[0]]
  rotorBNotch = rotorNotchDict[rotors[1]]
  rotorCNotch = rotorNotchDict[rotors[2]]
  
  rotorALetter = ringPositions[0]
  rotorBLetter = ringPositions[1]
  rotorCLetter = ringPositions[2]
  
  rotorASetting = ringSettings[0]
  offsetASetting = alphabet.index(rotorASetting)
  rotorBSetting = ringSettings[1]
  offsetBSetting = alphabet.index(rotorBSetting)
  rotorCSetting = ringSettings[2]
  offsetCSetting = alphabet.index(rotorCSetting)
  
  rotorA = caesarShift(rotorA,offsetASetting)
  rotorB = caesarShift(rotorB,offsetBSetting)
  rotorC = caesarShift(rotorC,offsetCSetting)
  
  if offsetASetting>0:
    rotorA = rotorA[26-offsetASetting:] + rotorA[0:26-offsetASetting]
  if offsetBSetting>0:
    rotorB = rotorB[26-offsetBSetting:] + rotorB[0:26-offsetBSetting]
  if offsetCSetting>0:
    rotorC = rotorC[26-offsetCSetting:] + rotorC[0:26-offsetCSetting]

  ciphertext = ""
  
  #Converplugboard settings into a dictionary
  plugboardConnections = plugboard.upper().split(" ")
  plugboardDict = {}
  for pair in plugboardConnections:
    if len(pair)==2:
      plugboardDict[pair[0]] = pair[1]
      plugboardDict[pair[1]] = pair[0]
  
  plaintext = plaintext.upper()  
  for letter in plaintext:
    encryptedLetter = letter  
    
    if letter in alphabet:
      #Rotate Rotors - This happens as soon as a key is pressed, before encrypting the letter!
      rotorTrigger = False
      #Third rotor rotates by 1 for every key being pressed
      if rotorCLetter == rotorCNotch:
        rotorTrigger = True 
      rotorCLetter = alphabet[(alphabet.index(rotorCLetter) + 1) % 26]
      #Check if rotorB needs to rotate
      if rotorTrigger:
        rotorTrigger = False
        if rotorBLetter == rotorBNotch:
          rotorTrigger = True 
        rotorBLetter = alphabet[(alphabet.index(rotorBLetter) + 1) % 26]
  
        #Check if rotorA needs to rotate
        if (rotorTrigger):
          rotorTrigger = False
          rotorALetter = alphabet[(alphabet.index(rotorALetter) + 1) % 26]
      		 
      else:
          #Check for double step sequence!
        if rotorBLetter == rotorBNotch:
          rotorBLetter = alphabet[(alphabet.index(rotorBLetter) + 1) % 26]
          rotorALetter = alphabet[(alphabet.index(rotorALetter) + 1) % 26]
        
      #Implement plugboard encryption!
      if letter in plugboardDict.keys():
        if plugboardDict[letter]!="":
          encryptedLetter = plugboardDict[letter]
    
      #Rotors & Reflector Encryption
      offsetA = alphabet.index(rotorALetter)
      offsetB = alphabet.index(rotorBLetter)
      offsetC = alphabet.index(rotorCLetter)

      # Wheel 3 Encryption
      pos = alphabet.index(encryptedLetter)
      let = rotorC[(pos + offsetC)%26]
      pos = alphabet.index(let)
      encryptedLetter = alphabet[(pos - offsetC +26)%26]
      
      # Wheel 2 Encryption
      pos = alphabet.index(encryptedLetter)
      let = rotorB[(pos + offsetB)%26]
      pos = alphabet.index(let)
      encryptedLetter = alphabet[(pos - offsetB +26)%26]
      
      # Wheel 1 Encryption
      pos = alphabet.index(encryptedLetter)
      let = rotorA[(pos + offsetA)%26]
      pos = alphabet.index(let)
      encryptedLetter = alphabet[(pos - offsetA +26)%26]
      
      # Reflector encryption!
      if encryptedLetter in reflectorDict.keys():
        if reflectorDict[encryptedLetter]!="":
          encryptedLetter = reflectorDict[encryptedLetter]
      
      #Back through the rotors 
      # Wheel 1 Encryption
      pos = alphabet.index(encryptedLetter)
      let = alphabet[(pos + offsetA)%26]
      pos = rotorA.index(let)
      encryptedLetter = alphabet[(pos - offsetA +26)%26] 
      
      # Wheel 2 Encryption
      pos = alphabet.index(encryptedLetter)
      let = alphabet[(pos + offsetB)%26]
      pos = rotorB.index(let)
      encryptedLetter = alphabet[(pos - offsetB +26)%26]
      
      # Wheel 3 Encryption
      pos = alphabet.index(encryptedLetter)
      let = alphabet[(pos + offsetC)%26]
      pos = rotorC.index(let)
      encryptedLetter = alphabet[(pos - offsetC +26)%26]
      
      #Implement plugboard encryption!
      if encryptedLetter in plugboardDict.keys():
        if plugboardDict[encryptedLetter]!="":
          encryptedLetter = plugboardDict[encryptedLetter]

    ciphertext = ciphertext + encryptedLetter
  
  return ciphertext

#Main Program Starts Here
print("  ##### Enigma Encoder #####")
print("")
plaintext = input("Enter text to encode or decode:\n")
print("")

#ciphertext = encode(plaintext)

#print("\nEncoded text: \n " + ciphertext)

contador = 17575*17575*17575


texto_buscado_1 = "RAFAEL"
texto_buscado_2 = "NADAL"
texto_buscado_3 = "FUERA"
texto_buscado_4 = "SERIA"


ring_test = ""
ring_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ring_1 = 'A'
ring_1_pos = 0
ring_2 = 'A'
ring_2_pos = 0
ring_3 = 'A'
ring_3_pos = 0

ringPos_1 = 'A'
ringPos_1_pos = 0
ringPos_2 = 'A'
ringPos_2_pos = 0
ringPos_3 = 'A'
ringPos_3_pos = 0


rotor_test = []

rotores = ["I","II","III","IV","V"]

rotor1 = 0
rotor2 = 0
rotor3 = 0

rotor_test.append(rotores[rotor1])
rotor_test.append(rotores[rotor2])
rotor_test.append(rotores[rotor3])

rotors = rotor_test

while contador != 0:


	ringSettings = ring_1+ring_2+ring_3
	ringPositions = ringPos_1+ringPos_2+ringPos_3
	rotors = rotor_test

	#print(rotors,ringSettings,ringPositions,contador)

	contador -= 1

	ring_3_pos += 1

	if ring_3_pos > 25:

		ring_3_pos = 0
		ring_2_pos += 1

		if ring_2_pos > 25:

			ring_2_pos = 0
			ring_1_pos += 1

			if ring_1_pos > 25:

				ring_1_pos = 0
				rotor1 +=1

				if rotor1 > 4:

					rotor1 = 0
					rotor2 += 1
					
					if rotor2 > 4:

						rotor2 = 0
						rotor3 += 1

						#print(rotor1,rotor2,rotor3,"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

						if rotor3 > 4:

							print(rotors,contador)

							rotor3 = 0
							ringPos_3_pos +=1
							

							if ringPos_3_pos > 25:

								ringPos_3_pos = 0
								ringPos_2_pos += 1

								if ringPos_2_pos > 25:

									ringPos_2_pos = 0
									ringPos_1_pos += 1

									if ringPos_1_pos > 25:

										print("FIN")
										break

						
	#print(ring_3_pos,ring_2_pos,ring_1_pos)

	ring_3 = ring_characters[ring_3_pos]
	ring_2 = ring_characters[ring_2_pos]
	ring_1 = ring_characters[ring_1_pos]

	ringPos_3 = ring_characters[ringPos_3_pos]
	ringPos_2 = ring_characters[ringPos_2_pos]
	ringPos_1 = ring_characters[ringPos_1_pos]

	rotor_test = []

	rotor_test.append(rotores[rotor1])
	rotor_test.append(rotores[rotor2])
	rotor_test.append(rotores[rotor3])


	#print(ring_test)

	ciphertext = encode(plaintext)

	t1 = ciphertext.find(texto_buscado_1)
	t2 = ciphertext.find(texto_buscado_2)
	t3 = ciphertext.find(texto_buscado_3)
	t4 = ciphertext.find(texto_buscado_4)

	if t1 != -1 or t2 != -1 or t3 != -1 or t4 != -1:

		print(ciphertext,'RING SETTINGS:',ringSettings, 'RING POSITION:',ringPositions,'ROTORES:',rotors)

	if t1 != -1:

		print('############',ciphertext,'##########')

	if t1 != -1 and t2 != -1:

		print('***************************',ciphertext,'***********************')
		break

	if ciphertext.startswith("RAFAEL"):

		print(ciphertext)
