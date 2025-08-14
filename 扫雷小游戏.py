import pygame
import random
import sys
from pygame.locals import *

# 初始化pygame
pygame.init()

# 游戏常量
CELL_SIZE = 30
GRID_WIDTH = 16
GRID_HEIGHT = 16
MINES_COUNT = 40
SCREEN_WIDTH = CELL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT + 50  # 额外空间用于显示状态
FPS = 60

# 颜色定义
BACKGROUND = (220, 220, 220)
GRID_LINES = (180, 180, 180)
UNREVEALED = (200, 200, 200)
REVEALED = (230, 230, 230)
MINECOLOR = (255, 0, 0)
FLAGCOLOR = (0, 255, 0)
TEXTCOLOR = (0, 0, 0)
STATUSBAR = (50, 50, 50)
NUM_COLORS = [
    (0, 0, 255),  # 1 - 蓝色
    (0, 128, 0),  # 2 - 绿色
    (255, 0, 0),  # 3 - 红色
    (0, 0, 128),  # 4 - 深蓝
    (128, 0, 0),  # 5 - 深红
    (0, 128, 128),  # 6 - 青色
    (0, 0, 0),  # 7 - 黑色
    (128, 128, 128)  # 8 - 灰色
]

# 设置字体
font = pygame.font.SysFont(None, 24)
large_font = pygame.font.SysFont(None, 36)


class Cell:
    def __init__(self):
        self.is_mine = False
        self.is_revealed = False
        self.is_flagged = False
        self.neighbor_mines = 0


class Minesweeper:
    def __init__(self):
        self.width = GRID_WIDTH
        self.height = GRID_HEIGHT
        self.mine_count = MINES_COUNT
        self.reset_game()

    def reset_game(self):
        self.grid = [[Cell() for _ in range(self.width)] for _ in range(self.height)]
        self.game_over = False
        self.game_won = False
        self.first_click = True
        self.flags_placed = 0
        self.start_time = pygame.time.get_ticks()
        self.elapsed_time = 0

    def place_mines(self, first_x, first_y):
        # 确保第一次点击的位置不是地雷
        safe_cells = [(x, y) for x in range(self.width) for y in range(self.height)]
        safe_cells.remove((first_x, first_y))

        # 随机放置地雷
        mines = random.sample(safe_cells, self.mine_count)
        for x, y in mines:
            self.grid[y][x].is_mine = True

        # 计算每个单元格周围的地雷数量
        for y in range(self.height):
            for x in range(self.width):
                if not self.grid[y][x].is_mine:
                    count = 0
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < self.width and 0 <= ny < self.height:
                                if self.grid[ny][nx].is_mine:
                                    count += 1
                    self.grid[y][x].neighbor_mines = count

        self.first_click = False

    def reveal(self, x, y):
        if not (0 <= x < self.width and 0 <= y < self.height):
            return

        cell = self.grid[y][x]

        if cell.is_revealed or cell.is_flagged or self.game_over or self.game_won:
            return

        if self.first_click:
            self.place_mines(x, y)
            self.start_time = pygame.time.get_ticks()

        cell.is_revealed = True

        if cell.is_mine:
            self.game_over = True
            return

        # 如果周围没有地雷，递归翻开周围的单元格
        if cell.neighbor_mines == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        if not self.grid[ny][nx].is_revealed:
                            self.reveal(nx, ny)

        # 检查是否胜利
        self.check_win()

    def toggle_flag(self, x, y):
        if not (0 <= x < self.width and 0 <= y < self.height):
            return

        cell = self.grid[y][x]
        if not cell.is_revealed and not self.game_over and not self.game_won:
            cell.is_flagged = not cell.is_flagged
            self.flags_placed += 1 if cell.is_flagged else -1

    def check_win(self):
        # 如果所有非地雷单元格都被翻开，则游戏胜利
        for y in range(self.height):
            for x in range(self.width):
                cell = self.grid[y][x]
                if not cell.is_mine and not cell.is_revealed:
                    return
        self.game_won = True
        self.elapsed_time = pygame.time.get_ticks() - self.start_time


