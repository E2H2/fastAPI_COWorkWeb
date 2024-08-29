# router
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db

from domain.comment import comment_schema, comment_crud

router = APIRouter(
    prefix="/api/detail/{post_id}"
)

@router.post("/comment")
def create_comment(detail_id: int, member_id: int, _create_comment: comment_schema.Create, db: Session = Depends(get_db)):
    result = comment_crud.create_comment(detail_id = detail_id, member_id = member_id, db = db, _create_comment = _create_comment)
    return {"댓글이 성공적으로 생성되었습니다."}

@router.patch("/comment/{comment_id}")
def update_comment(comment_id: int, _update_comment: comment_schema.Update, db: Session = Depends(get_db)):
    updated_comment = comment_crud.update_comment(comment_id=comment_id, db=db, _update_comment=_update_comment)
    return {"message": "댓글이 성공적으로 수정되었습니다.", "comment": updated_comment}

@router.delete("/comment/{comment_id}")
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    result = comment_crud.delete_comment(comment_id=comment_id, db=db)
    return result

@router.get("/comments")
def get_comments(db: Session = Depends(get_db)):
    comments = comment_crud.get_comments(db=db)
    return comments

# @router.get("/comment")
# def get_comment(db: Session = Depends(get_db)):
#     result = comment_crud.get_comment(db, comment_id = comment_id)


@router.patch("/comment/{comment_id}/accept")
def accept_comment(comment_id: int, db: Session = Depends(get_db)):
    # 댓글을 채택 상태로 업데이트합니다.
    
    accepted_comment = comment_crud.accept_comment(comment_id=comment_id, db=db)
    return {"message": "댓글이 채택되었습니다.", "comment": accepted_comment}
