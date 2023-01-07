from datetime import datetime

from sqlalchemy import (TIMESTAMP, Boolean, Column, ForeignKey, Integer,
                        String, Text)
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Blog(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    is_published = Column(Boolean, default=True)
    posted_on = Column(TIMESTAMP, default=datetime.now)

    # fks
    posted_by_id = Column(Integer, ForeignKey("user.id"), index=True)
    
    # relationships
    posted_by = relationship("User", back_populates="blogs")
    comments = relationship("BlogComment", back_populates="blog")


class BlogComment(Base):
    id = Column(Integer, primary_key=True, index=True)
    comment = Column(String(255), nullable=False)
    
    # fks
    blog_id = Column(Integer, ForeignKey("blog.id"), index=True)
    user_id = Column(Integer, ForeignKey("user.id"), index=True)

    # relationships
    blog = relationship("Blog", back_populates="comments")
    user = relationship("User", back_populates="comments")
    


