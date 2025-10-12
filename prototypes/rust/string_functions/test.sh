BASE_URL=http://localhost:8000

curl $BASE_URL/
echo 
curl "$BASE_URL/reverse?input=hElLo"
echo 
curl "$BASE_URL/upper?input=hElLo"
echo 
curl "$BASE_URL/lower?input=hElLo"