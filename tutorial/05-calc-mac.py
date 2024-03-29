import flet
from flet import (
    Column,
    Container,
    ElevatedButton,
    Page,
    Row,
    Text,
    border_radius,
    colors,
)


def main(page: Page):
    page.title = "Calc App"
    result = Text(value="0", color=colors.WHITE, size=20)

    page.add(
        Container(
            width=300,
            bgcolor=colors.BLACK,
            border_radius=border_radius.all(20),
            padding=20,
            content=Column(
                controls=[
                    Row(controls=[result], alignment="end"),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="AC",
                                bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="+/-",
                                bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="%",
                                bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="/",
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="7",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="8",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="9",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="*",
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="4",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="5",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="6",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="-",
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="1",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="2",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="3",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="+",
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="0",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=2,
                            ),
                            ElevatedButton(
                                text=".",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="=",
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                            ),
                        ]
                    ),
                ]
            ),
        )
    )


flet.app(target=main)