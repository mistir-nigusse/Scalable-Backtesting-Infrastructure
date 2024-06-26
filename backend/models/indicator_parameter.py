from sqlalchemy import Column, Integer,  ForeignKey, Float,String
from sqlalchemy.orm import relationship
from ..utils.database_connection import Base

class IndicatorParameter(Base):
    __tablename__ = "indicator_parameters"
    id = Column(Integer, primary_key=True, index=True)
    indicator_id = Column(Integer, ForeignKey("indicators.indicator_id"))
    parameter_name = Column(String, index=True)
    parameter_value = Column(Float)
    # scene = relationship("Indicator", back_populates="indicators")
    indicators = relationship("Indicator", back_populates="parameters")
    # backtest_results = relationship("BacktestResult", back_populates="indicator_parameters")

    