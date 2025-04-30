
# Env variable is used for the sensitive information like password, tokens , api keys
# To avoid the hard coded in we use the en variables
# to create 
# $env:password = "Sravan@123456789"
# echo $env:password

import os

print(os.getenv("password"))
print(os.getenv("token"))