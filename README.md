# stormtech
Test Developer Back-end Python


----------------- Linux deploy execution ----------------------------

apt-get update<br>
apt-get install python python-pip virtualenv curl<br>
virtualenv stormtech_env<br>
source activate stormtech_env/bin/activate<br>
pip install flask flask-restful<br>
python teste.py<br>

--------------------------------------------------------------------

-----------------Client Request --------------------------------------------

curl http://127.0.0.1:5000/ -X POST -d '{"title":"asc"}'  -H "Content-Type: application/json" 

curl http://127.0.0.1:5000/ -X POST -d '{"title":"desc", "author":"asc"}'  -H "Content-Type: application/json" 

curl http://127.0.0.1:5000/ -X POST -d '{"title":"asc", "author":"desc", "edition": "desc"}'  -H "Content-Type: application/json" 

curl http://127.0.0.1:5000/ -X POST -d '{}'  -H "Content-Type: application/json" 

curl http://127.0.0.1:5000/ -X POST  -H "Content-Type: application/json" 
