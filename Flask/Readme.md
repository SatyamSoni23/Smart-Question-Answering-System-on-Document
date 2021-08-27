## Flask Deployment
1. Install the Python 3.6 (If you are using heroku run runtime.txt file)
2. Install packages using requirements.txt file 
3. Run app.py file
4. Open your browser write your IP Address and add :500 at last. (example- http://192.168.114.84:5000/)


If you are facing any problem running project on local host 
In app.py replace app.run(host="0.0.0.0", port=8080) with app.run(debug=True)  (If you are deploying project on aws don't replace this line)
