from sqlalchemy.sql.expression import distinct
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, render_template


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


@app.route("/")
def api_list():
    """List all available api routes."""

    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/dashboard<br/>"
        f"/api/v1.0/year/&lt;year&gt;<br/>"
        f"/api/v1.0/monthly/&lt;year&gt;/&lt;primary_type&gt;<br>"
        f"/api/v1.0/&lt;year&gt;/&lt;primary_type&gt;"
        f""
    )

@app.route("/model/parameters")
def parameters():
    model = pickle.load('logisticregression.sav')
    parameters = request.get()


if __name__ == '__main__':
    app.run(debug=True)
