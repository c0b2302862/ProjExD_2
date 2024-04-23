import os
import sys
import pygame as pg
import random
import time


WIDTH, HEIGHT = 1600, 900
DELTA = {
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, +5),
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT: (+5, 0)
}

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def check_bound(obj_rct:pg.Rect) -> tuple[bool, bool]: #練習3
    """
    こうかとんRect、または、爆弾Rectの画面内外判定用の関数
    引数：こうかとんRect、または、爆弾Rect
    戻り値：横方向判定結果、縦方向判定結果（True：画面/False：画面外）
    """
    yoko, tate = True, True
    if obj_rct.left < 0 or WIDTH < obj_rct.right:
        yoko = False
    if obj_rct.top < 0 or HEIGHT < obj_rct.bottom:
        tate = False
    return yoko, tate

def main():
    #こうかとんの表示
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg")    
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 2.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400
    clock = pg.time.Clock()
    tmr = 0
    #爆弾の表示
    bd_img = pg.Surface((20, 20))
    bd_img.set_colorkey((0, 0, 0))
    pg.draw.circle(bd_img, (255, 0, 0), (10, 10), 10)
    bd_rct = bd_img.get_rect()
    bd_rct.center = random.randint(0, WIDTH), random.randint(0, HEIGHT)
    vx, vy = +5, +5
    accs = [a for a in range(1, 11)] #演習2
    bo_img = pg.Surface((WIDTH, HEIGHT)) #演習3
    pg.draw.rect(bo_img, (0, 0, 0), pg.Rect(0, 0, WIDTH, HEIGHT))
    bo_img.set_alpha(200)
    fonto = pg.font.Font(None, 80)
    txt = fonto.render("Game Over", True, (255, 255, 255))
    kk_img2 = pg.image.load("fig/8.png")
    kk_img3 = pg.image.load("fig/8.png")
    trct = txt.get_rect()
    trct.center = WIDTH/2, HEIGHT/2
    kk_rct2 = kk_img2.get_rect()
    kk_rct2.center = WIDTH/2, HEIGHT/2
    kk_rct3 = kk_img2.get_rect()
    kk_rct3.center = WIDTH/2, HEIGHT/2


    
    


    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            
        if kk_rct.colliderect(bd_rct): #こうかとんと爆弾がぶつかったら　練習4
            
            screen.blit(bo_img, [0, 0])
            screen.blit(txt, trct)
            screen.blit(kk_img2, [WIDTH/2, HEIGHT/2])
            screen.blit(kk_img3, [1000, HEIGHT/2])
            #print("Game Over")
            pg.display.update()
            time.sleep(5)
            return
        

        screen.blit(bg_img, [0, 0]) 

        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        for k, v in DELTA.items(): #練習問題1
            if key_lst[k]:
                sum_mv[0] += v[0]
                sum_mv[1] += v[1]

            
        # if key_lst[pg.K_UP]:
        #     sum_mv[1] -= 5
        # if key_lst[pg.K_DOWN]:
        #     sum_mv[1] += 5
        # if key_lst[pg.K_LEFT]:
        #     sum_mv[0] -= 5
        # if key_lst[pg.K_RIGHT]:
        #     sum_mv[0] += 5
        kk_rct.move_ip(sum_mv)
        if check_bound(kk_rct) != (True, True):
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])
                #sum_mv[0], sum_mv[1] = 0, 0
        screen.blit(kk_img, kk_rct)
        #爆弾に移動と表示
        bd_rct.move_ip(vx, vy)
        screen.blit(bd_img, bd_rct)
        
        yoko, tate = check_bound(bd_rct)
        if not yoko: #横にはみ出たら
            vx *= -1
        if not tate: #縦にはみ出たら
            vy *= -1

        #for r in range(1, 11):
        #    bb_img = pg.Surface((20*r, 20*r))
        #    pg.draw.circle(bb_img, (255, 0, 0), (10*r, 10*r), 10*r)
        
        pg.display.update()
        tmr += 1
        clock.tick(50)
        


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
