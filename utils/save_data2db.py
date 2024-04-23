import pandas as pd
from sqlalchemy import create_engine

# 读取文本文件
data = pd.read_csv('../spiders/5000.txt', sep="\t")

# 创建数据库连接
engine = create_engine('mysql+pymysql://root:Lx284190056@localhost:3306/weiboarticles')

# 将数据写入数据库
data.to_sql('model_data', con=engine, index=False, if_exists='append')

# 关闭数据库连接
engine.dispose()
