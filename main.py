from flet import *
import time

import pyscreenshot as ImageGrab



def main(page:Page):

	def myscreenshoot(e):
		page = e.control.page
		y = page.window_top
		x = page.window_left
		w = page.window_width
		h = page.window_height

		# PROCESS SCREESHOT
		screen = ImageGrab.grab(
		# AREA FOR YOU SCREENSHOT
			bbox =(x,y,w+x,h+y) 
			)
		# GET TIME FOR NAME YOU FILE UPLOAD
		t = str(time.time())
		myimagelocation = f"assets/{t.split('.')[0]}.png"
		screen.save(myimagelocation)

		# load YOU IIMAGE
		loadimage = Image(src=myimagelocation,fit="contain")

		# PREVIEW IN YOU SCREEN IF SUCCESS SCRENSHOT
		if len(ImageContainer.controls) >= 1:
			ImageContainer.clean()

		# PUSH TO COLUMN
		ImageContainer.controls.append(loadimage)
		page.update()


		



	btn = ElevatedButton("screenshoot",
		on_click=myscreenshoot

		)
	txtinput = TextField("")

	ImageContainer = Column()

	page.add(
		Column([
			Row([
				txtinput,
				btn
				]),
		Text("You screenshot image result",
			size=30,
			weight="bold"

			),
		ImageContainer

			])

		)



flet.app(target=main,assets_dir="assets")

