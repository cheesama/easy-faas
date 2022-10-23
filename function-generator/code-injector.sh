echo $CODE
echo $CODE >> ./main.py

uvicorn main:app --host 0.0.0.0 --port 80

