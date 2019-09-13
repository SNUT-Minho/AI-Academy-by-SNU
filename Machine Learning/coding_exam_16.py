import sys

inTrFile = sys.argv[1] # Training data file
inTsFile = sys.argv[2] # Test data file

# Variables
lstTest = []		# Store test data
#			ex) "Sunny Cool High Strong"	=> ["Sunny", "Cool", "High", "Strong"]
dctClassCount = {}	# Store the count of each class
#			ex) { 'Yes': 9, 'No': 5 } 
dctOccur = {}		# Count the occurrence of each pair of feature and class
#		 	ex) "Sunny Cool ... Yes"
#			    "Sunny Mild ... Yes"
#			    "Overcast Cool ... Yes"
#			    "..."
#			     => (Sunny & Yes: 2), (Cool & Yes: 2), (Mild & Yes: 1), (Overcast & Yes: 1) ...
dctLikelihood = {}	# Store the likelihood calculated by dividing the occurrence counts by the class counts
dctPrior = {}		# Calculate and store prior probability using the values of 'dctClassCount'

sInFile = open ( inTrFile, 'r' ) # Open training data file

for sReadLine in sInFile.readlines():	# Read the lines in the file one by one
	sReadLine = sReadLine.replace ( '\n', '' )	# Remove newline character
	lstToken = sReadLine.split( '\t' )		# Split the line by '\t' and store the separated items in a list, lstToken
							# ex) "Sunny	Cool	High	Strong"	=> lstToken = ["Sunny", "Cool", "High", "Strong"]
	for i in range ( len (lstToken[:-1]) ):		# The last element of the list, lstToken[-1], is class label.
							# Visit every feature but the class.
							# ex) 
							# 	0	1	2	3	4(or -1)
							#	Sunny	Cool	High	Strong	Yes	=>	range(0, 4)
		try:
			dctOccur[lstToken[i]][lstToken[-1]] += 1			# 1) Complete this line. 
							# Count the occurrence of each feature-class pair and store in a dictionary, dctOccur.
		except KeyError:
			dctOccur[lstToken[i]] = dctOccur.get ( lstToken[i], {} )
			dctOccur[lstToken[i]][lstToken[-1]] = 1			# 2) Complete this line by initializing 'dctOccur[key1][key2]'

	try:
		dctClassCount[lstToken[-1]] += 1	# 3) Complete this line. Count the number of each class.
	except KeyError:
		dctClassCount[lstToken[-1]] = 1	# 4) Complete this line. Initialize the variable, dctClassCount.

sInFile.close()			# Close training data file

sInFile = open ( inTsFile, 'r' )	# Open test data file

for sReadLine in sInFile.readlines():
	sReadLine = sReadLine.replace ( '\n', '' )
	lstToken = sReadLine.split ( '\t' )
	lstTest.append ( lstToken )

sInFile.close()				# Close test data file

print ( "*** Prior ***" )
for label in dctClassCount.keys():
	dctPrior[label] = dctClassCount[label] / float ( sum ( dctClassCount.values() ) )
	print ( "P(", label, ") = ", dctPrior[label] )
print ( "\n*** Training Results ***" )

for i in dctOccur.keys():
	for j in dctOccur[i].keys():
		try:
			dctLikelihood[i][j] = dctOccur[i][j] / float ( dctClassCount[j] )
		except KeyError:
			dctLikelihood[i] = dctLikelihood.get ( i, {} )
			dctLikelihood[i][j] = dctOccur[i][j] / float ( dctClassCount[j] )

		print ( "P(", i, "|",j, ") = %.2f" % dctLikelihood[i][j],  )

print ( "\n*** Testing ***" )
for i in range ( len(lstTest) ):
	print ( "Test data", i + 1, ":" )  
	for label in dctPrior.keys():
		sOutLine = ""
		tmp = 1
		for j in range ( len(lstTest[i]) ):
			tmp *= dctLikelihood[lstTest[i][j]][label]
			sOutLine += "P(" + lstTest[i][j] + "|" + label + ")"
		tmp *= dctPrior[label]
		sOutLine = "P(" + label + ")" + sOutLine + " ="
		print ( sOutLine, "%.5f" % tmp )
