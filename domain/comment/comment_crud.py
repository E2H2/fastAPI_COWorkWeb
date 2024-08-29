# crud
from models import Board, Member, Comment
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from domain.comment.comment_schema import Create, Update
from fastapi import HTTPException
from datetime import datetime

def get_nickname(member_id: int, db: Session) -> str:
    """ 회원 ID로 nickname을 조회합니다. """
    try:
        member = db.query(Member).filter(Member.member_id == member_id).one()
        return member.nickname
    except NoResultFound:
        raise ValueError("Member not found")

def create_comment(detail_id: int, member_id: int, db: Session, _create_comment: Create):
    nickname = get_nickname(member_id, db)

    db_create = Comment(board_id = detail_id,
                        member_id = member_id,
                        content = _create_comment.content,
                        price = _create_comment.price,
                        create_date = datetime.now(),
                        accepted_status_yn = "N" ,
                        nickname=nickname
                        )
    db.add(db_create)
    db.commit()


def update_comment(comment_id: int, db: Session, _update_comment: Update):
    db_comment = db.query(Comment).filter(Comment.comment_id == comment_id).first()  # 필드 이름 수정

    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")

    if _update_comment.content is not None:
        db_comment.content = _update_comment.content

    if _update_comment.price is not None:
        db_comment.price = _update_comment.price

    db_comment.update_date = datetime.now()  # `create_date` 대신 `update_date`로 수정

    db.commit()
    db.refresh(db_comment)
    return db_comment

def delete_comment(comment_id: int, db: Session):
    db_comment = db.query(Comment).filter(Comment.comment_id == comment_id).first()  # 필드 이름 수정

    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")

    # 댓글의 삭제 날짜를 현재 시간으로 설정하여 논리적으로 삭제
    db_comment.delete_date = datetime.now()
    db.commit()
    db.refresh(db_comment)
    return {"message": "댓글이 성공적으로 삭제되었습니다.", "comment": db_comment}

def get_comments(db: Session):
    # 삭제되지 않은 댓글들만 가져오기
    comments = db.query(Comment).filter(Comment.delete_date.is_(None)).all()
    return comments

def accept_comment(comment_id: int, db: Session):
    # 댓글을 채택 상태로 업데이트합니다.
    db_comment = db.query(Comment).filter(Comment.comment_id == comment_id).first()

    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")

    # 댓글의 채택 상태를 'Y'로 업데이트
    db_comment.accepted_status_yn = 'Y'
    db_comment.update_date = datetime.now()  # 업데이트 날짜 갱신

    db.commit()
    db.refresh(db_comment)
    return db_comment
