import pandas as pd
 
data = {
    "polish": ["styczen","luty","marzec","kwiecien","maj","czerwiec",
                "lipiec","sierpien","wrzesien","pazdziernik","listopad","grudzien"],
    "days" :  [31,28,31,30,31,30,31,31,30,31,30,31]
}
 
dataFrame = pd.DataFrame(data)
 
print(dataFrame)
