from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import func

from database import Base

class Member(Base):
    __tablename__ = "member"
    member_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False) ### PK
    email = Column(String(50), nullable=False, unique=True)
    phone_num = Column(String(50), nullable=False)
    nickname = Column(String(50), nullable=False, unique=True)
    
    board = relationship("Board", back_populates="member")
    comment = relationship("Comment", back_populates="member")
    #  password = Column(String, nullable=False)

class Board(Base):
    __tablename__ = "board"
	  
    board_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False) ### PK
    member_id = Column(Integer, ForeignKey("member.member_id"), nullable=False) ### FK
    title = Column(Text, nullable=False)
    content = Column(Text, nullable=False)

    start_price = Column(Integer, nullable=False, default=0)
    create_date = Column(DateTime, server_default=func.now())
    update_date = Column(DateTime, server_default=func.now(), onupdate=func.now())
    delete_date = Column(DateTime)
    due_date = Column(DateTime, nullable=False)

    completed_status_yn = Column(String(1), server_default= 'N')
    image_id = Column(Integer, ForeignKey("imageAlbum.image_id"), nullable=False) ### FK
    image_url = Column(Text)
    area = Column(String(100), nullable=False)

    member = relationship("Member", back_populates="board")
    imageAlbum = relationship("ImageAlbum", back_populates="board")
    comment = relationship("Comment", back_populates="board")

class ImageAlbum(Base):
    __tablename__ = "imageAlbum"
    
    image_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)  # 이미지 ID ### PK
    
    image_url = Column(Text, nullable=False)  # 이미지 URL
    image_name = Column(String(512), nullable=False)  # 이미지 파일명

    board = relationship("Board", back_populates="imageAlbum")

class Comment(Base):
    __tablename__ = "comment"
 
    comment_id = Column(Integer, primary_key=True, autoincrement=True)  # 댓글 ID ### PK
    board_id = Column(Integer, ForeignKey("board.board_id"), nullable=False)  # 게시글 ID ### FK
    member_id = Column(Integer, ForeignKey("member.member_id"), nullable=False)
    content = Column(Text)  # 댓글 내용
    price = Column(Integer, nullable=False, default=0)  # 댓글 가격
    create_date = Column(DateTime, server_default=func.now())  # 댓글 작성 일자
    update_date = Column(DateTime, server_default=func.now(), onupdate=func.now())  # 댓글 수정 일자
    delete_date = Column(DateTime)  # 댓글 삭제 일자
    nickname = Column(String(50))  # 작성자 이름
    accepted_status_yn = Column(String(1), server_default='N')  # 채택 상태 여부 (예: 'Y' 또는 'N')

    board = relationship("Board", back_populates="comment")
    member = relationship("Member", back_populates="comment")