import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'fixedacidity':2.0000,'volatileacidity':9.0000,'citricacid':6.0000,'trestbps':2.00000,'residualsugar':9.00000,'chlorides':6.00000,
                            'freesulfurdioxide':9.00000,'totalsulfurdioxide':6.00000,'density':20000,'pH':900000,
                            'sulphates':60000,'alcohol':60000})

print(r.json()) ## we can give single value also  'age':2.0000, // 'age':2,
