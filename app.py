#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, render_template
import joblib


# In[2]:


app = Flask(__name__)


# In[3]:


@app.route("/", methods=["GET", "POST"])
def index():
    models = ['svm_linear', 'svm_poly', 'svm_rbf', 'svm_sigmoid', 'ada_boost', 'gradient_boost', 'log_regression']
    model_accuracy = {'svm_linear': 0.8105119918353462,
                     'svm_poly': 0.6878720870896411,
                     'svm_rbf': 0.8457220615750978,
                     'svm_sigmoid': 0.7121959516924647,
                     'ada_boost': 0.790100357203606,
                     'gradient_boost': 0.8113624766116686,
                     'log_regression': 0.8021772410273856}
    
    if request.method == "POST": 
        model = request.form.get("model")
        model_selected = joblib.load(model)
        str1 = f"The accuracy of {model} to predict bankruptcy is : {model_accuracy[model]*100:.2f}%"
        return(render_template("index.html", result1=str1, models = models))
    else:
        return(render_template("index.html", result1="Your result will be shown here", models = models))


if __name__ == "__main__": 
    app.run()


# In[ ]:




