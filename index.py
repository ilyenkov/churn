# -*- coding: utf-8 -*-
__author__ = 'xead'
from churn_model import model
from codecs import open
#import time
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

#print "Preparing model"
#start_time = time.time()
ec_model = model()
#print "Model is ready"
#print time.time() - start_time, "seconds"

@app.route("/churn-model", methods=["POST", "GET"])
def index_page(weight=0, arpu=100, retention_cost=20, retention_prob=0.2, retention_scale=0.01, retention_life_exp=12, fix_costs=10000, result=""):
    a="hello.html"
    if request.method == "POST":
        weight = request.form["weight"]
        arpu = request.form["arpu"]
        retention_cost = request.form["retention_cost"]
        retention_prob = request.form["retention_prob"]
        retention_scale = request.form["retention_scale"]
        retention_life_exp = request.form["retention_life_exp"]
        fix_costs = request.form["fix_costs"]
        result = ec_model.effect(weight, arpu, retention_cost, retention_prob, retention_scale, retention_life_exp, fix_costs)       
        
    return render_template(a, weight=weight, arpu=arpu, retention_cost=retention_cost, retention_prob=retention_prob, retention_scale=retention_scale, retention_life_exp=retention_life_exp, fix_costs=fix_costs, result=result)
	#return redirect(url_for('index_page', _anchor="mod"))    
    #else:
	#return render_template(a, weight=weight, arpu=arpu, retention_cost=retention_cost, retention_prob=retention_prob, retention_scale=retention_scale, retention_life_exp=retention_life_exp, fix_costs=fix_costs, result=result)
def index_page_mod():
    return redirect(url_for('index_page', _anchor="mod"))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=False)
