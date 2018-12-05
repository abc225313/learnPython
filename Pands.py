import pandas as pd

name = ["蒙其·D·魯夫", "羅羅亞·索隆", "娜美", "騙人布", "賓什莫克·香吉士", "多尼多尼·喬巴", "妮可·羅賓", "佛朗基", "布魯克"]
occupation = ["船長", "劍士", "航海士", "狙擊手", "廚師", "醫生", "考古學家", "船匠", "音樂家"]

# 建立 dict
straw_hat_dict = {"name": name,
                  "occupation": occupation
}

# 建立第一個 data frame
straw_hat_df = pd.DataFrame(straw_hat_dict)

name = ["蒙其·D·魯夫", "多尼多尼·喬巴", "妮可·羅賓", "布魯克"]
devil_fruit = ["橡膠果實", "人人果實", "花花果實", "黃泉果實"]

# 建立 dict
devil_fruit_dict = {"name": name,
                    "devil_fruit": devil_fruit
}

# 建立第二個 data frame
devil_fruit_df = pd.DataFrame(devil_fruit_dict)

# 連接
straw_hat_merged = pd.merge(straw_hat_df, devil_fruit_df, how = "right")#左右代表取方向為標準
#取共通的陣列名,左右決定採用何者以他的行數為標準
print(straw_hat_merged)
