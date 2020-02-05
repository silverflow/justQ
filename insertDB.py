from sqlalchemy import Column, String, Integer, Float, Date
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.ext.declarative import declarative_base
import pymysql
import pandas as pd
from sqlalchemy import create_engine


engine = create_engine(
    "mysql+pymysql://root:8884@ec2-13-125-246-153.ap-northeast-2.compute.amazonaws.com:3306/my_database", encoding='utf-8-sig')


Base = declarative_base()


class salesOrdersRaw(Base):
    __tablename__ = 'salesOrders'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    OrderDate = Column(Date())
    Region = Column(String(20))
    Rep = Column(String(20))
    Item = Column(String(10))
    Units = Column(Integer())
    UnitCost = Column(Float())
    Total = Column(Float())


metadata = Base.metadata
metadata.create_all(engine)

df = pd.read_excel('SampleData.xlsx', sheet_name='SalesOrders', header=0)
df.to_sql(name='sales_order', con=engine, if_exists='append', index=False)
