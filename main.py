import pygame
from random import randint

pygame.init()
win = pygame.display.set_mode((1100,700))
pygame.display.set_caption("Calculator!")
no=randint(0,1000)
col=(210,210,0)

def display():
	win.fill((255,255,255))
	pygame.draw.rect(win,(128,128,128),(0,0,1100,100),10)
	pygame.draw.rect(win,(0,0,0),(0,110,200,100),10)
	pygame.draw.rect(win,(0,0,0),(200,110,200,100),10)
	pygame.draw.rect(win,(0,0,0),(400,110,200,100),10)
	pygame.draw.rect(win,(0,0,0),(600,110,200,100),10)
	pygame.draw.rect(win,(0,0,0),(0,210,200,100),10)
	pygame.draw.rect(win,(0,0,0),(200,210,200,100),10)
	pygame.draw.rect(win,(0,0,0),(400,210,200,100),10)
	pygame.draw.rect(win,(0,0,0),(600,210,200,100),10)
	pygame.draw.rect(win,(0,0,0),(0,310,200,100),10)
	pygame.draw.rect(win,(0,0,0),(200,310,200,100),10)
	pygame.draw.rect(win,(0,0,0),(400,310,200,100),10)
	pygame.draw.rect(win,(0,0,0),(600,310,200,100),10)
	pygame.draw.rect(win,(0,0,0),(0,410,200,100),10)
	pygame.draw.rect(win,(0,0,0),(200,410,200,100),10)
	pygame.draw.rect(win,(0,0,0),(400,410,200,100),10)
	pygame.draw.rect(win,(0,0,0),(600,410,200,100),10)
	pygame.draw.rect(win,(0,0,0),(200,510,200,100),10)
	pygame.draw.rect(win,(0,0,0),(400,510,200,100),10)
	pygame.draw.rect(win,(0,0,0),(600,510,200,100),10)
	pygame.draw.rect(win,(255,0,0),(0,610,800,50),10)
	pygame.draw.rect(win,(143,0,255),(805,105,295,555),10)
	pygame.draw.rect(win,(142,0,255),(830,170,245,20))
	pygame.draw.rect(win,(142,0,255),(830,260,245,20))
	pygame.draw.rect(win,(143,0,255),(0,663,800,50),10)
	pygame.draw.rect(win,(0,0,0),(810,663,290,50),10)
	
	text1=font1.render('1',1,(0,255,0))
	text2=font2.render('2',1,(0,255,0))
	text3=font3.render('3',1,(0,255,0))
	text4=font4.render('4',1,(0,255,0))
	text5=font5.render('5',1,(0,255,0))
	text6=font6.render('6',1,(0,255,0))
	text7=font7.render('7',1,(0,255,0))
	text8=font8.render('8',1,(0,255,0))
	text9=font9.render('9',1,(0,255,0))
	text0=font0.render('0',1,(0,255,0))
	textDE=fontDE.render('DELETE',1,(0,100,100))
	textE=fontE.render('=',1,(0,100,100))
	textP=fontP.render('+',1,(0,100,100))
	textS=fontS.render('-',1,(0,100,100))
	textM=fontM.render('x',1,(0,100,100))
	textD=fontD.render('÷',1,(0,100,100))
	textA=fontA.render(f"{answer}",1,col)
	text_=font_.render("MADE BY OMANSHU",1,(210,210,0))
	textb1=fontb1.render('(',1,(0,100,100))
	textb2=fontb2.render(')',1,(0,100,100))
	textE2=fontE2.render('^',1,(0,100,100))
	textPS=fontPS.render("Previous Input:",1,(0,0,255))
	textPS2=fontPS2.render(f"{PS}",1,(0,0,255))
	textL=fontL.render("Vacant Spaces:",1,(0,0,255))
	textREM=fontREM.render("REM",1,(0,100,100))
	textC=fontC.render("DELETE ALL",1,(0,100,100))
	textG=fontG.render("NUMBER GUESSING GAME !",1,(0,255,200))
	
	VS=17-len(answer)
	textL2=fontL2.render(f"{VS}",1,(0,0,255))
	
	win.blit(text1,(75,130))
	win.blit(text2,(275,130))
	win.blit(text3,(475,130))
	win.blit(text4,(75,230))
	win.blit(text5,(275,230))
	win.blit(text6,(475,230))
	win.blit(text7,(75,330))
	win.blit(text8,(275,330))
	win.blit(text9,(475,330))
	win.blit(text0,(75,430))
	win.blit(textDE,(225,440))
	win.blit(textE,(475,420))
	win.blit(textP,(675,120))
	win.blit(textS,(675,220))
	win.blit(textM,(675,320))
	win.blit(textD,(675,420))
	win.blit(textA,(20,5))
	win.blit(text_,(470,620))
	win.blit(textb1,(75,520))
	win.blit(textb2,(275,520))
	win.blit(textE2,(475,520))
	win.blit(textPS,(820,120))
	win.blit(textPS2,(820,150))
	win.blit(textL,(820,210))
	win.blit(textL2,(820,240))
	win.blit(textREM,(640,540))
	win.blit(textC,(850,675))
	win.blit(textG,(200,675))
	
	pygame.display.update()

answer=""
PS="No Previous Input"

