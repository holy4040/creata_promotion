# creata_promotion
Creata interview project
1. make build will run the backend (admin portal, email management, API) and initial data (create superuser if .env set up) with 5 promotion codes in postgres DB. All available commands are in Makefile.
2. admin portal: http://127.0.0.1:8080/creata_portal/
login info is in .env
email management portal: http://localhost:5557/
For future purpose if needs to register customers when they sumit the promotion code. This could be used to manage email sending.
3. creata_promo.postman_collection.json has basic API test.
For admin, required to login and get the auth code for the other API call.
The code should be placed to Authorization Bearer Token.
a. user login
b. create promotion code (if required)
c. all participants: return all participants detail with promotion code and is winner flag
d. select winner: choose one of the promotion code as the winner. Only all promotion code has been redeemed could proceed.

For frontend client site, submit promotion code is set in frontend API call.
