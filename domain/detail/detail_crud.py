# crud
from models import Board, Member
from sqlalchemy.orm import Session
from domain.detail.detail_schema import Create, Update, Detail

from datetime import datetime

def get_board_detail(db: Session, detail_id: int):
    query = db.query(Board, Member.nickname).join(Member).filter(Board.board_id == detail_id).one_or_none()

    return query

def create_board(db: Session, _create_board: Create):
    db_create = Board(member_id = _create_board.member_id,
                      title = _create_board.title,
                      content = _create_board.content,
                      start_price = _create_board.start_price,
                      completed_status_yn = _create_board.completed_status_yn,
                      image_id = _create_board.image_id,
                      image_url = _create_board.image_url,
                      area = _create_board.area,
                      # due_time은 프론트에서 어떻게 넘겨줘요???
                      due_date = datetime.now()
                      )
    db.add(db_create)
    db.commit()

def update_board(db: Session, target_db: Board, _update_board: Update):
    target_db.content = _update_board.content
    target_db.image_url = _update_board.image_url

    db.add(target_db)
    db.commit()

def delete_board(db: Session, target_db: Board, _board_delete: Detail):
    target_db.delete_date = datetime.now()
    
    db.add(target_db)
    db.commit()