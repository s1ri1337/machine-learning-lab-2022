from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
import pandas as pd
import json

app = FastAPI()

@app.get("/recommend")
def getRecs(userNo):
    recs = pd.read_csv("recs.csv")
    return JSONResponse(recs.loc[recs['userId'] == userNo]["title"].reset_index(drop = True).to_dict())
