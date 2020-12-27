import pygame
import sys
import copy

pygame.init()

#necessary variables
w = 602
h = 602
h_max = 650

val = (w - 2)/3

x_score = 0
o_score = 0

a = 0
which_move = 'x'
which_round = 'x'
victory = False

white = (255,255,255)
black = (0,0,0)
red = (170,0,0)
blue = (0,0,170)

field_base = [
	[ 
		[  [0,val],[0,val]  ], [  [val+1,val*2],[0,val]  ], [  [(val*2)+1,(val*3)],[0,val]  ]
	],

	[ 
		[  [0,val],[val+1,val*2]  ], [  [val+1,val*2],[val+1,val*2]  ], [  [(val*2)+1,(val*3)],[val+1,val*2]  ]
	],

	[ 
		[  [0,val],[(val*2)+1,(val*3)]  ], [  [val+1,val*2],[(val*2)+1,(val*3)] ], [  [(val*2)+1,(val*3)],[(val*2)+1,(val*3)] ] 
	],
]

win = pygame.display.set_mode((w,h_max))
sur = pygame.Surface((w,h_max - h))


#functions
def update_screen():
	global a
	a = 0
	win.fill(white)

	win.blit(sur,(0,h))
	sur.fill(black)

	pygame.draw.line(win,black,[val+1,0],[val+1,h],1)
	pygame.draw.line(win,black,[(val*2)+1,0],[(val*2)+1,h],1)

	pygame.draw.line(win,black,[0,val+1],[h,val+1],1)
	pygame.draw.line(win,black,[0,(val*2)+1],[h,(val*2)+1],1)

	return copy.deepcopy(field_base)


def view_score():
	win.blit(sur,(0,h))
	sur.fill(black)
	text_score = pygame.font.SysFont('arial',30)
	text_score = text_score.render(f'{o_score} - O | X - {x_score}',1,white)

	win.blit(text_score,((w - text_score.get_rect()[2])/2,h + ((h_max - h) - text_score.get_rect()[3])/2))


field = update_screen()
view_score() 


while True:
	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			sys.exit()

		if victory == True:
			text_info = pygame.font.SysFont('lato',18)
			text_info = text_info.render('Click right mouse button',0,white)
			win.blit(text_info,(10,h_max - 10 - text_info.get_rect()[3]))

			if i.type == pygame.MOUSEBUTTONDOWN:
				if i.button == 3:
					if which_round == 'x':
						which_round,which_move = 'o','o'
					else:
						which_round,which_move = 'x','x'

					victory = False
					field = update_screen()

	if victory == False:
		keys = pygame.mouse.get_pressed()
		pos = pygame.mouse.get_pos()

		for j in field:
			for k in range(len(j)):
				if keys[0] and j[k] != 'x' and j[k] != 'o':
					if j[k][0][0] <= pos[0] <= j[k][0][1] and j[k][1][0] <= pos[1] <= j[k][1][1]:
						if which_move == 'x':
							pygame.draw.line(win,blue,[j[k][0][0] + 55,j[k][1][0] + 35 ],[j[k][0][1] - 55,j[k][1][1] - 35],8)
							pygame.draw.line(win,blue,[j[k][0][1] - 55,j[k][1][0] + 35 ],[j[k][0][0] + 55,j[k][1][1] - 35],8)
							j[k] = 'x'
							a += 1
							which_move = 'o'
						else:
							pygame.draw.circle(win,red,[   (j[k][0][0] + j[k][0][1])/2,(j[k][1][0] + j[k][1][1])/2  ],70,8)
							j[k] = 'o'
							a += 1
							which_move = 'x'
		#1-9
		if field[0][0] == 'x' and field[1][1] == 'x' and field[2][2] == 'x':
			x_score += 1
			pygame.draw.line(win,black,[0+20,0+20],[w-20,h-20],20)
			victory = True
		elif field[0][0] == 'o' and field[1][1] == 'o' and field[2][2] == 'o':
			o_score += 1
			pygame.draw.line(win,black,[0+20,0+20],[w-20,h-20],20)
			victory = True

		#3-7
		if field[0][2] == 'x' and field[1][1] == 'x' and field[2][0] == 'x':
			x_score += 1
			pygame.draw.line(win,black,[w-20,0+20],[0+20,h-20],20)
			victory = True
		elif field[0][2] == 'o' and field[1][1] == 'o' and field[2][0] == 'o':
			o_score += 1
			pygame.draw.line(win,black,[w-20,0+20],[0+20,h-20],20)
			victory = True

		#1-3
		if field[0][0] == 'x' and field[0][1] == 'x' and field[0][2] == 'x':
			x_score += 1
			pygame.draw.line(win,black,[0+20,val*0.5],[w-20,val*0.5],20)
			victory = True
		elif field[0][0] == 'o' and field[0][1] == 'o' and field[0][2] == 'o':
			o_score += 1
			pygame.draw.line(win,black,[0+20,val*0.5],[w-20,val*0.5],20)
			victory = True

		#4-6
		if field[1][0] == 'x' and field[1][1] == 'x' and field[1][2] == 'x':
			x_score += 1
			pygame.draw.line(win,black,[0+20,val*1.5],[w-20,val*1.5],20)
			victory = True
		elif field[1][0] == 'o' and field[1][1] == 'o' and field[1][2] == 'o':
			o_score += 1
			pygame.draw.line(win,black,[0+20,val*1.5],[w-20,val*1.5],20)
			victory = True

		#7-9
		if field[2][0] == 'x' and field[2][1] == 'x' and field[2][2] == 'x':
			x_score += 1
			pygame.draw.line(win,black,[0+20,val*2.5],[w-20,val*2.5],20)
			victory = True
		elif field[2][0] == 'o' and field[2][1] == 'o' and field[2][2] == 'o':
			o_score += 1
			pygame.draw.line(win,black,[0+20,val*2.5],[w-20,val*2.5],20)
			victory = True

		#1-7
		if field[0][0] == 'x' and field[1][0] == 'x' and field[2][0] == 'x':
			x_score += 1
			pygame.draw.line(win,black,[val*0.5,0+20],[val*0.5,h-20],20)
			victory = True
		elif field[0][0] == 'o' and field[1][0] == 'o' and field[2][0] == 'o':
			o_score += 1
			pygame.draw.line(win,black,[val*0.5,0+20],[val*0.5,h-20],20)
			victory = True

		#2-8
		if field[0][1] == 'x' and field[1][1] == 'x' and field[2][1] == 'x':
			x_score += 1
			pygame.draw.line(win,black,[val*1.5,0+20],[val*1.5,h-20],20)
			victory = True
		elif field[0][1] == 'o' and field[1][1] == 'o' and field[2][1] == 'o':
			o_score += 1
			pygame.draw.line(win,black,[val*1.5,0+20],[val*1.5,h-20],20)
			victory = True

		#3-9
		if field[0][2] == 'x' and field[1][2] == 'x' and field[2][2] == 'x':
			x_score += 1
			pygame.draw.line(win,black,[val*2.5,0+20],[val*2.5,h-20],20)
			victory = True
		elif field[0][2] == 'o' and field[1][2] == 'o' and field[2][2] == 'o':
			o_score += 1
			pygame.draw.line(win,black,[val*2.5,0+20],[val*2.5,h-20],20)
			victory = True

		if a == 9:
			victory = True

		view_score()


	pygame.time.Clock().tick(30)
	pygame.display.update()