# stormtech
Test Developer Back-end Python


----------------- Linux deploy execution ----------------------------

apt-get update
apt-get install python python-pip virtualenv curl
virtualenv stormtech_env
source activate stormtech_env/bin/activate
pip install flask flask-restful
python teste.py

--------------------------------------------------------------------

-----------------Client Request --------------------------------------------

curl http://127.0.0.1:5000/ -X POST -d '{"title":"asc"}'  -H "Content-Type: application/json" 

curl http://127.0.0.1:5000/ -X POST -d '{"title":"desc", "author":"asc"}'  -H "Content-Type: application/json" 

curl http://127.0.0.1:5000/ -X POST -d '{"title":"asc", "author":"desc", "edition": "desc"}'  -H "Content-Type: application/json" 

curl http://127.0.0.1:5000/ -X POST -d '{}'  -H "Content-Type: application/json" 

curl http://127.0.0.1:5000/ -X POST  -H "Content-Type: application/json" 
