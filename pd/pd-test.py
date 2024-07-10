import flet as ft
import pandas as pd

def main(page: ft.Page):
    # Create a DataFrame with user data
    data = {'name': ['Alice', 'Bob', 'Charlie']}
    df = pd.DataFrame(data)
    
    # Extract the first user's name
    user_name = df.loc[0, 'name']
    
    # Create a Text control to display the greeting
    greeting = ft.Text(value=f"Hello, {user_name}!", color="green")
    
    # Add the Text control to the page
    page.controls.append(greeting)
    
    # Update the page to reflect changes
    page.update()

ft.app(target=main)
