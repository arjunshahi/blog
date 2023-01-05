from app.db.base_class import Base
from sqlalchemy import Boolean, Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
from datetime import datetime

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    joined_on = Column(TIMESTAMP, default=datetime.now)

    # relationships
    blogs = relationship("Blog", back_populates="posted_by")
    comments = relationship("BlogComment", back_populates="blog")
