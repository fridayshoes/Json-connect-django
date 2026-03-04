## Json Connect Project using Django

Activity :

Create New Django
Project AS JsonConnect

REST API Creation
3 app Services to be created and used!
REST creation atleat one will be fetching data from External file as JsON .

Create fresh Project

Backend

Front End By Angualr

### Service 1

#### Task 1

Displays data from data.json at http://127.0.0.1:8000/service1/ - GET METHOD

#### Task 2

Displays data from data.json at http://127.0.0.1:8000/service1/filter-age/ - only POST method

Go to POSTMAN app,

Put in URL, select POST, select Body (raw, JSON) and input below

```
{
"age": 34
}
```

Press, Send.

Should see JSON data for 34 or above only

#### Task 3

Displays only records with bonus 3000 or above http://127.0.0.1:8000/service1/filter-bonus/ - only GET method allowed

#### Task 4

Displays only records with bonus 3000 and above and age 34 127.0.0.1:8000/service1/filter-bonus-age/ - only GET method allowed

#### Task 5

Displays data from records.json and updates bonus when given an age http://127.0.0.1:8000/service1/filter-age-update-bonus/ - only POST method

Go to POSTMAN app,

Put in URL, select POST, select Body (raw, JSON) and input below

```
{
"age": 29
}
```

Press, Send.

Should see JSON data for people with age 29 or above, bonuses will be updated by 10,000
