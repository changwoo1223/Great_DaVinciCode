import random

player_count = int(input('플레이 할 인원을 입력하시오 > '))  # 플레이어 수 입력

tile = [
    '0b','1b','2b','3b','4b','5b','6b','7b','8b','9b','10b','11b','jb',
    '0w','1w','2w','3w','4w','5w','6w','7w','8w','9w','10w','11w','jw'
]

# 플레이어 손패 리스트
players = [[] for _ in range(player_count)]
# 공개된 인덱스 리스트
hide_index_list = [[] for _ in range(player_count)]

# 정렬 기준 함수
def sort_tile(tile):
    if tile in ['jb', 'jw']:  # 조커는 정렬 제외 (맨 뒤로)
        return (99, 2)
    num = int(tile[:-1])
    color = tile[-1]
    color_priority = 0 if color == 'b' else 1
    return (num, color_priority)

# 초기 패 나눠주는 함수
def start_tile(players):
    for i, player in enumerate(players):
        temp_hand = []
        while len(temp_hand) < 4:
            draw = random.choice(tile)
            tile.remove(draw)
            if draw in ['jb', 'jw']:
                pos = int(input(f"{i}번 플레이어: 조커({draw})를 어디에 배치하시겠습니까? (0~{len(temp_hand)} 위치 중 선택) > "))
                temp_hand.insert(pos, draw)
            else:
                temp_hand.append(draw)
        player.extend(temp_hand)

# 드로우 함수
def draw_turn(player):
    if len(tile) > 0:
        draw_tile = random.choice(tile)
        tile.remove(draw_tile)
        print(f"드로우된 타일: {draw_tile}")
        if draw_tile in ['jb', 'jw']:
            pos = int(input(f"조커({draw_tile})를 어디에 배치하시겠습니까? (0~{len(player)} 위치 중 선택) > "))
            player.insert(pos, draw_tile)
        else:
            player.append(draw_tile)
            player.sort(key=sort_tile)
        return draw_tile
    else:
        return None

# 손패 출력 함수 (숨겨진 타일 *)
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
        hide_index_list[target_index].append(target_tile_index)
        return True
    else:
        print('틀렸습니다!')
        if draw_tile:
            tile_index = players[guess_player_index].index(draw_tile)
            hide_index_list[guess_player_index].append(tile_index)
        return False

# 플레이어 턴 함수
def player_turn(players, player_index):
    print(f"\n=== {player_index}번 플레이어의 턴입니다 ===")
    drawn_tile = draw_turn(players[player_index])

    # 전체 손패 출력
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
                return (player_index + 1) % player_count
            else:
                print("잘못된 입력입니다. 다시 선택해주세요.")
    else:
        print("틀렸습니다. 턴이 다음 플레이어에게 넘어갑니다.")
        return (player_index + 1) % player_count

# 게임 시작
start_tile(players)
current_player = 0

while True:
    current_player = player_turn(players, current_player)