def draw_game(screen, game):
    screen.fill(BACKGROUND)

    # 绘制状态栏
    pygame.draw.rect(screen, STATUSBAR, (0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50))

    # 显示地雷和旗帜计数
    mines_text = font.render(f"Mines: {game.mine_count - game.flags_placed}", True, (255, 255, 255))
    screen.blit(mines_text, (20, SCREEN_HEIGHT - 35))

    # 显示时间
    if not game.game_over and not game.game_won:
        game.elapsed_time = pygame.time.get_ticks() - game.start_time
    time_text = font.render(f"Time: {game.elapsed_time // 1000}s", True, (255, 255, 255))
    screen.blit(time_text, (SCREEN_WIDTH - 120, SCREEN_HEIGHT - 35))

    # 显示游戏状态
    if game.game_over:
        status_text = large_font.render("Game Over!", True, (255, 0, 0))
        screen.blit(status_text, (SCREEN_WIDTH // 2 - status_text.get_width() // 2, SCREEN_HEIGHT - 45))
    elif game.game_won:
        status_text = large_font.render("You Win!", True, (0, 255, 0))
        screen.blit(status_text, (SCREEN_WIDTH // 2 - status_text.get_width() // 2, SCREEN_HEIGHT - 45))
    else:
        status_text = font.render("Playing...", True, (200, 200, 200))
        screen.blit(status_text, (SCREEN_WIDTH // 2 - status_text.get_width() // 2, SCREEN_HEIGHT - 35))

    # 绘制网格
    for y in range(game.height):
        for x in range(game.width):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            cell = game.grid[y][x]

            if cell.is_revealed:
                pygame.draw.rect(screen, REVEALED, rect)
                pygame.draw.rect(screen, GRID_LINES, rect, 1)

                if cell.is_mine:
                    # 绘制地雷
                    pygame.draw.circle(screen, MINECOLOR, rect.center, CELL_SIZE // 3)
                    pygame.draw.circle(screen, (0, 0, 0), rect.center, CELL_SIZE // 3, 2)
                elif cell.neighbor_mines > 0:
                    # 绘制数字
                    num_text = font.render(str(cell.neighbor_mines), True, NUM_COLORS[cell.neighbor_mines - 1])
                    screen.blit(num_text, (x * CELL_SIZE + CELL_SIZE // 2 - num_text.get_width() // 2,
                                           y * CELL_SIZE + CELL_SIZE // 2 - num_text.get_height() // 2))
            else:
                # 未翻开的格子
                pygame.draw.rect(screen, UNREVEALED, rect)
                pygame.draw.rect(screen, GRID_LINES, rect, 1)

                if cell.is_flagged:
                    # 绘制旗帜
                    pygame.draw.polygon(screen, FLAGCOLOR, [
                        (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + 5),
                        (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE - 5),
                        (x * CELL_SIZE + CELL_SIZE - 5, y * CELL_SIZE + CELL_SIZE // 2)
                    ])

    # 绘制网格线
    for x in range(0, SCREEN_WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRID_LINES, (x, 0), (x, SCREEN_HEIGHT - 50))
    for y in range(0, SCREEN_HEIGHT - 50, CELL_SIZE):
        pygame.draw.line(screen, GRID_LINES, (0, y), (SCREEN_WIDTH, y))


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("扫雷游戏 (Minesweeper)")
    clock = pygame.time.Clock()

    game = Minesweeper()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos[0] // CELL_SIZE, event.pos[1] // CELL_SIZE

                if event.button == 1:  # 左键翻开
                    game.reveal(x, y)
                elif event.button == 3:  # 右键标记旗帜
                    game.toggle_flag(x, y)

            if event.type == KEYDOWN:
                if event.key == K_r:  # 按R键重置游戏
                    game.reset_game()

        draw_game(screen, game)
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()