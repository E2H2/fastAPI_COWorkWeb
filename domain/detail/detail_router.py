# router
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db

from domain.detail import detail_schema, detail_crud

router = APIRouter(
    prefix="/api/detail"
)

@router.get("/{detail_id}", response_model=detail_schema.Detail)
def board_detail(detail_id: int, db: Session = Depends(get_db)):
    result = detail_crud.get_board_detail(db, detail_id=detail_id)

    # tuple형태의 query result를 JSON 형태로 전환
    if result:
        _board, nickname = result
    # response_model에 값을 맞추기
        response = {
            "title" : _board.title,
            "nickname" : nickname,
            "create_date" : _board.create_date,
            "area" : _board.area,
            "content" : _board.content,
            "image_url" : _board.image_url
        }
        return response
    
    else: 
        raise HTTPException(status_code=404, detail="존재하지 않는 게시글")

@router.post("/create")
def board_create(_board_create: detail_schema.Create, db: Session = Depends(get_db)):
    #do nothing
    detail_crud.create_board(db = db, _create_board = _board_create)
    return {"우와 잘 등록이 되었어요~~"}

@router.patch("/update")
def board_update(detail_id : int, _board_update: detail_schema.Update, db: Session = Depends(get_db)):
    query = detail_crud.get_board_detail(db = db, detail_id = detail_id)
    # query는 tuple형으로, ([query결과], [nickname]) 의 형태를 가진다.
    target_db = query[0]
    detail_crud.update_board(db = db, target_db = target_db, _update_board = _board_update)
    return {"와 업데이트에 성공했어요~~"}

### delete query 는 우선, delete_date를 추가하는 api로 작성했습니다~~~ / 08.28
@router.delete("/delete")
def board_delete(detail_id: int, _board_delete: detail_schema.Detail, db: Session = Depends(get_db)):
    query = detail_crud.get_board_detail(db = db, detail_id=detail_id)
    target_db = query[0]
    detail_crud.delte_board(db = db, target_db = target_db, _board_delete = _board_delete)
    return {"와 삭제에 성공했어요~~"}