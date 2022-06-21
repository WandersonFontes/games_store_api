from typing import List
from ninja.router import Router
from ninja.orm import create_schema
from .models import Games
from django.shortcuts import get_object_or_404

router_api = Router()
GameSchema = create_schema(Games)

@router_api.post("/game/create",)
def create_games(request, payload: GameSchema):
    "Create new game"
    try:
       data = Games.objects.get(id=payload.id)
    except Games.DoesNotExist:
        data = Games.objects.create(
            name=payload.name, 
            price=payload.price, 
            page=payload.page,
            picture=payload.picture, 
        )
    data.save()
    return {"success": True}

@router_api.get("/games/all", response=List[GameSchema])
def list_games(request):
    'List all games'
    datas = Games.objects.all()
    return datas

# @router_api.get("/game/{id}", response=GameSchema)
# def get_game(request, id: int):
#     game = get_object_or_404(Games, id=id)
#     return game

# @router_api.put("/game/{id}")
# def update_game(request, id: str, payload: GameSchema):
#     game = get_object_or_404(Games, id=id)
#     for attr, value in payload.dict().items():
#         setattr(game, attr, value)
#     game.save()
#     return {"success": True}

# @router_api.delete("/game/{id}")
# def delete_game(request, id: int):
#     game = get_object_or_404(Games, id=id)
#     game.delete()
#     return {"success": True}