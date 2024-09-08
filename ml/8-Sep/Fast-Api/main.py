from fastapi import FastAPI
import joblib
from pydantic import BaseModel
import pandas as pd

final_model = joblib.load("final_model.joblib")

app = FastAPI()

#Perform parsing
class LoanPred(BaseModel):
    Dependents: int 
    Education: int 
    Self_Employed: int 
    TotalIncome: int  # 'income_annum'
    LoanAmount: int 
    Loan_Amount_Term: int  # 'loan_term'
    Credit_History: int  # 'cibil_score'
    Residential_Assets_Value: int 
    Commercial_Assets_Value: int
    Luxury_Assets_Value: int 
    Bank_Asset_Value: int 


@app.get("/")
def read_root():
    return {"Hello": "World, welcome to homepage"}

# You need the details
@app.post("/predict")
def post_demo(loan_details: LoanPred):
    data = loan_details.model_dump()
    new_data = {
        'no_of_dependents': data['Dependents'],
        'education': data['Education'],
        'self_employed': data['Self_Employed'],
        'income_annum': data['TotalIncome'],
        'loan_amount': data['LoanAmount'],
        'loan_term': data['Loan_Amount_Term'],
        'cibil_score': data['Credit_History'],
        'residential_assets_value': data['Residential_Assets_Value'],
        'commercial_assets_value': data['Commercial_Assets_Value'],
        'luxury_assets_value': data['Luxury_Assets_Value'],
        'bank_asset_value': data['Bank_Asset_Value']
	}

    df = pd.DataFrame([new_data])
    prediction = final_model.predict(df)
    if prediction[0] == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'
    return {'Status of Loan Application':pred}