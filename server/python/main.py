# 게임 로직을 담는 코드

import random

player_count = int(input('플레이 할 인원을 입력하시오 > '))  # 플레이어의 수

tile = [
    '0b','1b','2b','3b','4b','5b','6b','7b','8b','9b','10b','11b','jb',
    '0w','1w','2w','3w','4w','5w','6w','7w','8w','9w','10w','11w','jw'
]

# 손 패를 담을 리스트
players = [[] for _ in range(player_count)]
# 공개된 인덱스를 담을 리스트
hide_index_list = [[] for _ in range(player_count)]

# 타일 정렬 기준
def sort_tile(tile):
    if tile == 'jb':
        return (0, 0)
    if tile == 'jw':
        return (0, 1)
    num = int(tile[:-1])
    color = tile[-1]
    color_priority = 0 if color == 'b' else 1
    return (num, color_priority)

# 패 나눠주는 함수
def start_tile(players):
    for _ in range(4): 
        for player in players:
            draw_tile = random.choice(tile)
            player.append(draw_tile)
            tile.remove(draw_tile)
            player.sort(key=sort_tile)

# 드로우 함수
def draw_turn(player):
    if len(tile) > 0:
        draw_tile = random.choice(tile)
        player.append(draw_tile)
        tile.remove(draw_tile)
        player.sort(key=sort_tile)
        return draw_tile
    else:
        return None

# 손패 보여주는 함수
def display_tiles(hand, hide_index):
    display = []
    for i, tile in enumerate(hand):
        if i in hide_index:
            display.append(tile)
        else:
            display.append('*')
    return display

# 타일 추측 함수
def guess_tile(players, guess_player_index):
    target_index = int(input('어느 플레이어를 선택하시겠습니까? > '))
    print(f'{guess_player_index}번 플레이어가 {target_index}번 플레이어를 선택하였습니다.')

    print(f'{target_index}번 플레이어의 현재 패: {display_tiles(players[target_index], hide_index_list[target_index])}')
    
    target_tile_index = int(input(f'{target_index}번 플레이어의 몇 번째 손패를 선택하시겠습니까? (0부터 시작) > '))
    target_tile = input(f'{target_tile_index}번째 타일은 어떤 타일 입니까? > ')

    if target_tile == players[target_index][target_tile_index]:
        print('맞췄습니다!')
        # 공개된 인덱스로 저장
        hide_index_list[target_index].append(target_tile_index)
    else:
        print('틀렸습니다!')



start_tile(players)
draw_turn = draw_turn(players[0])
guess_tile(players, 0)