from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP

from database import Base


class Tweet(Base):
    __tablename__ = 'tweets'
    id = Column(Integer, primary_key=True)
    text = Column(String(500))
    positive = Column(Boolean)
    negative = Column(Boolean)
    created_at = Column(TIMESTAMP)

    def __init__(self, text=None, positive=None, negative=None, created_at=None):
        self.text = text
        self.positive = positive
        self.negative = negative
        self.created_at = created_at

    def __repr__(self):
        return '<Tweet %r>' % (self.text)
