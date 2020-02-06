from sqlalchemy import Column, String, Integer, Float, Date
from sqlalchemy.ext.declarative import declarative_base
import pymysql
import pandas as pd
from sqlalchemy import create_engine


# 제 개인 연습용 AWS 입니다. 테스트 환경에 맞게 밑에 설정을 바꿔주세요
# 아이디:비밀번호@호스트명:포트/DB명
engine = create_engine(
    "mysql+pymysql://root:8884@ec2-13-125-246-153.ap-northeast-2.compute.amazonaws.com:3306/my_database", encoding='utf-8-sig')

Base = declarative_base()

# ORM Class


class salesOrdersRaw(Base):
    __tablename__ = 'sales_order'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    OrderDate = Column(Date())
    Region = Column(String(20))
    Rep = Column(String(20))
    Item = Column(String(10))
    Units = Column(Integer())
    UnitCost = Column('Unit Cost', Float())
    Total = Column(Float())


# DB에 메타데이터 생성
metadata = Base.metadata
metadata.create_all(engine)

# DB에 데이터 넣기
df = pd.read_excel('SampleData.xlsx', sheet_name='SalesOrders', header=0)
df.to_sql(name='sales_order', con=engine, if_exists='append', index=False)
