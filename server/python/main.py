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
    # 추후 수정정
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
def guess_tile(players, guess_player_index, draw_tile=None):
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
        if draw_tile:
            # 드로우한 타일이 플레이어 손패의 몇 번째에 들어갔는지 찾음
            tile_index = players[guess_player_index].index(draw_tile)
            hide_index_list[guess_player_index].append(tile_index)
            
def player_turn(players, player_index):
    print(f"\n=== {player_index}번 플레이어의 턴입니다 ===")
    drawn_tile = draw_turn(players[player_index])

    # 현재 전체 손패 상황 출력
    for i, hand in enumerate(players):
        print(f'{i}번 손패: {display_tiles(hand, hide_index_list[i])}')

    guessed_correctly = guess_tile(players, player_index, drawn_tile)

    if guessed_correctly:
        while True:
            choice = input("1. 한번 더 추리하기\n2. 턴 넘기기\n선택하세요 (1 또는 2): ")
            if choice == "1":
                print(f"{player_index}번 플레이어가 다시 추리를 시도합니다!")
                return player_index  # 턴 유지
            elif choice == "2":
                print("턴을 넘깁니다.")
                return (player_index + 1) % player_count  # 다음 플레이어로
            else:
                print("잘못된 입력입니다. 다시 선택해주세요.")
    else:
        print("틀렸습니다. 턴이 다음 플레이어에게 넘어갑니다.")
        return (player_index + 1) % player_count  # 틀리면 자동 턴 넘김

start_tile(players)

while True:
    current_player = player_turn(players, current_player)
    
# for i, hand in enumerate(players):
#     print(f'{i}, {hand}')
