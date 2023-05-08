import requests
url = 'http://localhost:5000/fetch'
r = requests.post(url,json={'max_temp_val_12':54,
                            'heatday_val_10':134,
                            'reservoir_3':168223,
                            "('storm_count', 'Wildfire')":1,
                            'coolday_val_3':0,
                            'heatday_val_6':18,
                            "('storm_count', 'Excessive Heat')":6,
                            'max_temp_val_9':83})
