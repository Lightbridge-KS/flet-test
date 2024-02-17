import flet
from flet import *
 
def main(page:Page):
	page.update()
	def changetab(e):
	# GET INDEX TAB
		my_index = e.control.selected_index
		tab_1.visible = True if my_index == 0 else False
		tab_2.visible = True if my_index == 1 else False
		tab_3.visible = True if my_index == 2 else False
		page.update()
 
 
	page.navigation_bar = NavigationBar(
	bgcolor="blue",
	on_change=changetab,
	selected_index = 0,
	destinations = [
	NavigationDestination(icon="home"),
	NavigationDestination(icon="explore"),
	NavigationDestination(icon="settings"),
	]
	)
 
	tab_1 = Text("Tab 1",size=30,visible=True)
	tab_2 = Text("Tab 2",size=30,visible=False)
	tab_3 = Text("Tab 3",size=30,visible=False)
 
	page.add(
		Container(
		margin = margin.only(
		top=page.window_height/2,
		left=50
 
			),
			content=Column([
				tab_1,
				tab_2,
				tab_3
 
 
				])
 
			)
 
		)
 
flet.app(target=main)