font0=pygame.font.SysFont("comicsans",100,True)
font1=pygame.font.SysFont("comicsans",100,True)
font2=pygame.font.SysFont("comicsans",100,True)
font3=pygame.font.SysFont("comicsans",100,True)
font4=pygame.font.SysFont("comicsans",100,True)
font5=pygame.font.SysFont("comicsans",100,True)
font6=pygame.font.SysFont("comicsans",100,True)
font7=pygame.font.SysFont("comicsans",100,True)
font8=pygame.font.SysFont("comicsans",100,True)
font9=pygame.font.SysFont("comicsans",100,True)
fontP=pygame.font.SysFont("comicsans",100,True)
fontS=pygame.font.SysFont("comicsans",120,True)
fontM=pygame.font.SysFont("comicsans",100,True)
fontD=pygame.font.SysFont("comicsans",100,True)
fontE=pygame.font.SysFont("comicsans",100,True)
fontDE=pygame.font.SysFont("comicsans",50,True)
fontA=pygame.font.SysFont("comicsans",120,True)
fontb1=pygame.font.SysFont("comicsans",100,True)
fontb2=pygame.font.SysFont("comicsans",100,True)
font_=pygame.font.SysFont("comicsans",40,True,True)
fontE2=pygame.font.SysFont("comicsans",130,True)
fontPS=pygame.font.SysFont("comicsans",30,True)
fontPS2=pygame.font.SysFont("comicsans",30,True)
fontL=pygame.font.SysFont("comicsans",30,True)
fontL2=pygame.font.SysFont("comicsans",30,True)
fontREM=pygame.font.SysFont("comicsans",70,True)
fontC=pygame.font.SysFont("comicsans",40,True)
fontG=pygame.font.SysFont("comicsans",40,True)

extra=0
game=False
run=True
while run:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False
		if event.type==pygame.MOUSEBUTTONDOWN:
			mx,my=pygame.mouse.get_pos()
			if mx>10 and my>100 and mx<200 and my<205 and len(answer)<17:
				answer+='1'
				if extra>0:
					extra=0
			if mx>200 and my>100 and mx<400 and my<205 and len(answer)<17:
				answer+='2'
				if extra>0:
					extra=0
			if mx>400 and my>100 and mx<600 and my<205 and len(answer)<17:
				answer+='3'
				if extra>0:
					extra=0
			if mx>600 and my>100 and mx<800 and my<205 and len(answer)>0 and len(answer)<16 and extra==0:
				answer+='+'
				extra+=1
			if mx>10 and my>205 and mx<200 and my<305 and len(answer)<17:
				answer+='4'
				if extra>0:
					extra=0
			if mx>200 and my>205 and mx<400 and my<305 and len(answer)<17:
				answer+='5'
				if extra>0:
					extra=0
			if mx>400 and my>205 and mx<600 and my<305 and len(answer)<17:
				answer+='6'
				if extra>0:
					extra=0
			if mx>600 and my>205 and mx<800 and my<305 and len(answer)<16 and extra==0:
				answer+='-'
				extra+=1
			if mx>10 and my>305 and mx<200 and my<405 and len(answer)<17:
				answer+='7'
				if extra>0:
					extra=0
			if mx>200 and my>305 and mx<400 and my<405 and len(answer)<17:
				answer+='8'
				if extra>0:
					extra=0
			if mx>400 and my>305 and mx<600 and my<405 and len(answer)<17:
				answer+='9'
				if extra>0:
					extra=0
			if mx>600 and my>305 and mx<800 and my<405 and len(answer)>0 and len(answer)<16 and extra==0:
				answer+='*'
				extra+=1
			if mx>10 and my>405 and mx<200 and my<505 and len(answer)<17:
				answer+='0'
				if extra>0:
					extra=0
			if mx>600 and my>405 and mx<800 and my<505 and len(answer)<16 and len(answer)>0 and extra==0:
				answer+='/'
				extra+=1
			if mx>10 and my>505 and mx<200 and my<605 and len(answer)<16:
				if extra>0 or len(answer)==0:
				    answer+='('
				    extra+=1
			if mx>200 and my>505 and mx<400 and my<605 and len(answer)<17 and extra==0 and len(answer)>0:
				answer+=')'
				extra=0
			if mx>400 and my>505 and mx<600 and my<605 and len(answer)<15 and extra==0 and len(answer)>0:
				answer+="**"
				extra+=1
			if mx>600 and mx>505 and mx<800 and my<605 and len(answer)<16 and extra==0 and len(answer)>0:
				answer+='%'
				extra+=1
			if mx>800 and my>663 and mx<1101 and my<713:
				answer=""
			if mx>400 and my>405 and mx<600 and my<505 and game==False:
				try:
				    PS=answer
				    a=eval(answer)
				    answer=str(a)
				except:
					try:
					    answer=answer[:-1]
					    PS=answer
					    a=eval(answer)
					    answer=str(a)
					except:
						answer="Invalid Input"
			if mx>200 and my>405 and mx<400 and my<505 and len(answer)>0:
				answer=answer[:-1]
			if mx>10 and my>663 and mx<800 and my<713:
				col=(0,255,200)
				game=True
				answer="Guess A Number"
			if mx>400 and my>405 and mx<600 and my<505 and game==True:
				try:
				    b=eval(answer)
				    if b>no:
					    answer="Lesser"
				    elif b<no:
				    	answer="Greater"
				    if b==no:
				    	answer="You Won"
				    	col=(210,210,0)
				    	game=False
				except:
					answer="Invalid Input"	
	display()
		
pygame.quit()
